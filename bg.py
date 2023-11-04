import pygame

class Bg(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bg/Padoru_bg by Parker Gaijin.png").convert_alpha()
        self.rect = self.image.get_rect(center=(700, 400))

    def update(self):
        pass
