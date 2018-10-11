#OOPR-Assgn-24
class Apparel:
    counter = 100
    def __init__(self,price,item_type):
        self.__item_id = None
        self.__price = price
        self.__item_type = item_type
        Apparel.counter += 1
        if self.__item_type == "Cotton":
            self.__item_id = "C" + str(Apparel.counter)
        else:
            self.__item_type = "Silk"
            self.__item_id = "S" + str(Apparel.counter)

    
    def get_item_id(self):
        return self.__item_id


    def get_price(self):
        return self.__price


    def get_item_type(self):
        return self.__item_type


    def set_price(self, price):
        self.__price = price
        
    
    def calculate_price(self):
#         prc = 0.05 * self.__price
        self.__price += self.__price * 0.05
        return self.__price
        
class Cotton(Apparel):
    def __init__(self,price,discount):
        self.__discount = discount
        super().__init__(price, "Cotton")

    def get_discount(self):
        return self.__discount
    
    def calculate_price(self):
        super().calculate_price()
        total_price= self.get_price()-(self.get_price()*self.__discount/100)
        total_price =total_price * 1.05
        self.set_price(total_price)
class Silk(Apparel):
    def __init__(self,price):
        self.__points = None
        super().__init__(price, "Silk")

    def get_points(self):
        return self.__points

    def calculate_price(self):
        super().calculate_price()
        if self.get_price() > 10000:
            self.__points = 10
        else:
            self.__points = 3
        compute_price = self.get_price() * 0.1 + self.get_price()
        self.set_price(compute_price)
        
        
    
        
        

  
        
    
        
