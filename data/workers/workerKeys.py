import pygame

def read_butts():
    if pygame.key.get_focused:
        for count in range (0,len(pygame.key.get_pressed())):
            if pygame.key.get_pressed()[count]!=0:
                return pygame.key.name(count)