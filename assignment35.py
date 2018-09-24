#PF-Assgn-35
'''
Created on Sep 22, 2018

@author: jatin.pal
'''
#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    global list_of_marks
    count1=0
    l=[]
    sum1=0
    # print(l)
    for i in range(len(list_of_marks)):
        #print(i)
        sum1=sum1+list_of_marks[i]
        a=sum1/len(list_of_marks)
    
    for j in range(len(list_of_marks)):    
        if(list_of_marks[j]>a):
            l+=[list_of_marks[i]]
            count1+=1
            #print(count1)
    avg=float(count1*10)
    return avg

def sort_marks():
    return sorted(list_of_marks)
    

def generate_frequency():
    global list_of_marks
    l=[]
    for i in range(0,26):
        count=0
        for j in list_of_marks:
            if i==j: 
                count+=1
        l+=[count] 
    return l    

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())