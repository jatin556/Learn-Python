#OOPR-Assgn-12
class Bill:
    def __init__(self,bill_id,patient_name):
        self.__bill_id = bill_id
        self.__patient_name = patient_name
        self.__bill_amount = None

    def get_bill_id(self):
        return self.__bill_id


    def get_patient_name(self):
        return self.__patient_name


    def get_bill_amount(self):
        return self.__bill_amount

    def calculate_bill_amount(self,consultation_fees, quantity_list, price_list):
        total_bill_amount = 0
        for i in range(0,len(quantity_list)):
            for j in range(0,len(price_list)):
                if i == j:
                    total_bill_amount += quantity_list[i] * price_list[j]
        total_bill_amount += consultation_fees
        self.__bill_amount = total_bill_amount 
