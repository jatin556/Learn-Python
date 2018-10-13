#DSA-Assgn-8

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from src.DataStructures import LinkedList

class BakeHouse:
    def __init__(self):
        self.__occupied_table_list=LinkedList()

    def get_occupied_table_list(self):
        return self.__occupied_table_list

    def allocate_table(self):
        
        temp = self.__occupied_table_list.get_head()
        while temp is not None:
            self.__occupied_table_list.add(temp.get_data())
            temp=temp.get_next()
        return self.__occupied_table_list    
            
    
    def deallocate_table(self,table_number):
        temp = self.__occupied_table_list.get_head()
        while temp is not None:
            self.__occupied_table_list.delete(table_number)
            temp=temp.get_next()
        return   self.__occupied_table_list  
        
        
    
    #Implement other methods here

bakehouse=BakeHouse()
list1=LinkedList()
list1.add(5)
list1.add(10)
bakehouse.allocate_table()
#Invoke the methods of BakeHouse class and test the program
