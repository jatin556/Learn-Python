#PF-Assgn-34
'''
Created on Sep 20, 2018

@author: jatin.pal
'''
def find_pairs_of_numbers(num_list,n):
    count1=0
    l = []
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):
            sum1=num_list[i]+num_list[j]
            if(sum1==n):
#                 if(num_list[i], num_list[j]) not in l and (num_list[j],num_list[i]) not in l:
                    l.append((num_list[i], num_list[j]))
                    count1+=1
    print(l)
    return count1                    
    

num_list=[3, 4, 1, 8, 5, 9, 0, 6]
n=9
print(find_pairs_of_numbers(num_list,n))