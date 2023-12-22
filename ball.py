import pygame
import threading
class Ball:

    def __init__(self, screen):
        self.image = pygame.image.load("ball/Circle Ichi.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (120, 120))
        self.rect = pygame.draw.circle(screen, "black", (500, 300), 50)
        self.ball_gravity = 0
        self.force_x = 10
        self.bounce = False


    def gravity(self):
        self.ball_gravity = 9

        if self.rect.bottom >= 700:  # prevent ball under the ground
            self.rect.bottom = 700
            self.bounce = True

        if self.rect.top <= 30:
            self.rect.top = 30
            self.bounce = False

        if not self.bounce:
              # constant increase gravity
            self.rect.y += self.ball_gravity  # F = mg

        elif self.bounce:

            self.rect.y -= self.ball_gravity  # F = mg

    def positive_x_force(self):
        if self.force_x >= 0:
            return True
        else:
            return False

    def left_right(self, rect_of_object):

        # if ball collide with object it will bounce
        if rect_of_object and self.rect.colliderect(rect_of_object):

            if self.rect.right == rect_of_object.left:
                if self.positive_x_force():
                    self.force_x += 15
                else:
                    self.force_x -= 15
                self.bounce = False

            elif self.rect.left == rect_of_object.right:
                if self.positive_x_force():
                    self.force_x += 15
                else:
                    self.force_x -= 15
                self.bounce = False

                # Check bottom collision
            elif self.rect.bottom >= rect_of_object.top:
                self.force_x = 0
                self.bounce = True

            self.force_x *= -1



    def newton_third_law(self, collide_player1, collide_player2, net):
        self.rect.x += self.force_x ###TODO remove this when make hit
        #bounce left and right screen
        if self.rect.right >= 1300 or self.rect.left <= 50:
            self.force_x *= -1

        # all collide
        self.left_right(collide_player1)

        self.left_right(collide_player2)

        # if ball collide with object it will bounce
        if net and self.rect.colliderect(net):
            self.force_x *= -1



    def update(self, collide_player1, collide_player2, net):
        self.gravity()
        self.newton_third_law(collide_player1, collide_player2, net)

