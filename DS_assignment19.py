#DSA-Assgn-19
def last_instance( num_list,  start,  end,  key):
    count=0
    if key not in num_list:
        return -1
    else:
        for i in range(len(num_list)):
            if key==num_list[i]:
                count+=1
        for i in range(len(num_list)):
            if key==num_list[i]:
                return i+count-1 
            
    
    #Remove pass and write your logic here
    

num_list=[1,1,2,2,3,4,5,5,5,5]
start=0
end=len(num_list)-1
key=6 #Number to be searched
#Pass different values for num_list, start,end and key and test your program
result=last_instance(num_list, start,end,key)

if(result!=-1):
    print("The index position of the last occurrence of the number:",result)
else:
    print("Number not found")
