from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-240, 270)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 18, "normal"))

    def add_point(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 20)
        self.write("Game over", align="center", font=("Courier", 18, "normal"))
        self.goto(0, 0)
        self.write(f"Your final score was {self.level}.", align="center",
                   font=("Courier", 18, "normal"))
        self.goto(0, -20)
        self.write("Click to exit.", align="center",
                   font=("Courier", 18, "normal"))
