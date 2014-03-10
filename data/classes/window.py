from data.classes.object import Object
from data.workers.workerInteractions import update_interactions


class WindowObj(Object):
    def __init__(self, table, coords=None,size=None):
        Object.__init__(self, table, coords,size)
        self.set_snc(coords,size)
        self.image_name='window'
        self.image_state='stand'
        print("Window born.")

    def virtual_return_image(self):
            return 'testWindow.hmtex'

    def children_update(self):
        #print(self.children)
        for tarObj in self.children:
            tarObj.update()
            tarObj.update_state(self.table.curFol)
            update_interactions(self.children, self)
        '''draw_sec_table(self.table.screen, [self])
        draw_sec_table(self.table.screen, self.children)'''

    def update(self):
        self.children_update()

    def state_action(self):
        pass

    def create(self,obj):
        self.children.append(obj)

    def destroy(self,obj):
        print('Error',self,self.children,obj)
        self.children.remove(obj)

    def exterminate(self):
        print('EXTERMINATE')
        for obj in self.children:
            self.destroy(obj)
