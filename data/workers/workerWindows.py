import sys, pygame
from data.classes.buttonObj import ButtonObj
from data.classes.window import WindowObj
from data.classes.objects.item import Item


def load_preset(name):
    print('Loading:',name)
    try:
        file = open('data/txts/presets/' + name +'.txt')
        info = file.readlines()
        file.close()
    except IOError:
            error_message(("Loading:", "not found " + name+ '.txt'))
    return info

def create_window(wind,name):
    preset=load_preset(name)
    data=[]
    coor=[0,0]
    size=[10,10]
    prop=[]
    for count in range(0,len(preset)):
        data.append(preset[count].split(" "))
    if data[0][0]=='full' or data[0][1]=='full':
        wind.size=[data[0][0],data[0][1]]
    if data[0][0]!='full':
        wind.size[0]=int(data[0][0])
    if data[0][1]!='full':
        wind.size[1]=int(data[0][1])
    wind.check_size()
    for count in range(1,len(data)):
        if not data[count][0]=='#':
            prop=[]
            ob_class=data[count][0]
            coor[0]=int(data[count][1])
            coor[1]=int(data[count][2])
            size[0]=int(data[count][3])
            size[1]=int(data[count][4])
            interactive_name=data[count][5]
            counter=6
            while data[count][counter]!='\n':
                prop.append(data[count][counter])
                counter+=1
            if ob_class=='button':
                object=ButtonObj(wind.give_table(),coor,size)
                object.dis_text=prop[0]
            elif ob_class=='carrier':
                object=Item(wind.give_table(),coor,size)
                wind.carrier=object
                object.image_name='carrier'
            object.interactive_name=interactive_name
            wind.create(object)
            object.prop=prop[:]
            object.bonded_to=wind
            object.parent=wind
            object.check_size()


def update_buttons(ob1, table, prop):
    if ob1.interactive == True and ob1.interactive_name =='deleteSelfAddObjectButton':
        if prop[1] == 'rufus':
            obj = Item(table, ob1.give_coords(), [300, 400])
            obj.animation_name = 'rufusRake'
            obj.pic_type = [1, 20, 12]
        try:
            remove_menu(ob1.parent.parent,ob1.parent)
            add_object(table, obj)
        except:
            print('Error: obj referenced before assignment')
    if ob1.interactive == True and ob1.interactive_name == 'addWindow':
        wind=WindowObj(table)
        ob1.parent.create(wind)
        wind.parent = ob1.parent
        create_window(wind, ob1. prop[1])
    if ob1.interactive and ob1.interactive_name == 'deleteSelf':
        remove_menu(ob1.parent.parent, ob1.parent)
    if ob1.interactive and ob1.interactive_name == 'setResolution':
        table.screen = pygame.display.set_mode((int(prop[1]), int(prop[2]))) #creating window object




def add_object(table,object):
    table.create(object)

def remove_menu(table,ob1):
    #ob1.bondedTo.exterminate()
    table.destroy(ob1)

def error_message(info):
    print("Wild error appears!")
    print(info)
    sys.exit()
