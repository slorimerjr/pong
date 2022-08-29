from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        # paddle size is wid=100, len=20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        paddle = self
        new_y = paddle.ycor() + 20
        paddle.goto(paddle.xcor(), new_y)

    def down(self):
        paddle = self
        new_y = paddle.ycor() - 20
        paddle.goto(paddle.xcor(), new_y)




