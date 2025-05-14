import pygame
from driver import play_level 

level1 = []
level1.append("#" * 25),
for _ in range(1, 12):
    level1.append("#" + " " * 23 + "#"),
level1.append("#" + "." * 11 + "P" + "." * 11 + "#")
for _ in range(13, 24):
    level1.append("#" + " " * 23 + "#")
level1.append("#" * 25)

levle2 = []
# Top wall
levle2.append("#" * 25)
# Inner rows
for i in range(1, 24):
    if i == 12:
        # Player start row
        row = "#" * 12 + "P" + " " * 12 + "#"
    elif i in {4, 8, 16, 20}:
        # Internal walls with large gaps
        row = "#" + "####" + " " * 13 + "####" + "#"
    elif i in {6}:
        # Narrower central obstacles
        row = "#" + " " * 10 + "###" + "." * 11 + "#"
    else:
        # Open rows with pellets
        row = "#" + " " * 23 + "#"
    levle2.append(row)
# Bottom wall
levle2.append("#" * 25)

while True:
    kill = True
    LEVEL = 1
    SCORE = 0
    LIVES = 3
    SPEED = 5
    while kill:
        LEVEL, score, lives = play_level(level1, LEVEL, SCORE, LIVES, SPEED)
        LEVEL = 'END'
        LEVEL, score, lives = play_level(levle2, LEVEL, SCORE, LIVES, SPEED)
        kill = False
        
