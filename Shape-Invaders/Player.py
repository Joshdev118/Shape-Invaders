import pygame
from Bullet import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self, s_width, s_height):
        super().__init__()
        self.s_width = s_width
        self.s_height = s_height
        self.widthOffset = 50
        self.image = pygame.image.load("Image/Player.png")
        self.image = pygame.transform.scale(self.image, 
                                            (self.image.get_width() * 1.5, 
                                             self.image.get_height() * 1.5))
        self.image.fill((243, 216, 63))
        self.rect = self.image.get_rect(midbottom = (self.s_width // 2, self.s_height))
        self.speed = 6

        self.LaserGroup = pygame.sprite.Group()
        self.laser_Ready = True
        self.laser_delay = 500
        self.lastLaser = 0
        self.lasersfx = pygame.mixer.Sound("SFX/laserShoot.wav")



    def getInput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: ## right keys
            self.rect.x += self.speed

        if keys[pygame.K_a] or keys[pygame.K_LEFT]: ## left keys
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.laser_Ready:  ## shoot key
            self.laser_Ready = False
            self.lasersfx.play()
            laser = Laser(self.rect.center, 6, self.s_height)
            self.LaserGroup.add(laser)

            self.lastLaser = pygame.time.get_ticks()

            
    def update(self):
        self.getInput()
        self.movementBounds()

        self.LaserGroup.update()
        self.laserImmune()

    def movementBounds(self):
        if self.rect.right > self.s_width - self.widthOffset:
            self.rect.right = self.s_width - self.widthOffset

        if self.rect.left < self.widthOffset:
            self.rect.left = self.widthOffset

    def laserImmune(self):
        if not self.laser_Ready:
            currentTime = pygame.time.get_ticks()
            if currentTime - self.lastLaser >= self.laser_delay:
                self.laser_Ready = True

    def setup(self):
        self.rect = self.image.get_rect(midbottom = (self.s_width // 2, self.s_height))
