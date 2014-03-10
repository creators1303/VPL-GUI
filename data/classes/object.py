from data.workers.workerAnimation import animate

class Object():
    def __init__(self, table, coords=None,size=None):
        self.coords=[0,0]
        self.size=[10,10]
        self.parent=table
        self.set_snc(coords,size)
        self.state = 0
        self.interactive=False
        self.bonded_to=0
        self.children=[]
        self.table=table
        self.pic_type=[0,0,0]
        self.image_name='standartPic'
        self.image_state='stand'
        self.animation_name='standartAnim'
        self.anim_counter=[0,0]
        self.interactive=False
        self.interactive_name=0
        self.crossable=True
        self.carrier=0
        print('It is an Object.')

    def set_snc(self,coords,size):
        if not coords is None:
            self.coords[0]=coords[0]
            self.coords[1]=coords[1]
        if not size is None:
            self.size[0]=size[0]
            self.size[1]=size[1]

    def follow_object(self,object):
        if self.bonded_to!=0:
            self.bonded_to.follow_object(object)
        else:
            self.coords[0]=object.coords[0]-5
            self.coords[1]=object.coords[1]-5

    def give_coords(self):
        if self.bonded_to!=0:
            #print(self,' ',self.bondedTo,' ',self.coords[0],'2',self.bondedTo.giveCoords()[0],'3', self.coords[1],'4',self.bondedTo.giveCoords()[1])
            return [self.coords[0]+self.bonded_to.giveCoords()[0], self.coords[1]+self.bonded_to.giveCoords()[1]]
        else:
            return self.coords

    def if_crosses(self, obj):
        coords1= self.give_coords()
        coords2= obj.give_coords()
        size1=self.size
        size2=obj.size
        #print(size1, size2, coords1,coords2)
        if coords1[0] + size1[0] >coords2[0] and coords1[0] < coords2[0] + size2[0] and \
        coords1[1] + size1[1] > coords2[1] and coords1[1] < coords2[1] + size2[1] and self.crossable==True and obj.crossable==True:
            if self.bonded_to!=0:
                pass
                #self.bondedTo.set_crossables(False)
            return True
        else:
            if self.bonded_to!=0:
                pass
                #self.bondedTo.set_crossables(True)
            return False

    def set_crossables(self,state):
        self.crossable=state
        if self.bonded_to!=0:
            self.bonded_to.set_crossables(state)

    def image_update(self):
        pass

    def update_state(self, object):
        pass

    def give_table(self):
        if self.bonded_to!=0 and self.bonded_to!=self:
            print(':D',self.bonded_to)
            return self.bonded_to.give_table()
        else:
            return self.table

    def return_image(self):
        if self.pic_type[0]==1:
            self.image_name=animate(self.animation_name,self.anim_counter[0])
            self.anim_counter[1]+=1
            if self.anim_counter[1]>self.pic_type[2]:
                self.anim_counter[1]=0
                self.anim_counter[0]+=1
                if self.anim_counter[0]>self.pic_type[1]:
                    self.anim_counter[0]=0
        return self.image_name

    def update(self):
        pass

    def virtual_return_image(self):
        return 'error.tex'

    def check_size(self):
        for counter in range(0,2):
            if self.size[counter]=='full':
                if self.bonded_to==0:
                    print('!!!',self.table.size[counter])
                    self.size[counter]=self.table.size[counter]
                else:
                    self.size[counter]=self.bonded_to.size[counter]
        print(self, self.size)

    def draw_children(self, table):
        from data.drawer import draw_sec_table
        for count in self.children:
            draw_sec_table(table,[count])
            if len(count.children)!=0:
                count.draw_children(table)