import pygame, random
from Player import Player
from Obstacle import Obstacle
from Obstacle import grid
from Enemy import Enemy
from Bullet import Laser

class Game(pygame.sprite.Sprite):
    def __init__(self, s_width, s_height):
        self.s_width = s_width
        self.s_height = s_height 
        self.run = True
        self.win = False

        # Player            
        self.PlayerGroup = pygame.sprite.GroupSingle()
        self.PlayerGroup.add(Player(self.s_width, self.s_height))
        self.playerHitSFX = pygame.mixer.Sound("SFX/hitHurt.wav")
        self.playerLive = 3

        # Obstacle 
        self.obstacles = self.createObstacles()

        # Enemy
        self.EnemyGroup = pygame.sprite.Group()
        self.createEnemies()
        self.enemy_direction = 1
        self.enemy_LaserGroup = pygame.sprite.Group()
        self.speed = 3


    def createObstacles(self):
        obstacle_width = len(grid[0] * 3)
        gap = (self.s_width - (4 * obstacle_width))/5
        obstacles = []
        for i in range(4):
            offset_x = (i + 1) * gap + i * obstacle_width
            obstacle = Obstacle(offset_x, self.s_height - 100)
            obstacles.append(obstacle)
        return obstacles
    
    def createEnemies(self):
        for row in range(4):
            for column in range(8):
        
                if (row == 0):               # randommizer for different types of enemies
                    enemy_type = 3
                elif (row == 1 or row == 2):
                    enemy_type = 2
                else :
                    enemy_type = 1

                enemy = Enemy(enemy_type, 150 + column * 70, 55 + row * 60)  # size of the group
                self.EnemyGroup.add(enemy)

    def moveEnemies(self):      ## move enemies between left and right
        self.EnemyGroup.update(self.enemy_direction)
        
        for enemy in self.EnemyGroup.sprites():             
            if enemy.rect.right >= self.s_width - 100:
                self.enemy_direction = -1 * self.speed
                self.moveEnemiesDown(2)
            elif enemy.rect.left <= 100:
                self.enemy_direction = 1 * self.speed
                self.moveEnemiesDown(2)

    def moveEnemiesDown(self, distance):    ## moving the enemies down
        for enemy in self.EnemyGroup.sprites():
            enemy.rect.y += distance

    def shootEnemyLaser(self):      ## enemy's laser

        if self.EnemyGroup.sprites():  #checking whether an enemy is present
            choosenEnemy1 = random.choice(self.EnemyGroup.sprites())
            choosenEnemy2 = random.choice(self.EnemyGroup.sprites())

            laserSprite = Laser(choosenEnemy1.rect.center, -6, self.s_height)
            self.enemy_LaserGroup.add(laserSprite)
            laserSprite = Laser(choosenEnemy2.rect.center, -6, self.s_height)
            self.enemy_LaserGroup.add(laserSprite)

    def checkForCollisions(self):   ## check for bullet hits for enemy
        if (self.PlayerGroup.sprite.LaserGroup):

            for PlayerLaser in self.PlayerGroup.sprite.LaserGroup:

                if pygame.sprite.spritecollide(PlayerLaser, self.EnemyGroup, True):
                    PlayerLaser.kill()

            for obstacle in self.obstacles:
                if pygame.sprite.spritecollide(PlayerLaser, obstacle.BlockGroup, True):
                    PlayerLaser.kill()

        if self.enemy_LaserGroup:
            
            for EnemyLaser in self.enemy_LaserGroup:
                if pygame.sprite.spritecollide(EnemyLaser, self.PlayerGroup, False):
                    EnemyLaser.kill()

                    self.playerLive -= 1
                    self.playerHitSFX.play()
                    if (self.playerLive == 0):
                        self.gameOver()

                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(EnemyLaser, obstacle.BlockGroup, True):
                        EnemyLaser.kill()

        if self.EnemyGroup:
            
            for enemy in self.EnemyGroup:
                for obstacle in self.obstacles:

                    pygame.sprite.spritecollide(enemy, obstacle.BlockGroup, True)

                if pygame.sprite.spritecollide(enemy, self.PlayerGroup, False):
                    self.playerHitSFX.play()
                    self.gameOver()         

    def gameOver(self):
        self.run = False

    def reset(self):
        self.win = False
        self.run = True
        self.playerLive = 3
        self.PlayerGroup.sprite.setup()
        self.enemy_LaserGroup.empty()
        self.EnemyGroup.empty()
        self.obstacles = self.createObstacles()
        self.createEnemies()

                


