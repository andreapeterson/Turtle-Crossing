# Turtle-Crossing
Written in Python (OOP and class inheritance), the objective of the game is to get the turtle across the screen without hitting any blocks. Each time you make it across, your level increases by 1 and the blocks also increase speed. Special features include different-sized blocks approaching from both sides of the screen, when you lose the turtle turns red from either going out of bounds or the block that hits you turns black, the turtle can move in all four directions with arrow clicks on your keyboard, the score is kept, and a color palette of my choice(feel free to customize in blocks.py). Additionally, to fix the bug of too many blocks clogging the loop, I added a system in blocks.py so that the blocks that go off-screen are added to a list to be reused. 
Also, to fix the issue of once you get to a higher level there are fewer blocks(blocks are moving faster and get across fast but don't spawn as quickly), I added a timer variable and passed that through time.sleep() so each time you cross the finish line the timer variable decreases so the pause for spawning is less. Please let me know if you find any other bugs!


![turtlecross](https://github.com/andreapeterson/Turtle-Crossing/assets/134665743/8408379c-3622-41e0-9dd2-c8b2b66138c8)
