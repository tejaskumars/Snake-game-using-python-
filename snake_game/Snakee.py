import turtle
import time 
positions = [(0,0),(-20,0),(-40,0)]
distance = 20
up = 90
down = 270
left = 180
right = 0
class Snakee:
    def __init__(self,s):
        self.s = s
        self.segments = []

    def create_snakes(self):
        for (i,j) in positions:
            self.add_segment((i,j))
            

    def move_snake(self):
            for seg_num in range(len(self.segments)-1,0,-1):
                new_x = self.segments[seg_num-1].xcor()
                new_y = self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(new_x,new_y)
            self.segments[0].forward(distance)

    def up(self):
        if (self.head.heading() != down):
            self.head.setheading(up)
    def down(self):
        if (self.head.heading() != up):
            self.head.setheading(down)
    def left(self):
        if (self.head.heading() != right):
            self.head.setheading(left)
    def right(self):
        if (self.head.heading() != left):
            self.head.setheading(right)

    def add_segment(self,position):
        new_square = turtle.Turtle()
        new_square.shape("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.segments.append(new_square)
        self.head = self.segments[0]

    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snakes()
        self.head = self.segments[0]
    
    
        

    def grow(self):
        self.add_segment(self.segments[-1].position())
