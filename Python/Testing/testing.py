import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Testing")
screen = pygame.display.get_surface()

class player(object):
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (0, 0, 128), (64, 54, 16, 16))
        self.dist = 10
    
    def movement(self):
        for e in pygame.event.get():
            if e == pygame.QUIT:
                pygame.quit(); exit()
            
            elif e.type == KEYDOWN:
                key = e.key
                if key == K_w:
                    self.draw_rect(0, -1)
                elif key == K_s:
                    self.draw_rect(0, 1)
                elif key == K_a:
                    self.draw_rect(-1, 0)
                elif key == K_d:
                    self.draw_rect(1, 0)
                elif key == K_ESCAPE:
                    pygame.quit(); exit()
    
    def draw_rect(self,x,y):
        screen.fill((255, 255, 255))
        self.rect = self.rect.move(x*self.dist, y*self.dist); pygame.draw.rect(screen, (0, 0, 128), self.rect)
        pygame.display.update()
    
    def draw(self,surface):
        pygame.draw.rect(screen, (0, 0, 128), (64, 54, 16, 16))
        
        
class Player(object):
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (0, 0, 128), (64, 54, 16, 16))
        self.dist = 10

    def handle_keys(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit(); exit()
            elif e.type == KEYDOWN:
                key = e.key
                if key == K_LEFT:
                    self.draw_rect(-1, 0)
                elif key == K_RIGHT:
                    self.draw_rect(1, 0)
                elif key == K_UP:
                    self.draw_rect(0, -1)
                elif key == K_DOWN:
                    self.draw_rect(0, 1)
                elif key == K_ESCAPE:
                    pygame.quit(); exit()

    def draw_rect(self,x,y):
        screen.fill((255, 255, 255))
        self.rect = self.rect.move(x*self.dist, y*self.dist); pygame.draw.rect(screen, (0, 0, 128), self.rect)
        pygame.display.update()

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), (64, 54, 16, 16))

player2 = Player()        
player1 = player()
#clock = pygame.time.Clock()
screen.fill((255, 255, 255))
player1.draw(screen)
player2.draw(screen)

pygame.display.update()

while True:
    object()
    player1.movement()
    player2.handle_keys()