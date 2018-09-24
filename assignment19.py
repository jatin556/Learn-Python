#PF-Assgn-19
'''
Created on Sep 17, 2018

@author: jatin.pal
'''
def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    cost_of_veg=120
    cost_of_non_veg=150
    if(quantity_ordered==0):
        bill_amount=-1
    elif(quantity_ordered!=0):
        if(food_type=="v" or food_type=="n"):
            bill_amount=-1
        elif(food_type=="N"):
            if(distance_in_kms>0 and distance_in_kms<=3):
                bill_amount=quantity_ordered*cost_of_non_veg
            elif(distance_in_kms>3 and distance_in_kms<=6):
                    bill_amount=(quantity_ordered*cost_of_non_veg+3*
                                 (distance_in_kms-3))
            elif(distance_in_kms>6):
                    bill_amount=(quantity_ordered*cost_of_non_veg+9+ 
                                 6*(distance_in_kms-6))
            else:
                    bill_amount=-1
        else:
            bill_amount=-1
    if(quantity_ordered==0):
        bill_amount=-1  
    elif(quantity_ordered!=0): 
        if(food_type=="v" or food_type=="n"):
            bill_amount=-1
        elif(food_type=="V"):
            if(distance_in_kms>0 and distance_in_kms<=3):
                bill_amount=quantity_ordered*cost_of_veg
            elif(distance_in_kms>3 and distance_in_kms<=6):
                bill_amount=quantity_ordered*cost_of_veg+3*(distance_in_kms-3)
            elif(distance_in_kms>6):
                bill_amount= (quantity_ordered*cost_of_veg+9+6 
                              *(distance_in_kms-6))
            else:
                bill_amount=-1    
    #write your logic here
    return bill_amount

#Provide different values for food_type,quantity_ordered,
#distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,8)
print(bill_amount)