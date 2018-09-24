#PF-Assgn-16
'''
Created on Sep 17, 2018

@author: jatin.pal
'''
def make_amount(rupees_to_make,no_of_five,no_of_one):
   five_needed = rupees_to_make // 5
   rem_amt = 0
   if(five_needed > no_of_five):rem_amt = rupees_to_make - no_of_five * 5
   one_req = rem_amt
   if(one_req > no_of_one):
       print(-1)
    print("No. of 1 coins:" , five_needed)
    
    
       
    
    

    #Start writing your code here
    #Populate the variables: five_needed and one_needed


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("No. of Five needed :", five_needed)
    #print("No. of One needed  :", one_needed)
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)