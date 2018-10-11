#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data=""
    list2.reverse()
    
    for l1 in range(len(list1)):
        for l2 in range(len(list2)):
            temp=""
            if l1==l2:
                if list1[l1] is not None:
                    temp +=list1[l1]
                if list2[l2] is not None:
                    temp+=list2[l2]
                if l1 == len(list1)-1:
                    merged_data+= temp
                else:
                    merged_data+= temp+" "  #write your logic here
    return merged_data

#Provide different values for the variables and test your program
list1=['The', 's', 'ris', 'in', None, 'ea']
list2=['st', 'the', None, 'es', 'un', None]
merged_data=merge_list(list1,list2)
print(merged_data)
