#PF-Assgn-37

#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    return sum(chocolates_received)

def reward_child(child_id_rewarded,extra_chocolates):
    if extra_chocolates<1:
        print("Extra chocolates is less than 1")
    else:    
        if child_id_rewarded not in child_id:
            print("Child id is invalid")
        else:
            for i in range(len(child_id)):
                if child_id[i]== child_id_rewarded:
                    chocolates_received[i]+=extra_chocolates
                    print(chocolates_received)            
                


print(calculate_total_chocolates())
#Test your code by passing different 
#values for child_id_rewarded,extra_chocolates
reward_child(20,0)