#DSA-Assgn-11

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from src.DataStructures import Queue

def merge_queue(queue1,queue2):
    list1=[]
    list2=[]
    merged_queue=Queue(9)
    while not queue1.is_empty():
        list1.append(queue1.dequeue())
    while not queue2.is_empty():
        list2.append(queue2.dequeue())
    if len(list1)<len(list2):
        for i in range(len(list1)):
            merged_queue.enqueue(list1.pop(0))
            merged_queue.enqueue(list2.pop(0))
        for x in list2:
                merged_queue.enqueue(x)
    #write your logic here
        return merged_queue
    
    elif len(list1)>len(list2):
        for i in range(len(list2)):
            merged_queue.enqueue(list1.pop(0))
            merged_queue.enqueue(list2.pop(0))
        for x in list1:
                merged_queue.enqueue(x)
        return merged_queue
    
    else:
        for i in range(len(list2)):
            merged_queue.enqueue(list1.pop(0))
            merged_queue.enqueue(list2.pop(0))
        return merged_queue
        

#Enqueue different values to both the queues and test your program

queue1=Queue(3)
queue2=Queue(6)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')

merged_queue=merge_queue(queue1, queue2)
print("The elements in the merged queue are:")
merged_queue.display()
