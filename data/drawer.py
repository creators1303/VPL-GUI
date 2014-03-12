import pygame
from pygame.locals import *
from data.workers.workerImage import get_image

pygame.init()
myfont = pygame.font.SysFont("monospace", 15)

def draw_table(screen, object_list): #function, that draws hexes
    draw_sec_table(screen,object_list)
    pygame.display.flip () #updating the screen
    screen.fill ((255, 255, 255)) #making white background

def draw_sec_table(screen,object_list):
    for tar_obj in object_list:
        coords=tar_obj.give_coords()
        if tar_obj.pic_type[0]==1:
            pic_type=0
            state=str(tar_obj.anim_counter[0])
        else:
            state=tar_obj.image_state
        name=tar_obj.return_image()
        image=get_image(name,state,tar_obj.size,255,False) #image to display
        screen.blit (image,coords) #drawing image on screen
        if tar_obj.dis_text!=None:
            draw_text(screen,tar_obj)


def draw_text(screen,obj):
    label = myfont.render(obj.dis_text, 1, (255,255,0))
    screen.blit(label, obj.give_coords())