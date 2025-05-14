import pyautogui
import pygame
from map import draw_map
 
'''inatalize the map and get some variables'''
def init(TILES, game_map):
    screen_width, screen_height = pyautogui.size()
    screen_height -= 100 # so it doesn't get in the way of MAC dock bar
    if screen_height > screen_width:
        screen_height = screen_width
    else:
        screen_width = screen_height
# create a surface for the game
    map_design = pygame.Surface((screen_width, screen_height))
    tile_size = screen_width / TILES
    playersize = int(tile_size * 0.8)

    map_design, walls_list, pellets_list = draw_map(game_map, map_design, tile_size)
    return map_design, playersize, tile_size, screen_width, screen_height, walls_list, pellets_list



    