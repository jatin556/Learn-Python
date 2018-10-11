#DSA-Assgn-18

def find_unknown_words(text,vocabulary):
    list1=[]
    list1=text.split(" ")
    list2=[]
    
    
    for i in list1:
        if i not in vocabulary:
            list2.append(i)
        a=set(list2) 
    if len(a)==0:
        return -1
    else:
        return a
    #Remreturn ave pass and write your logic here
    

#Pass different values of text and vocabular
#y to the function and test your program
text="hot"
vocabulary = ['the','the']
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)
