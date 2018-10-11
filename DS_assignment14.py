#DSA-Assgn-14

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from src.DataStructures import Queue

def check_numbers(number_queue):
    solution_queue1=Queue(number_queue.get_max_size())
    list1=[]
    while not number_queue.is_empty():
        list1.append(number_queue.dequeue())
    for i in list1:
        if i%1==0 and i%2==0 and i%3==0 and i%4==0 and i%5==0 and i%6==0 and i%7==0 and i%8==0 and i%9==0 and i%10==0:
            solution_queue1.enqueue(i)
    
    #wri    te your logic here

    return solution_queue1

#Add different values to the queue and test your program
number_queue=Queue(5)
number_queue.enqueue(13983)
number_queue.enqueue(10080)
number_queue.enqueue(7113)
number_queue.enqueue(2520)
number_queue.enqueue(2500)
check_numbers(number_queue)
