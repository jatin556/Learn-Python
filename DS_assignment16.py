#DSA-Assgn-16

#This assignment needs DataStru
#ctures.py file in your package, you can get it from resources page

from src.DataStructures import Stack,Queue

def separate_boxes(box_stack):
    new_queue=Queue(box_stack.get_max_size())
    list1=[]
    while not box_stack.is_empty():
        i=box_stack.pop()
        if i in ["Red","Green","Blue"]:
            list1.append(i)
        else:
            new_queue.enqueue(i)    
    list1.reverse()
    for i in list1:
        box_stack.push(i)
    return new_queue    
    
#     print(list1)
#     list2=[]
#     for i in range(0,len(list1)):
#         if list1[i]=="Red" or list1[i]=="Green" or list1[i]=="Blue":
#             list2.append(list1.pop(i))
#             
#     print(list2)
#     print(list1)
#     box_stack.push()
    #Remove pass and write your logic here
    

#Use different values for stack and test your program
box_stack=Stack(8)
box_stack.push("Red")
box_stack.push("Magenta")
box_stack.push("Yellow")
box_stack.push("Red")
box_stack.push("Orange")
box_stack.push("Green")
box_stack.push("White")
box_stack.push("Purple")
print("Boxes in the stack:")
box_stack.display()
result=separate_boxes(box_stack)
print()
print("Boxes in the stack after modification:")
box_stack.display()
print("Boxes in the queue:")
result.display()
