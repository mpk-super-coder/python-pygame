import pygame
from pygame.locals import *

pygame.init()
win = pygame.display.set_mode((500,500))

#events
running = True
while running:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            running=False

pygame.quit()
