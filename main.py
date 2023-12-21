import pygame
from character import Player_1, Player_2
from ball import Ball
import threading

# def collision(player):
#     if pygame.sprite.spritecollide(player.sprite, ball, False):
#
#         return True
#     return False

###TODO Make game scale with user resolution (move, spawn) How to do? IDK!!!
GAME_BACKGROUND = "bg/Background.png"
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

#set up pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #resolution of the game
clock = pygame.time.Clock()
pygame.display.set_caption("Padoru-volleyball")

#Background surface
bg_surface = pygame.image.load(GAME_BACKGROUND)
bg_rect = bg_surface.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

#Net surface
net_surface = pygame.image.load("bg/Bonk.png").convert_alpha()
net_surface = pygame.transform.smoothscale(net_surface, (25, 230))
net_rect = net_surface.get_rect(midbottom=(SCREEN_WIDTH / 2, 700))


#indicator
player_1 = Player_1(SCREEN_WIDTH)
player_2 = Player_2(SCREEN_WIDTH)
ball = Ball(screen)

# player_1 = pygame.sprite.GroupSingle()
# player_1.add(Player_1(SCREEN_WIDTH))
#
# player_2 = pygame.sprite.GroupSingle()
# player_2.add(Player_2(SCREEN_WIDTH))
#
# net = pygame.sprite.GroupSingle()
# net.add(Net(SCREEN_WIDTH))
#
# ball = pygame.sprite.GroupSingle()
# ball.add(Ball(screen))


running = True #variable for game + event loop

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    #print() player to screen
    screen.blit(bg_surface, bg_rect)
    # player_1.draw(screen)
    screen.blit(player_1.image, player_1.rect)
    rect = player_1.update()


    # player_2.draw(screen)
    screen.blit(player_2.image, player_2.rect)
    player_2.update()

    #Position
    player1_pos = player_1.rect.left, player_1.rect.right , player_1.rect.top , player_1.rect.y
    player2_pos = player_2.rect.left, player_2.rect.right , player_2.rect.top
    net_pos = net_rect.left, net_rect.right , net_rect.top

    # net.draw(screen)
    # net.update()
    screen.blit(net_surface, net_rect)


    screen.blit(ball.image, ball.rect)
    # ball.draw(screen)
    ball.update(player_1.rect, player_2.rect, net_rect)



    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
