#PF-Assgn-48

def find_correct(word_dict):
    correct = 0
    almost_correct = 0
    wrong = 0
    for key, value in word_dict.items():
        if(len(key) != len(value)): wrong += 1
        else:
            if(key == value): correct += 1
            else:
                diff = 0
                for i in range(len(key)):
                    if(key[i] != value[i]): diff += 1
                if diff <= 2: almost_correct += 1
                else: wrong += 1
    return [correct, almost_correct, wrong]
            
        

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))