from turtle import Turtle
from paddle import Paddle

Y_CEILING = 390
Y_FLOOR = -390


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("slowest")
        self.goto(0, 0)
        self.x_move = 1
        self.y_move = 1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
#         if a ball bounces: which one gets reduced, and which one stays constant? x stays constant; y changes

    def bounce(self):
        self.y_move *= -1
