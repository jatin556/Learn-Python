#PF-Prac-1
def add_string(str1):
    if len(str1) >= 3:
        if str1.endswith("ing"):
            str1+="ly"
            return str1
        else:
            str1+="ing"
            return str1
    else:
        return str1
  #start writing your code here

  
  

str1="com"
print(add_string(str1))
