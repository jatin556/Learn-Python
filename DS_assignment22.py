#DSA-Assgn-22

#This assignment needs DataSt
#ructures.py file in your package, you can get it from resources page

from src.DataStructures import Stack

def merge_stack(stack1,stack2):
    new_stack=Stack(stack1.get_max_size()+stack2.get_max_size())
    list1=[]
    while not stack1.is_empty():
        list1.append(stack1.pop())
        
    while not stack2.is_empty():
        list1.append(stack2.pop())
        
    list1.sort()
    
    while not new_stack.is_full():
        new_stack.push(list1.pop(0))
        
    return new_stack
    #Remove pass and write your logic here
    

#Pass different values to the function and test your program
stack2=Stack(3)
stack2.push(9)
stack2.push(11)
stack2.push(15)

stack1=Stack(4)
stack1.push(3)
stack1.push(7)
stack1.push(10)
stack1.push(21)

print("The elements in stack1 are:")
stack1.display()
print("The elements in stack2 are:")
stack2.display()
print()
output_stack=merge_stack(stack1, stack2)
print("The elements in the output stack are:")
output_stack.display()
