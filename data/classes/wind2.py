


class WindowObj(Object):
    def __init__(self, table, coords=[0,0],size=[500,500]):
        Object.__init__(self, table, coords,size)
        self.children=[]
        self.setSnC(coords,size)
        self.imageName='window'
        self.imageState='stand'
        print("Window born.")

    def virtual_return_image(self):
            return 'testWindow.hmtex'

    def childrenUpdate(self):
        #print(self.children)
        for tarObj in self.children:
            tarObj.update()
            tarObj.updateState(self.table.curFol)
            updateInteractions(self.children, self)
        drawSecTable(self.table.screen, [self])
        drawSecTable(self.table.screen, self.children)

    def update(self):
        self.childrenUpdate()

    def stateAction(self):
        pass

    def removeChild(self,table,child):
        print(table)
        self.children.remove(child)

    def removeChildren(self, table):
        for child in self.children:
            self.removeChild(table,child)
