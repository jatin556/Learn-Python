#DSA-Assgn-7

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from src.DataStructures import LinkedList

def remove_duplicates(duplicate_list):
    list1=[]
    temp = duplicate_list.get_head()
    while temp is not None:
        list1.append(temp.get_data())
        temp = temp.get_next()
    a=set(list1)
    b=list(a)
    b.sort()
    temp=duplicate_list.get_head()
    while temp is not None:
        duplicate_list.delete(temp.get_data())
        temp=temp.get_next()
        
    for i in b:
        duplicate_list.add(i)
    #write your logic here
    return duplicate_list

#Add different values to the linked list and test your program
duplicate_list=LinkedList()
duplicate_list.add(30)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)

remove_duplicates(duplicate_list)
