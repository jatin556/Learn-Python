#PF-Assgn-16
'''
Created on Sep 17, 2018

@author: jatin.pal
'''
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    five_needed=rupees_to_make//5
    one_needed=rupees_to_make%5
    if(rupees_to_make<5):
        five_needed=0
        one_needed=rupees_to_make
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    elif(five_needed<=no_of_five and one_needed<=no_of_one):
        
    
    #Start writing your code here
    #Populate the variables: five_needed and one_needed


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    elif(five_needed>no_of_five and one_needed>no_of_one):
        extra_five=five_needed-no_of_five
        #extra_one=one_needed-no_of_one
        one_needed+=extra_five*5
        five_needed-=extra_five
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
            
    else:    
        print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(105,19,3)