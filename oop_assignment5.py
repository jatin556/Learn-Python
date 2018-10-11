#OOPR-Assgn-5
'''
Created on Sep 27, 2018

@author: jatin.pal
'''

class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None

    def get_premium_amount(self):
        return self.__premium_amount

    def set_premium_amount(self, premium_amount):
        self.__premium_amount = premium_amount
        
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
        
    def get_vehicle_id(self):
        return self.__vehicle_id
    
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
        
    def get_vehicle_type(self):
        return self.__vehicle_type
    
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
        
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    
#     def set_premium_amount(self,premium_amount):
#         self.__premium_amount=premium_amount
#         
#     def get_premium_amount(self):
#         return self.premium_amount()
    
    def calculate_premium(self):
        if self.__vehicle_type == "Two Wheeler":
            self.__premium_amount = self.__vehicle_cost * 0.02
            
        elif self.__vehicle_type =="Four Wheeler":
            self.__premium_amount = self.__vehicle_cost * 0.06
        
                   
    def display_vehicle_details(self):
        
        print("vehicle type:" ,self.get_vehicle_type()  , 
              "vehicle   id:" ,self.get_vehicle_id() , 
              "vehicle_cost:" , self.get_vehicle_cost() , 
              "premium amount:",self.__premium_amount)
        
        
        
v1=Vehicle()
v2=Vehicle()
v1.display_vehicle_details()
                       