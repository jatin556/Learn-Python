#OOPR-Assgn-9
class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
        self.__course_id=None
        self.__fees=None

    def get_course_id(self):
        return self.__course_id


    def get_fees(self):
        return self.__fees


    def get_student_id(self):
        return self.__student_id


    def get_marks(self):
        return self.__marks


    def get_age(self):
        return self.__age


    def set_student_id(self, student_id):
        self.__student_id = student_id


    def set_marks(self, marks):
        self.__marks = marks


    def set_age(self, age):
        self.__age = age
        
    
    def validate_marks(self):
        if self.__marks >= 0 and self.__marks <=100:
            return True
        else:
            return False
        
    def validate_age(self):
        if self.__age > 20:
            return True
        else:
            return False
        
    def check_qualification(self):
        if self.validate_age() == True and self.validate_marks() == True:
            if self.__marks >= 65:
                return True
            else:
                return False
        else:
            return False
        
    def choose_course(self,course_id):
        discount = 25/100
        if course_id == 1001:
            self.__course_id = course_id
            if self.__marks > 85:
                self.__fees= 25575 -25575 * discount
                    
            else:
                self.__fees= 25575
            return True
        elif course_id == 1002:
            self.__course_id = course_id
            if self.__marks > 85:
                self.__fees= 15500 -15500 * discount
            else:
                self.__fees= 15500
            return True
        else:
            return False    
        
    
                
                    
                    
                
            
        
                      
                
                
            
        
        
stud1=Student()
stud1.set_age(23)
stud1.set_marks(67)
stud1.check_qualification()
stud1.choose_course(1001)
