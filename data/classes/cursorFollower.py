from data.classes.object import Object
import pygame

class CursorFollower(Object):
    def __init__ (self, table, coords=None,size=None):
        Object.__init__(self, table)
        self.state=1
        self.carried=0
        self.set_snc(coords,size)
        self.image_name='Cursor'
        print("Cursor follower born.")


    def image_update(self):
        if self.state==0:
            return 'blank.tex'
        elif self.state==1:
            return 'testCursor.tex'

    def update(self):
        self.follow_cursor()

    def update_state(self,object_obj):
        pass

    def follow_cursor(self):
        self.coords=pygame.mouse.get_pos()
