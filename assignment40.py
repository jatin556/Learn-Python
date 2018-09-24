#PF-Assgn-40
'''
Created on Sep 21, 2018

@author: jatin.pal
'''
def is_palindrome(word):
    word=word.lower()
    if len(word) < 1:
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False
result=is_palindrome("jaaj")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")