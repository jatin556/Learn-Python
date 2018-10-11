#OOPR-Assgn-19
class Ticket:
    counter = 0
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name = passenger_name
        self.__ticket_id = None
        self.__source = source
        self.__destination = destination

    def get_passenger_name(self):
        return self.__passenger_name


    def get_ticket_id(self):
        return self.__ticket_id


    def get_source(self):
        return self.__source


    def get_destination(self):
        return self.__destination

    def validate_source_destination(self):
        if self.__source == "delhi" or self.__source == "Delhi" or self.__source == "DELHI":
            d=["Mumbai","MUMBAI","mumbai","Kolkata","KOLKATA","kolkata","Pune","PUNE","pune","Chennai","CHENNAI","chennai"]
        
            for i in range(0,len(d)):
                if self.__destination == d[i]:
                    return True
            else:
                return False                
                    
        
#                 return True
        else:
            return False
        
    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter +=1
            if Ticket.counter <10:
                
                self.__ticket_id = self.__source[0]+self.__destination[0]+"0"+str(Ticket.counter)
            else:
                self.__ticket_id = self.__source[0]+self.__destination[0]+str(Ticket.counter)
        else:
            self.__ticket_id = None
        
