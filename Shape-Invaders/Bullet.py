import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, s_height):
        super().__init__()
        self.image = pygame.Surface((4, 15))
        self.image.fill((243, 216, 6))
        self.rect = self.image.get_rect(center = position)
        self.speed = speed

        self.s_height = s_height


    def update(self):
        self.rect.y -= self.speed

        if self.rect.y > self.s_height + 15 or self.rect.y < 0: ## deletes the clone once reach border
            self.kill()
