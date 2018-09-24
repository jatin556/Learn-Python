#PF-Assgn-41
'''
Created on Sep 24, 2018

@author: jatin.pal
'''

def find_ten_substring(num_str):
    result = []
    for i in range(0, len(num_str)):
        j = i
        sum = 0
        while sum < 10 and  j < len(num_str):
            sum += int(num_str[j])
            j += 1
             
        if sum == 10:
            k = j + 1
            if(k < len(num_str) and num_str[k] == 0): j += 1
            result.append(num_str[i: j])
    return result


num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)