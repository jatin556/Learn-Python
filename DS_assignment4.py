#DSA-Assgn-4

class Player:
    def __init__(self,name,experience):
        self.__name=name
        self.__experience=experience
        
    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return(self.__name+" "+(str)(self.__experience))
        
class Game:
    def __init__(self,players_list):
        self.__players_list = players_list
        
    def sort_players_based_on_experience(self):
        for i in range(len(self.__players_list)):
            for j in range(len(self.__players_list)):
                if self.__pslayers_list[i].get_experience() > self.__players_list[j].get_experience():
                    self.__players_list[i],self.__players_list[j] = self.__players_list[j],self.__players_list[i]
                    
                     
    
    def shift_player_to_new_position (self,old_index_position, new_index_position):
        element=self.__players_list.pop(old_index_position)
        self.__players_list.insert(new_index_position,element)
         
#temp= self.__players_list[old_index_position]
#         self.__players_list[old_index_position]= self.__players_list[new_index_position]
#         self.__players_list[new_index_position]=temp
#         self.__players_list.insert(new_index_position,self.__players_list[old_index_position])
            
    
    def display_player_details(self):
        for i in self.__players_list:
            print(i.get_name," ",i.get_experience())
        
            

#Implement Game class here

player1=Player("Dhoni",15)
player2=Player("Virat",10)
player3=Player("Rohit",12)
player4=Player("Raina",11)
player5=Player("Jadeja",13)
player6=Player("Ishant",9)
player7=Player("Shikhar",8)
player8=Player("Axar",7.5)
player9=Player("Ashwin",6)
player10=Player("Stuart",7)
player11=Player("Bhuvneshwar",5)
#Add different values to the list and test the program
players_list=[player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]
print(player1)
game=Game(players_list)
game.sort_players_based_on_experience()
game.shift_player_to_new_position(0, 4)