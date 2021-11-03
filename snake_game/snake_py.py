import turtle
import time
from Snakee import Snakee
from Food import Food
from Score import Score
head = turtle.Turtle()
s = head.getscreen()
s.setup(600,600)
s.bgcolor("black")
s.title("My snake game")
s.tracer(0)
s.listen()

game_on = True

snake = Snakee(s)
food = Food()
score = Score()
snake.create_snakes()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")
s.onkey(s.bye,"e")


while(game_on):
   s.update()
   time.sleep(0.1)
   snake.move_snake()

   #detect collsion with the food 
   if (snake.head.distance(food) < 15):
      food.refresh()
      score.update()
      snake.grow()
      

   #detect collison with wall
   if (snake.head.xcor()>290 or snake.head.xcor() < -290 or snake.head.ycor()> 290 or snake.head.ycor() < -290):
      score.reset()
      snake.reset()

   #detect collision with tail
   for segment in snake.segments[1:]:
      if(snake.head.distance(segment)< 10):
         score.reset()
         snake.reset()

            

s.exitonclick()