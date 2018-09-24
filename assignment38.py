#PF-Assgn-38
'''
Created on Sep 24, 2018

@author: jatin.pal
'''
# def check_double(number):
#     num1=2*number
#     number=str(number)
#     num1=str(num1)
#     if(len(num1)==len(number)):
#         for i in number:
#             if i in num1:
#                 continue
#             else:
#                 return False
#         return True
#     else:
#         return False
#     
#     
# #Provide different values for number and test your program
# print(check_double(125874))


def check_double(number):
    num=2*number
    a=sorted(str(number))
    b=sorted(str(num))
    if a == b:
        return True
    else:
        return False

#Provide different values for number and test your program
print(check_double(125874))