#OOPR-Assgn-25
class Purchase:
    __counter = 101
    def __init__(self,customer,fruit_name,quantity):
        self.__purchase_id = None
        self.__customer = customer 
        self.__fruit_name = fruit_name
        self.__quantity = quantity 
    def get_purchase_id(self):
        return self.__purchase_id


    def get_customer(self):
        return self.__customer


    def get_quantity(self):
        return self.__quantity

    def calculate_price(self):
        total_price = 0
        total_price1 = 0
        total_price2 = 0
        if FruitInfo.get_fruit_price(self.__fruit_name):
            if self.__fruit_name == "Apple" and self.__quantity > 1:
                total_price = self.get_fruit_price_list() - self.get_fruit_price_list() * 0.02
            elif self.__fruit_name == "Sweet Lime" and self.__quantity >= 5:
                total_price1 = self.get_fruit_price_list() - self.get_fruit_price_list() * 0.05
            elif self.__customer.get_cust_type() == "wholesale":
                if self.__fruit_name == "Apple" and self.__quantity > 1:
                    total_price2 =(self.get_fruit_price_list() - (self.get_fruit_price_list() - self.get_fruit_price_list() * 0.02)*0.1
            else:
                self.__fruit_name == "Sweet Lime" and self.__quantity >= 5:
                total_price1 =self.__fruit_name == "Sweet Lime" and self.__quantity >= 5:
                total_price1 = self.get_fruit_price_list() - (self.get_fruit_price_list() - self.get_fruit_price_list() * 0.05)*0.1
        pass
    
class FruitInfo:
    __fruit_name_list = ["Apple","Guava","Orange","Grape","sweet Lime"]
    __fruit_price_list = [200,80,70,110,60]

    

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitsInfo.__fruit_name_list:
            for i in FruitInfo.__fruit_name_list:
                return FruitInfo.__fruit_price_list[i]
            
        
    
    @staticmethod
    def get_fruit_name_list():
        return Purchase._fruit_name_list
    
    @staticmethod
    def get_fruit_price_list():
        return Purchase._fruit_price_list

    
    
class Customer:
    def __init__(self, customer_name,cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type

    def get_customer_name(self):
        return self.__customer_name


    def get_cust_type(self):
        return self.__cust_type

    
        
    
    
    
    
