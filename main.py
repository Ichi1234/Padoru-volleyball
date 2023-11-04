import pygame
from character import Player_1, Player_2


BACKGROUND = "bg/Padoru_bg by Parker Gaijin.png"
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

#set up pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #resolution of the game
clock = pygame.time.Clock()
pygame.display.set_caption("Padoru-volleyball")

#Background surface
bg_surface = pygame.image.load(BACKGROUND)
bg_rect = bg_surface.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))


#indicator
player_1 = pygame.sprite.GroupSingle()
player_1.add(Player_1())

player_2 = pygame.sprite.GroupSingle()
player_2.add(Player_2())



running = True #variable for game + event loop

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_ESCAPE:
            running = False

    #print() player to screen
    screen.blit(bg_surface, bg_rect)
    player_1.draw(screen)
    player_1.update()

    player_2.draw(screen)
    player_2.update()





    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
