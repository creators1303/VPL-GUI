import pygame
from data.mainMenu import MainMenu

def main ():
    '''main function of the game'''
    ##preparing window
    pygame.init() #initialization of pygame module
    resolution=[800,600]
    '''resolution[0]=input('Width')
    resolution[1]=input("Height")'''
    screen = pygame.display.set_mode(resolution) #creating window object
    pygame.display.set_caption('BeholderJackGui vA.1.1.4') #naming window

    ##ending program
    menu=MainMenu(screen)
    pygame.quit() #closing window

if __name__ == '__main__': main()
