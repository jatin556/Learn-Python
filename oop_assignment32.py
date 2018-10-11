#OOPR-Assgn-32
from abc import ABCMeta, abstractmethod
class Employee(metaclass=ABCMeta):
    def __init__(self,job_band,employee_name,basic_salary,qualification):
        self.__job_band = job_band
        self.__employee_name = employee_name
        self.__basic_salary = basic_salary
        self.__qualification = qualification

    def get_job_band(self):
        return self.__job_band


    def get_employee_name(self):
        return self.__employee_name


    def get_basic_salary(self):
        return self.__basic_salary


    def get_qualification(self):
        return self.__qualification
    
    @abstractmethod 
    def validate_job_band(self):
        pass
    
    def validate_basic_salary(self):
        if self.__basic_salary > 3000:
            return True
        return False
    
    def validate_qualification(self):
        pass
    
    @abstractmethod 
    def calculate_gross_salary(self):
        pass
    
    
class Graduate(Employee):
    def __init__(self,job_band,employee_name,basic_salary,qualification,cgpa):
        super().__init__(job_band, employee_name, basic_salary, qualification)
        self.__cgpa = cgpa

    def get_cgpa(self):
        return self.__cgpa

    def validate_job_band(self):
        pass
    
    def calculate_gross_salary(self):
        pass
    
    
class Lateral(Employee):
    def __init__(self,job_band,employee_name,basic_salary,qualification,skill_set):
        super().__init__(job_band, employee_name, basic_salary, qualification)
        self.__skill_set = skill_set

    def get_skill_set(self):
        return self.__skill_set
        
    def validate_job_band(self):
        pass
    
    def calculate_gross_salary(self):
        pass
    
        

    
        
    
