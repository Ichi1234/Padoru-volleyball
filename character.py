"""
This is character module it's control everything of character
"""
import pygame

#image for player surface
player_1_image = "characters/Padoru 2021 by Ichi (myself).png"
player_2_image = "characters/MamoruEiji padoru.png"
class Player_1(pygame.sprite.Sprite):

    def __init__(self):
         super().__init__()
         #load image from directory
         self.image = pygame.image.load(player_1_image).convert_alpha()
         self.image = pygame.transform.smoothscale(self.image, (250, 250))  #scale image down
         self.rect = self.image.get_rect(midbottom= (200, 700))
         #gravity
         self.player_gravity = 0

    def jump(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.rect.bottom >= 700:
            self.player_gravity = -20
    def gravity(self):
        self.player_gravity  += 1
        self.rect.y += self.player_gravity
        if self.rect.bottom >= 700:
            self.rect.bottom = 700

    def update(self):
        self.gravity()
        self.jump()


class Player_2(pygame.sprite.Sprite):

    def __init__(self):
         super().__init__()
         self.image = pygame.image.load(player_2_image).convert_alpha()
         self.image = pygame.transform.smoothscale(self.image, (250, 250))  #scale image down
         self.image = pygame.transform.flip(self.image, True, False)
         self.rect = self.image.get_rect(midbottom= (1200, 700))
