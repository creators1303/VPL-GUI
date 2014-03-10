import pygame
from pygame import *

namesArr=[]
filesArr=[]
animArr=[]

def get_image(name, state, size, alpha, reset):
    if not reset:
        for count in range(0,len(namesArr)):
            if name+'.'+state==namesArr[count]:
                returner = pygame.transform.scale (filesArr[count], size)
                return returner
    file=load_image(name, state, alpha)
    namesArr.append(name+'.'+state)
    filesArr.append(file)
    file = pygame.transform.scale (file, size)
    return file


def load_image(name, state, alpha): #function, that loads image_obj from file
    try: #if image_obj exists
        print('data/textures/' + name +'/'+state+'.tex')
        image_obj = pygame.image.load ('data/textures/' + name +'/'+state+'.tex').convert() #loading and preparing image_obj from file
    except ZeroDivisionError: #if image_obj doesn't exist
        print('ImageLoading: failed to load ' + name)
        try:
            image_obj = pygame.image.load ('data/textures/Error/Stand.tex').convert()
        except ZeroDivisionError:
            error_message('ImageLoading: I cannot even load error pic!')
    image_obj.set_colorkey (image_obj.get_at((0,0)), RLEACCEL) #making transparent pixels on image_obj
    image_obj.set_alpha(alpha)
    #image_obj = pygame.transform.scale (image_obj, size) #changing size of image_obj
    print('loaded',name)
    return image_obj

def error_message(info):
    print("Wild error appears!")
    print(info)
    sys.exit()
