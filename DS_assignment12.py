#DSA-Assgn-12

#This assignment needs DataStructures.py file in your package, you can get it from resources page

#DSA-Assgn-12
from src.DataStructures import Stack

class Ball:
    def __init__(self,color,name):
        self.__color=color
        self.__name=name
        

    def __str__(self):
        return (self.__color+" "+self.__name)

    def get_color(self):
        return self.__color

    def get_name(self):
        return self.__name
class Game:
    def __init__(self,ball_stack):
        self.ball_container=ball_stack
        self.red_balls_container=Stack(4)
        self.green_balls_container=Stack(4)
        self.blue_balls_container=Stack(4)
        self.yellow_balls_container=Stack(4)
        
    def grouping_based_on_color(self):
        while(not(self.ball_container.is_empty())):
            a=self.ball_container.pop()
            if(a.get_color()=="Red"):
                self.red_balls_container.push(a)
            elif(a.get_color()=="Green"):
                self.green_balls_container.push(a)
            
            elif(a.get_color()=="Yellow"):
                self.yellow_balls_container.push(a)  
            
            elif(a.get_color()=="Blue"):
                self.blue_balls_container.push(a)  
       
    def rearrange_balls(self,color):
       
        if(color=="Red"):
            list1=[]
            list2=[]
            while(not(self.red_balls_container.is_empty())):
                a=self.red_balls_container.pop()
                if(a.get_name()=="B"):
                    list1.append(a)
                else:
                    list2.append(a)
            for i in list1:
                self.red_balls_container.push(i)
            for j in list2:
                self.red_balls_container.push(j)
                
        elif(color=="Green"):
            list1=[]
            list2=[]
            while(not(self.green_balls_container.is_empty())):
                a=self.green_balls_container.pop()
                if(a.get_name()=="B"):
                    list1.append(a)
                else:
                    list2.append(a)
            for i in list1:
                self.green_balls_container.push(i)
            for j in list2:
                self.green_balls_container.push(j)
        elif(color=="Blue"):
            list1=[]
            list2=[]
            while(not(self.blue_balls_container.is_empty())):
                a=self.blue_balls_container.pop()
                if(a.get_name()=="B"):
                    list1.append(a)
                else:
                    list2.append(a)
            for i in list1:
                self.blue_balls_container.push(i)
            for j in list2:
                self.blue_balls_container.push(j)
        elif(color=="Yellow"):
            list1=[]
            list2=[]
            while(not(self.yellow_balls_container.is_empty())):
                a=self.yellow_balls_container.pop()
                if(a.get_name()=="B"):
                    list1.append(a)
                else:
                    list2.append(a)
            for i in list1:
                self.yellow_balls_container.push(i)
            for j in list2:
                self.yellow_balls_container.push(j)
            
           


    def display_ball_details(self,color):
        pass
ball1=Ball("Red","A")
ball2=Ball("Blue","B")
ball3=Ball("Yellow","B")
ball4=Ball("Blue","A")
ball5=Ball("Yellow","A")
ball6=Ball("Green","B")
ball7=Ball("Green","A")
ball8=Ball("Red","B")
ball_list=Stack(8)
ball_list.push(ball1)
ball_list.push(ball2)
ball_list.push(ball3)
ball_list.push(ball4)
ball_list.push(ball5)
ball_list.push(ball6)
ball_list.push(ball7)
ball_list.push(ball8)
ball=Game(ball_list)
ball.grouping_based_on_color()
OBJ=Game(ball_list)
OBJ.rearrange_balls("")
#Create objects of Game class, invoke the methods and test the program

#Create objects of Game class, invoke the methods and test the program
