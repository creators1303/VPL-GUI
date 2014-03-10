import pygame

from data.workers.workerImage import get_image


def draw_table(screen, object_list): #function, that draws hexes
    draw_sec_table(screen,object_list)
    pygame.display.flip () #updating the screen
    screen.fill ((255, 255, 255)) #making white background

def draw_sec_table(screen,object_list):
    for tar_obj in object_list:
        coords=tar_obj.giveCoords()
        if tar_obj.picType[0]==1:
            pic_type=0
            state=str(tar_obj.animCounter[0])
        else:
            state=tar_obj.imageState
        name=tar_obj.returnImage()
        print(name)
        image=get_image(name,state,tar_obj.size,255,False) #image to display
        screen.blit (image,coords) #drawing image on screen
