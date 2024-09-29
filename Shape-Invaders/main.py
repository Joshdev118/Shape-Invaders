import pygame
from Game import Game

pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH , HEIGHT + 100))
pygame.display.set_caption("Shape Invaders")
GREY = (29, 29, 27)
clock = pygame.time.Clock()
YELLOW = (243, 216, 63)

FONT = pygame.font.Font("Font/PixelFont.ttf", 13)
levelSurface = FONT.render("LEVEL 01", False, YELLOW)
gameOver = FONT.render("GAME OVER", False, YELLOW)
win = FONT.render("SPACE To Play Again!", False, YELLOW)

game = Game(WIDTH, HEIGHT)

SHOOTLASER = pygame.USEREVENT
pygame.time.set_timer(SHOOTLASER, 300)


def main():

    run = True
    while run:
        # speed = FONT.render(str(game.EnemyGroup.sprites.speed_), False, YELLOW)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                break
                pygame.quit()
            
            if event.type == SHOOTLASER and game.run == True:  ## shooting delay for enemy
                        game.shootEnemyLaser()

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and (game.run == False or game.win == True):
                game.reset()


        if game.run:
            game.PlayerGroup.update()
            game.moveEnemies()
            game.enemy_LaserGroup.update()
            game.checkForCollisions()

        WIN.fill(GREY)
        pygame.draw.rect(WIN, YELLOW, (10, 10, 880, 580), 2, 0, 60, 60, 60, 60)
        pygame.draw.line(WIN, YELLOW, (20, 535), (860, 535), 3)

        if not game.run and not game.win:
            WIN.blit(gameOver, (700, 550, 15, 15))
        elif game.win:
            WIN.blit(win, (600, 550, 10, 10))

        if not game.EnemyGroup:
            game.gameOver()
            game.win = True

        x = 60
        for life in range(game.playerLive):
            WIN.blit(game.PlayerGroup.sprite.image, (x, 550))
            x += 50

        game.PlayerGroup.draw(WIN)
        game.PlayerGroup.sprite.LaserGroup.draw(WIN)
        game.enemy_LaserGroup.draw(WIN)

        for obstacle in game.obstacles:
            obstacle.BlockGroup.draw(WIN)

        game.EnemyGroup.draw(WIN)


        pygame.display.update()
        clock.tick(60)

    

if __name__ == "__main__":
    main()