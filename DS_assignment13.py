#DSA-Assgn-13

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from src.DataStructures import Stack
def change_smallest_value(number_stack):
    list1=[]
    while not number_stack.is_empty():
        list1.append(number_stack.pop())
     
    l=min(list1)
    l1=[]
    l2=[]
    for i in list1:
        if i == l:
            l1.append(i)
        else:
            l2.append(i)
#     print(l1)   
#     print(l2)  
    l2.reverse()
           
    m=[]
    m=l1+l2
    for i in m:
        number_stack.push(i)
    #write your logic here

    return number_stack

#Add different values to the stack and test your program
number_stack=Stack(8)
number_stack.push(7)
number_stack.push(8)
number_stack.push(5)
number_stack.push(66)
number_stack.push(5)
print("Initial Stack:")
number_stack.display()
change_smallest_value(number_stack)
print("After the change:")
number_stack.display()

# from src.DS_stack import Stack
# 
# def change_smallest_value(number_stack):
#     list1=[]
#     while not number_stack.is_empty():
#         list1.append(number_stack.pop())
#     
#     l=min(list1)
#     l1=[]
#     l2=[]
#     for i in list1:
#         if i == l:
#             l1.append(i)
#         else:
#             l2.append(i)
#     print(l1)   
#     print(l2)  
#     l2.reverse()
#           
#     m=[]
#     m=l1+l2
#     for i in m:
#         number_stack.push(i)
#     
#     
#     
# 
#     return number_stack
# 
# #Add different values to the stack and test your program
# number_stack=Stack(8)
# number_stack.push(7)
# number_stack.push(8)
# number_stack.push(5)
# number_stack.push(66)
# number_stack.push(5)
# print("Initial Stack:")
# number_stack.display()
# change_smallest_value(number_stack)
# print("After the change:")
# number_stack.display()
