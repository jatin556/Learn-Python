#PF-Assgn-33

def find_common_characters(msg1,msg2):
    #Remove pass and write your logic here
    string1=""
    
    for i in range(len(msg1)):
        if(msg1[i]==" "):
            pass
        elif msg1[i] in msg2:
            string1+=msg1[i]
            #msg1=msg1.replace("msg[i]","")
            
            
    if(string1==""):
        return -1
    else:       
        return string1         

#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="jklp"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)