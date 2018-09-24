#PF-Assgn-32
'''
Created on Sep 22, 2018

@author: jatin.pal
'''
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    count1=0
    count2=0
    count3=0
    for i in range(len(patient_medical_speciality_list)):
        if(patient_medical_speciality_list[i]=="P"):
            count1+=1
        if(patient_medical_speciality_list[i]=="O"):
            count2+=1
        if(patient_medical_speciality_list[i]=="E"):
            count3+=1
        if(count1>count2 and count1>count3):
            speciality="Pediatrics"
        elif(count2>count3 and count2>count1):
            speciality="Orthopedics"
        else:
            speciality="ENT"
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'O',302, 'O' ,305, 'O' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)