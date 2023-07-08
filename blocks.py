from turtle import Turtle
import random


COLORS = ["#FF9707", "#FEAC00", "#012988", "#2362D4", "#FC9A99"]
L_OR_R = [300, -300]
LEN = [0.5, 1, 1.5, 2, 2.5]


class Blocks:

    def __init__(self):
        self.all_blocks = []
        self.block_reserve = []
        self.block_speed = 5

    def create_block(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            if self.block_reserve:
                new_block = self.block_reserve.pop()
            else:
                new_block = Turtle("square")
                new_block.penup()
                new_block.turtlesize(stretch_len=random.choice(LEN))
                new_block.left(180)
                new_block.color(random.choice(COLORS))
            new_block.goto(x=random.choice(L_OR_R), y=random.randint(-250, 250))
            if new_block.xcor() == -300:
                new_block.left(180)
            self.all_blocks.append(new_block)

    def move_blocks(self):
        for block in self.all_blocks:
            block.forward(self.block_speed)
            if block.xcor() < -350 or block.xcor() > 350:
                self.all_blocks.remove(block)
                self.block_reserve.append(block)

    def level_up(self):
        self.block_speed += 2

    def game_over(self):
        for block in self.all_blocks:
            block.color("black")
