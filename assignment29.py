#PF-Assgn-29
'''
Created on Sep 20, 2018

@author: jatin.pal
'''
def calculate(distance,no_of_passengers):
    total_ticket_price=no_of_passengers*80
    print(total_ticket_price)
    petrol_required=distance/10
    print(petrol_required)
    petrol_price=petrol_required*70
    print(petrol_price)
    profit=total_ticket_price-petrol_price
    if(profit>0):
        return profit
    else:
        return -1



#Provide different values for distance, no_of_passenger and test your program
distance=100
no_of_passengers=1
print(calculate(distance,no_of_passengers))