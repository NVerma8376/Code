import pygame
from pygame.locals import *
from random import *

#Variables
width = 100
height = 30
color = [0,0,255]

# Init
pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill((255,255,255))
sprite = pygame.sprite.Group()
x = 400
y = 400

class rectangle(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(400, 400, width, height))
  
        self.rect = self.image.get_rect()
        
#Setup
rect = rectangle(x,y,width,height,color)
sprite.add(rect)   
        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    sprite.update()
    sprite.draw(screen)
    pygame.display.flip()   