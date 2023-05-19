from pygame import *
pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True


def new_func():
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False


while running:
    new_func()
