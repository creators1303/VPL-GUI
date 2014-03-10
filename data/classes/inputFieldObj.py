from data.classes.interactiveObject import InteractiveObject

class InputFiledObj(InteractiveObject):
    def __init__(self, table, coords=None,size=None):
        InteractiveObject.__init__(self,coords,size)
        self.table=table
        self.set_snc(coords,size)
        self.focused=False
        self.text_field=[]
        self.image_name='input'
        self.image_state='stand'
        self.prop=[]
        print("Input field born.")

    def state_action(self):
        self.pressed_action(self.table)

    def clear_field(self):
        self.text_field=[]
        

    def pressed_action(self, table):
        if self.focused:
            self.focused=False
        else:
            self.focused=True
