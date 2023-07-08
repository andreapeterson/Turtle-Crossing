from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("ForestGreen")
        self.goto(0, -280)
        self.left(90)

    def up(self):
        self.forward(15)

    def down(self):
        self.backward(15)

    def jump_right(self):
        self.setx(self.xcor()+15)

    def jump_left(self):
        self.setx(self.xcor()-15)

    def restart(self):
        self.goto(0, -280)
