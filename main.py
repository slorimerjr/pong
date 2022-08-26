from turtle import Screen
from paddle import Paddle
# import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

paddle_1 = Paddle()

screen.listen()

screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    # time.sleep(0.01)




screen.exitonclick()

