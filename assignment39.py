#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,250,3]

'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    for i in range(0, len(item_tuple), 2):
        item = item_tuple[i]
        quantity = item_tuple[i+1]
        if item not in menu:
            print(item + " is not available")
        else:
            if check_quantity_available(menu.index(item), quantity):
                print(item + " is  available")
            else:
                print(item + " stock is  over")


    #Populate the item name in the below given print statements
    #Use it to display the output wherever applicable
    #Also, do not modify the text in it for verification to work
    
    #print("<item name>is not available")
    #print("<item name>stock is over")
            
    
  


'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
    if(quantity_available[index] >= quantity_requested):
        quantity_available[index] -= quantity_requested
        return True
    return False
    #Remove pass and write your logic here to return an appropriate boolean value.


#Provide different values for items ordered and test your program
place_order("Veg Roll",2,"Noodles",2)
place_order("Soup",1,"Veg Roll", 2, "Fried Rice",1)
