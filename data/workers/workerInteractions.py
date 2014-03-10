from data.classes.objects.item import *

'''
0-Noting
1-Order
2-Chaos
3-Time
'''

def is_pressed_and_released(ob1,ob2):
    if ob1.if_crosses(ob2):
        if pygame.mouse.get_pressed()[0]:
            print('cross ',ob1.interactiveName, ob2.interactiveName)
            return True
    return False
''' if ob1.interaction_state==0:

        if ob1.if_crosses(ob2) and not pygame.mouse.get_pressed()[0]:

            ob1.interaction_state=1
    if ob1.interaction_state==1:
        print('in')
        if not ob1.if_crosses(ob2):
             ob1.interaction_state = 0
        if pygame.mouse.get_pressed()[0]:
            print(2)
            ob1.interaction_state = 2
    if ob1.interaction_state==2:
        print('cross ',ob1.interactiveName, ob2.interactiveName)
        return True
        if not ob1.if_crosses(ob2):
             ob1.interaction_state = 0
    return False'''


def update_interactions(object_list,table):
    for ob1 in object_list:
        if ob1.interactive==True and not ob1.interactive_name==0:
            for ob2 in object_list:
                if ob2.interactive==True and not ob1.interactive_name==ob2.interactive_name and not ob2.interactive_name==0:
                    if is_pressed_and_released(ob1, ob2):
                        two_to_one(ob1,ob2,table)

def replace_two_with_one(ob1,ob2,result,int_num,name,table):
    result.interactive_number=int_num
    result.image_name=name
    result.coords=ob1.coords
    table.destroy(ob1)
    table.destroy(ob2)
    table.create(result)

def two_to_one(ob1,ob2, table):
    if ob1.interactive_name=='order' and ob2.interactive_name=='chaos':
        print('IN ' +ob1.interactive_name, ob2.interactive_name)
        result=Item(table)
        replace_two_with_one(ob1,ob2,result,'time','Time',table)
        
