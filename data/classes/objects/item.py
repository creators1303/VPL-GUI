from data.classes.interactiveObject import InteractiveObject
import pygame

class Item(InteractiveObject):
    def __init__ (self, table, coords=None,size=None):
        InteractiveObject.__init__(self,coords,size)
        self.set_snc(coords,size)
        self.state=0
        print("It is an Item.")


    def update_state(self, object):
        if self.state == 0:
            if object.if_crosses(self) and not pygame.mouse.get_pressed()[0]:
                self.state = 1
        if self.state == 1:
            if pygame.mouse.get_pressed()[0]:
                self.state = 2
            if not object.if_crosses(self):
                self.state = 0
        if self.state == 2:
            self.follow_object(object)
            if not pygame.mouse.get_pressed()[0]:
                self.state = 3
        if self.state == 3:
            self.follow_object(object)
            if pygame.mouse.get_pressed()[0]:
                self.state = 4
        if self.state == 4:
            self.follow_object(object)
            if not pygame.mouse.get_pressed()[0]:
                self.state = 0

