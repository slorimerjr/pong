from turtle import Turtle
STARTING_POSITIONS = [(350, 0), (-350, 0)]
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.shapesize(stretch_wid=5, stretch_len=1)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def down(self):
        paddle = self.segments[0]
        new_y = paddle.ycor() - 20
        paddle.goto(paddle.xcor(), new_y)

    def up(self):
        paddle = self.segments[0]
        new_y = paddle.ycor() + 20
        paddle.goto(paddle.xcor(), new_y)

