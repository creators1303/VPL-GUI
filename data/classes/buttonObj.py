from data.classes.interactiveObject import InteractiveObject

class ButtonObj(InteractiveObject):
    def __init__(self, table, coords=None,size=None):
        InteractiveObject.__init__(self,coords,size)
        self.table=table
        self.set_snc(coords,size)
        self.image_name='button'
        self.image_state='stand'
        self.prop=[]
        print("Button born.")

    def state_action(self):
        self.pressed_action(self.table)

    def pressed_action(self, table):
        from data.workers.workerWindows import update_buttons
        update_buttons(self, table, self.prop)
