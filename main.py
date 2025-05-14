import pygame
from driver import play_level 
from AI_driver import AI_play_level 


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

level3 = []

# Top wall
level3.append("#" * 25)

# Inner rows
for i in range(1, 24):
    if i == 12:
        # Player starts in the center
        row = "#" * 12 + "P" + " " * 12 + "#"
    elif i in {2, 21}:
        # Edge wall rows with center opening
        row = "#" + "####" + " " * 13 + "####" + "#"
    elif i in {5, 18}:
        # Tighter corridor
        row = "#" + " " * 5 + "#####" + " " * 7 + "#####" + " " * 2 + "#"
    elif i in {8, 16}:
        # Mixed pellets and walls
        row = "#" + "##" + "." * 7 + "####" + "." * 7 + "##" + "#"
    elif i in {10, 14}:
        # Pellet corridors
        row = "#" + "." * 23 + "#"
    else:
        # Mostly open space
        row = "#" + " " * 23 + "#"
    level3.append(row)

# Bottom wall
level3.append("#" * 25)


# List of levels
levels = [level1, levle2, level3]

# Main game loop
def main():
    SCORE = 0
    LIVES = 3
    SPEED = 5
    LEVEL_NUM = 1

    for i, level in enumerate(levels):
        level_status = 'END' if i == len(levels) - 1 else LEVEL_NUM
        LEVEL_NUM, SCORE, LIVES = AI_play_level(level, level_status, SCORE, LIVES, SPEED) #change here for AI or manual
    pygame.quit()

if __name__ == "__main__":
    main()