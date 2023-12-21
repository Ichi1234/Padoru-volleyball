"""
This module have everything about player1, player2, volleyball net
"""
import pygame


#image for player surface
player_1_image = "characters/Ichi_Padoru.png"
player_2_image = "characters/MamoruEiji_Padoru.png"


class Player_1:

    def __init__(self, screen_width):
         #load image from directory
         self.image = pygame.image.load(player_1_image).convert_alpha()
         self.image = pygame.transform.smoothscale(self.image, (180, 180))  #scale image down
         self.image = pygame.transform.flip(self.image, True, False) #flip image in x-axis
         self.rect = self.image.get_rect(midbottom= (1200, 700))
         #gravity
         self.player_gravity = 0

         #screen
         self.screen_width = screen_width
    def move(self, player):
        #if user press any keys
        key = pygame.key.get_pressed()

        if player == 1: #player 1 movement
            if key[pygame.K_LEFT] and self.rect.left >= self.screen_width/2:
                self.rect.x -= 10
            if key[pygame.K_RIGHT] and self.rect.right <= self.screen_width:
                self.rect.x += 10

        elif player == 2: #player 2 movement
            if key[pygame.K_a] and self.rect.left >= 0:
                self.rect.x -= 10
            if key[pygame.K_d] and self.rect.right <= self.screen_width/2:
                self.rect.x += 10

    def jump(self, player):
        # if user press any keys
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.bottom >= 700 and player == 1: #player 1 jump
            self.player_gravity = -20
        if key[pygame.K_w] and self.rect.bottom >= 700 and player == 2: #player 2 jump
            self.player_gravity = -20

    def gravity(self):
        self.player_gravity  += 1 #constant increase gravity
        self.rect.y += self.player_gravity #F = mg
        if self.rect.bottom >= 700: #prevent player under the ground
            self.rect.bottom = 700


    def update(self): #sent these method to main
        self.gravity()
        self.jump(1)
        self.move(1)
        return self.rect

class Player_2(Player_1):
    #get every method from Player_1 class
    def __init__(self, screen_width):
         super().__init__(screen_width)
         self.image = pygame.image.load(player_2_image).convert_alpha()
         self.image = pygame.transform.smoothscale(self.image, (180, 180))  #scale image down
         self.rect = self.image.get_rect(midbottom= (200, 700))
         self.player_gravity = 0
    def update(self):
        self.gravity()
        self.jump(2)
        self.move(2)


# class Net:
#     def __init__(self, screen_width):
#         self.image = pygame.image.load("bg/Bonk.png").convert_alpha()
#         self.image = pygame.transform.smoothscale(self.image, (25, 250))
#         self.rect = self.image.get_rect(midbottom=(screen_width / 2, 700))
#
#     def update(self):
#         pass