#PF-Assgn-44
'''
Created on Sep 24, 2018

@author: jatin.pal
'''


def find_duplicates(list_of_numbers):
    return [x for x in set(list_of_numbers) if list_of_numbers.count(x) > 1]

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)