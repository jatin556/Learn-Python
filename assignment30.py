'''
Created on Sep 20, 2018

@author: jatin.pal
'''
def encode(message):
    result = ""
    oldL = message[0]
    count = 1
    for i in range(1,len(message)):
        if(message[i] == oldL):
            count +=1
        else:
            result += str(count) + oldL
            oldL = message[i]
            if(i == len(message)-1):result += str(count) + oldL
            #print(oldL)
            count =1
    return result
            

#Provide different values for message and test your program
encoded_message=encode("AABCCA")
print(encoded_message)