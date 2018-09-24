#PF-Assgn-24
'''
Created on Sep 19, 2018

@author: jatin.pal
'''
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    if(num1+num2>num3 and num2+num3>num1 and num1+num3>num2):

    #Write your logic here

    #Use the following messages to return the result wherever necessary
        return success
    else:
        return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
display=form_triangle(num1, num2, num3)
print(display)