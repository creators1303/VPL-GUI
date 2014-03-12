import pygame
from pygame.locals import *
from data.classes.objects.item import Item
from data.classes.cursorFollower import CursorFollower
from data.classes.window import WindowObj
from data.workers.workerWindows import create_window
from data.workers.workerInteractions import update_interactions
from data.drawer import draw_table
from data.drawer import draw_sec_table


class MainMenu():
    def __init__ (self, screen):
        pygame.mouse.set_visible(False)
        pygame.mouse.get_focused(True)
        pygame.init()
        music1='testBack.aud'
        music2='testBack2.aud'
        #play_file(music1)
        self.screen=screen
        self.size=screen.get_size()
        self.object_list=[]
        self.cur_fol=CursorFollower(self)
        self.wind=WindowObj(self)
        self.parent=screen
        self.myfont = pygame.font.SysFont("monospace", 15)
        create_window(self.wind,'mainMenu')
        self.order=Item(self,[200,100])
        self.chaos=Item(self,[100,100])


        self.order.image_name='Order'
        self.chaos.image_name='Chaos'
        self.order.interactive_name='order'
        self.chaos.interactive_name='chaos'
        #self.chaos.bondedTo=self.rufusRake
        self.create(self.order)
        self.create(self.chaos)

        self.create(self.cur_fol)
        self.create(self.wind)

        print("Damn you, world!")

        self.update()

    @staticmethod
    def follow_object(object1,object2):
        object1.coords=object2.coords

    def update(self):
        '''key=pygame.key.name(event.key)

        print(key)
        basicfont = pygame.font.SysFont(None, 48)
        text=basicfont.render(key, True, (255, 0, 0), (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = self.screen.get_rect().centerx
        textrect.centery = self.screen.get_rect().centery

        self.screen.blit(text, textrect)'''
        timer = pygame.time.Clock () #creating timer
        running=True
        self.coord = list(pygame.mouse.get_rel())
        while running:
            timer.tick() #ticking timer
            for tar_obj in self.object_list:
                tar_obj.update()
                tar_obj.update_state(self.cur_fol)
                update_interactions(self.object_list, self)
                draw_sec_table(self.screen, [tar_obj])
                tar_obj.draw_children(self.screen)
                for child in tar_obj.children:
                    child.update()
                    child.update_state(self.cur_fol)
                #print(read_butts())
            
            draw_table(self.screen,[self.cur_fol])
            event = pygame.event.poll() #getting last event from events stream
            if event.type == pygame.QUIT: #if player press X button on the top of the window
                running = False #reinitialization to stop working function
                break #stopping cycle
            elif event.type == KEYDOWN:
                pressed=pygame.key.get_pressed()
                for key in pressed:
                    if pressed[key]:
                        print(key)
                if event.key == K_ESCAPE:
                    return
            pygame.event.clear() #clearing of events stream

    def create(self,obj):
        self.object_list.append(obj)

    def destroy(self,obj):
        print(obj)
        self.object_list.remove(obj)

    def extrminate(self):
        for obj in self.object_list:
            self.destroy(obj)
