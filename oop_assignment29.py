#OOPR-Assgn-29
from abc import ABCMeta, abstractmethod
class Customer(metaclass=ABCMeta):
    def __init__(self,customer_name):
        self.__customer_name = customer_name
        self.bill_amount = None 
        self.bill_id = None
    
    def get_customer_name(self):
        return self.__customer_name
    
    @abstractmethod 
    def calculate_bill_amount(self):
        pass
    
class OccasionalCustomer(Customer):
    __counter = 1000
    def __init__(self,customer_name,distance_in_kms):
        self.__distance_in_kms = distance_in_kms
        super().__init__(customer_name)
        OccasionalCustomer.__counter += 1
        self.bill_id ="O" +str(OccasionalCustomer.__counter)

    def get_distance_in_kms(self):
        return self.__distance_in_kms

    def validate_distance_in_kms(self):
        if 1<= self.__distance_in_kms <= 5:
            return True
        return False
    def calculate_bill_amount(self):
        if self.validate_distance_in_kms():
            if 1<= self.__distance_in_kms <=2:
                self.bill_amount = 50 + self.__distance_in_kms * 5
            elif 2< self.__distance_in_kms <=5:
                self.bill_amount = 50 + self.__distance_in_kms * 7.5
            return self.bill_amount
        self.bill_amount = -1
        return self.bill_amount
    
    
class RegularCustomer(Customer):
    __counter = 100
    def __init__(self,customer_name,no_of_tiffin):
        self.__no_of_tiffin = no_of_tiffin
        super().__init__(customer_name)
        RegularCustomer.__counter += 1 
        self.bill_id ="R" + str(RegularCustomer.__counter) 

    def get_no_of_tiffin(self):
        return self.__no_of_tiffin

    def validate_no_of_tiffin(self):
        if 1<= self.__no_of_tiffin <=7:
            return True
        return False
    def calculate_bill_amount(self):
        if self.validate_no_of_tiffin():
            self.bill_amount = 50 * self.__no_of_tiffin * 7
            return self.bill_amount
        else:
            self.bill_amount = -1
            return self.bill_amount  
        
    
        
        
