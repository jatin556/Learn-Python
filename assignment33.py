#PF-Assgn-33
'''
Created on Sep 22, 2018

@author: jatin.pal
'''
def find_common_characters(msg1,msg2):
    str1=""
    for i in range(len(msg1)):
        #for j in range(len(msg2)):
            if(msg1[i]==" "):
                pass
            elif(msg1[i] in msg2):
                    str1+=(msg1[i])
    if str1=="":
        return -1
    else:
        return str1
            # else:
            #     return -1
                
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)