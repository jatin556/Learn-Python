#OOPR-Assgn-3
class Customer:
    def __init__(self,customer_name,bill_amount):
        self.customer_name=customer_name
        self.bill_amount=bill_amount
        
        
    def purchases(self):
        self.bill_amount -= self.bill_amount * 5/100
        self.pays_bill(self.bill_amount)
        
        
    def pays_bill(self,amount):
        print("customer name :"+ self.customer_name + " pays bill :", self.bill_amount)
        
# cust1=Customer("A", 2500)
# cust2=Customer("B",1289)
# cust3=Customer("C",3260)
# cust4=Customer("D",6543)
# cust1.purchases()
# cust2.purchases()
# cust3.purchases()
# cust4.purchases()