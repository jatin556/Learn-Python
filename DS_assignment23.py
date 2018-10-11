#DSA-Tryout
from src.assignment35 import generate_frequency

def generate_cards_per_type(card_type):
    list1=["2","3","4","5","6","7","8","9","J","Q","K","A"]
    list2=["C","D","H","S"]
    list3=[]
    if card_type in list2:
        for i in list1:
            list3+=[card_type+i]
    return list3
#     for i in list1:
#         if card_type is "C":
#             list2+= ["C"+i]
#         elif card_type is "D":
#             list2+= ["D"+i]
#         elif card_type is "H":
#             list2+= ["H"+i] 
#         else:
#             list2+= ["S"+i]
#     return list2
    #Remove pass and write your logic here

def generate_card_deck():
#     list1=["C","D","H","S"]
#     list2=[]
#     for i in list1:
#         list2+=[generate_cards_per_type(i)]
#     print(list2)
#     generate_cards_per_type("C")
    
#     list1.append(generate_cards_per_type("C"))
#     print(list1)
#     d=generate_cards_per_type("D")
#     list1.extend(d)
#     h=generate_cards_per_type("H")
#     list1.extend(h)
#     s=generate_cards_per_type("S")
#     list1.extend(s)
#     print(list1)
    
    #Remove pass and write your logic here
    pass

def shuffle_card_deck(cards_list):
    
    #Remove pass and write your logic here
    pass

def sort_cards_of_each_player(card_list):
    #Remove pass and write your logic here
    pass

def allocate_cards_to_players(cards_list):
    #Remove pass and write your logic here
    pass

def prepare_cards():
    #Remove pass and write your logic here
    pass

first_player=prepare_cards()
print("The first player is:",first_player)
generate_cards_per_type("S")

