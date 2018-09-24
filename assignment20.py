#PF-Assgn-20
'''
Created on Sep 24, 2018

@author: jatin.pal
'''
def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
#     eligible_loan_amount=0
#     bank_emi_expected=0
    count=0
#     if(loan_amount_expected<= eligible_loan_amount and customer_emi_expected<= bank_emi_expected):
        
        # while (account_number>0):
        #     account_number=account_number//10
        #     count+=1
    if(account_number>=1000 and account_number<2000):
            
        if(account_balance>100000):
                
            if(salary>25000 and loan_type == "Car" and loan_amount_expected<=500000 and customer_emi_expected<=36):
                eligible_loan_amount=500000
                bank_emi_expected=36
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.", eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:",customer_emi_expected)
                
                    
            elif(salary>50000 and loan_type == "House" and loan_amount_expected<=6000000 and customer_emi_expected<=60):
                eligible_loan_amount=6000000
                bank_emi_expected=60
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.", eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:",customer_emi_expected)
#                     print("Requested loan amount:", loan_amount_expected)
#                     print("The customer can avail the amount of Rs.", eligible_loan_amount)
#                     print("Eligible EMIs :", bank_emi_expected)
            elif(salary>75000 and loan_type == "Business" and loan_amount_expected<=7500000 and customer_emi_expected<=84):
                eligible_loan_amount=7500000
                bank_emi_expected=84
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.", eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:",customer_emi_expected)
#                     print("Requested loan amount:", loan_amount_expected)
#                     print("The customer can avail the amount of Rs.", eligible_loan_amount)
#                     print("Eligible EMIs :", bank_emi_expected)
            else:
                print("Invalid loan type or salary")
        else:
            print("Insufficient account balance")
    else:
        print("Invalid account number")
#     else:
#         print("The customer is not eligible for the loan")
    #Start writing your code here
    #Populate the variables: eligible_loan_amount and bank_emi_expected

    #Use the below given print statements to display the output, in case of success
    #
    #
    #
    #
    #

    #Use the below given print statements to display the output, in case of invalid data.
    #
    #
    #
    #
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1005,90000,255000,"Business",7600000,80)