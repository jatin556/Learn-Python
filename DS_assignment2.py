#DSA-Assgn-2
# from builtins import None

class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))
    
class Service:
    def __init__(self,car_list):
        self.__car_list = car_list

    def get_car_list(self):
        return self.__car_list

    def find_cars_by_year(self,year):
        temp=[]
        for i in range(len(self.__car_list)):
            if self.__car_list[i].get_year() == year:
                temp.append(self.__car_list[i].get_model())
        if temp == []:
            return None
        else:
            return temp
        
        
        
    
    def add_cars(self,new_car_list):
        self.__car_list.extend(new_car_list)
        print(self.__car_list[6].get_model())
        
        
        for i in range(0,len(self.__car_list)-1):
            for j in range(i+1,len(self.__car_list)):
                if self.__car_list[i].get_year() > self.__car_list[j].get_year():
                    temp = self.__car_list[i]
                    self.__car_list[i]=self.__car_list[j]
                    self.__car_list[j]=temp
#         return self.get_car_list()
        
    
    def remove_cars_from_karnataka(self):
        ka=[]
        for i in self.__car_list:
            if not (i.get_registration_number().startswith("KA")):
                ka.append(i)
        self.__car_list=ka  
#             if self.__car_list[i].get_registration_number().startswith("KA"):
#                 ka += self.__car_list[i]
#         for k in range(len(self.__car_list)):
#             for j in range(len(ka)):
#                 if self.__car_list[k].get_registration_number() == ka[j].get_registration_number():
#                     self.__car_list.remove(self.__car_list[k])
#         for i in self.__car_list:
#             if i.get_registration_number() == self.get_registration_number.startswith("KA"):
#                 self.__car_list[i].get_registration_number().pop(i)
    

#Implement Service class here

car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]
service=Service(car_list)
service.find_cars_by_year(2013)
car6=Car("BMW",2010,"KA09 3058")
car7=Car("Audi", 2011, "MH10 6777")
car8=Car("Swift", 2013,"KA12 9096")
car9=Car("Porch",2013,"GJ01 7855")
car10=Car("Baleno",2014,"KL07 4334")
new_car_list=[car6,car7,car8,car9,car10]
service.add_cars(new_car_list)

#Create object of Service class, invoke the methods and test your program
