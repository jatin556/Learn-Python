#PF-Assgn-36
'''
Created on Sep 24, 2018

@author: jatin.pal
'''
def create_largest_number(number_list):
    str1=""
    # for i in range(len(number_list)):
    #     for j in range(i+1,len(number_list)):
    #         if(number_list[i]>number_list[j]):
    #             temp=number_list[i]
    #             number_list[i]=number_list[j]
    #             number_list[j]=temp
    num=sorted(number_list,reverse=True)
    for i in num:
        str1+=str(i)
    return int (str1)    
        
    
        
               
number_list=[93,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)