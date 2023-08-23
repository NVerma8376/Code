import pygame
from pygame.locals import *
from random import *

# Init
pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill((255,255,255))
sprite = pygame.sprite.Group()


#Setup
color = (0,255,200)
color2 = (255,255,0)
pygame.draw.circle(screen,color, (400, 400), 400, 0)

class point(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill((0,0,0))
        pygame.draw.circle(self.image, color2, (x,y), 10, 0)
        self.rect = self.image.get_rect()
    
#calculate
dots = 20
#pygame.draw.circle(screen,color, (1, 1), 5, 0)


for i in range(0,dots):
    x = randrange(0,800)
    y = randrange(0,800)
    circle1 = point(x,y)
    sprite.add(circle1)


#print(n/d)
         
        


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    sprite.update()
    sprite.draw(screen)
    pygame.display.flip()