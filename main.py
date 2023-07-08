import turtle as t
from player import Player
from scoreboard import Scoreboard
from blocks import Blocks
import time


# Screen set-up
screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")


# Setting up the game parts
screen.tracer(0)
turtle = Player()
screen.listen()
screen.onkeypress(key="Up", fun=turtle.up)
screen.onkeypress(key="Down", fun=turtle.down)
screen.onkeypress(key="Right", fun=turtle.jump_right)
screen.onkeypress(key="Left", fun=turtle.jump_left)
score = Scoreboard()
blocks = Blocks()


# The Game
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    blocks.create_block()
    blocks.move_blocks()

    # If turtle leaves screen
    if turtle.xcor() > 280 or turtle.xcor() < -280 or turtle.ycor() < -290:
        turtle.color("red")
        game_on = False
        screen.update()
        score.game_over()

    # If turtle reaches finish line:
    if turtle.ycor() >= 280:
        screen.tracer(0)
        turtle.restart()
        score.add_point()
        blocks.level_up()

    # If turtle hits block:
    for block in blocks.all_blocks:
        if turtle.distance(block) < 22:
            turtle.color("red")
            block.color("black")
            game_on = False
            screen.update()
            score.game_over()


screen.exitonclick()
