import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        path = f"Image/Enemy_{type}.png"
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, 
                                            (self.image.get_width() * 1.5, 
                                             self.image.get_height() * 1.5))
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self, direction):
        self.rect.x += direction
