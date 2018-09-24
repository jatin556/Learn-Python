#PF-Assgn-31
'''
Created on Sep 22, 2018

@author: jatin.pal
'''
def check_palindrome(word):
   a=word[::-1]
   if(a==word):
       return True  
   else:
       return False

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")