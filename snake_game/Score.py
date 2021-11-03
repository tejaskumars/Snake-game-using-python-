from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",15,"italic")
FONT1 = ("Arial",10,"italic")
class Score(Turtle):

    file = open("score.txt", mode="r")
    
    def __init__(self):
        super().__init__()
        self.counter = -1
        self.hideturtle()
        self.highscore = self.file.read()
        self.file.close()
        self.penup()
        self.color("white")
        self.goto(0,-275)
        self.update()

    def update(self):
        self.goto(0,275)
        self.counter+=1
        self.clear()
        self.write("score : {x} high score : {y}".format(x =self.counter , y = self.highscore),move=False,align=ALIGNMENT,font=FONT)
        self.goto(0,-280)
        self.write("PRESS e to exit",move=False,align=ALIGNMENT,font=FONT1)


 
    def reset(self):
        if (self.counter > int(self.highscore)):
            file = open("score.txt", mode="w")
            self.highscore = self.counter
            x = str(self.highscore)
            file.write(x)
            file.close()
        self.counter = -1
        self.update()
        
   

    
