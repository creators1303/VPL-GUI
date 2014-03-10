from data.classes.object import Object
import pygame

class InteractiveObject(Object):
    def __init__ (self, table, coords=None,size=None):
        Object.__init__(self,table,coords,size)
        self.set_snc(coords,size)
        self.interactive=True
        self.interaction_state=0
        print("It is an Interactive Object.")

    def update_state(self, object):
        if self.state == 0:
            self.image_state='Stand'
            if object.if_crosses(self) and not pygame.mouse.get_pressed()[0]:
                self.state = 1
        if self.state == 1:
            self.image_state='Hig'
            if not object.if_crosses(self):
                self.state = 0
            elif pygame.mouse.get_pressed()[0]:
                self.state_action()
                self.state = 2
        if self.state == 2:
            self.image_state='Pres'
            if not pygame.mouse.get_pressed()[0]:
                self.state = 1
            elif not object.if_crosses(self):
                self.state = 3
        if self.state == 3:
            self.image_state='Rel'
            if not pygame.mouse.get_pressed()[0]:
                self.state = 1
            elif object.if_crosses(self):
                self.state = 2


    def state_action(self):
        pass

    def pressed_action(self):
        print(self," pressed.")
