import random
import pygame
WIDTH = 100
HEIGHT = 200
WHITE = (255 , 255 ,255)
BLUE = (0 , 0 , 255)
RED = (255 , 0 , 0)

game_display = pygame.display.set_mode(WIDTH,HEIGHT)
pygame.display.set_caption('Pravin Game')
clock = pygame.time.Clock()
class Blob:
    def __init__(self,color):
        self.x = random.randrange(0,WIDTH)
        self.y = random.randrange(0,HEIGHT)
        self.size = random.randrange(4,8)
        self.color = color

    def move(self):
        self.move_x = random.randrange(-1,2)
        self.move_y = random.randrange(-1,2)
        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH:
            self.x = WIDTH

        if self.y < 0:
            self.y = 0
        elif self.y > WIDTH:
            self.y = WIDTH

class DrawEnviroment():
    game_display.fill(WHITE)
    
    pygame.display.update()





