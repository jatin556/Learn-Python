#PF-Assgn-28
'''
Created on Sep 19, 2018

@author: jatin.pal
'''
def find_max(num1, num2):
    max_num=-1
    if(num1<num2):
        if(num1>=100 and num2>=100):
            max_num=-1
        else:    
            for i in range(num1,num2+1):
                sum1=0
                temp=i
                while(i>0):
                    rem=i%10
                    sum1=sum1+rem
                    i=i//10
                if(sum1%3==0 and temp%5==0):
                        max_num=temp
    else:
        max_num=-1
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(3,9)
print(max_num)