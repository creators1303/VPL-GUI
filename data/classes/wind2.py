from data.classes.object import Object
from data.drawer import draw_sec_table
from data.workers.workerInteractions import update_interactions


class WindowObj(Object):
    def __init__(self, table, coords=None,size=None):
        Object.__init__(self, table, coords,size)
        self.children=[]
        self.set_snc(coords,size)
        self.image_name='window'
        self.image_state='stand'
        print("Window born.")

    @staticmethod
    def virtual_return_image():
            return 'testWindow.hmtex'

    def children_update(self):
        #print(self.children)
        for tarObj in self.children:
            tarObj.update()
            tarObj.updateState(self.table.curFol)
            update_interactions(self.children, self)
        draw_sec_table(self.table.screen, [self])
        draw_sec_table(self.table.screen, self.children)

    def update(self):
        self.children_update()

    def state_action(self):
        pass

    def remove_child(self,table,child):
        print(table)
        self.children.remove(child)

    def remove_children(self, table):
        for child in self.children:
            self.remove_child(table,child)
