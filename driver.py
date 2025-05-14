import pygame
from keys import handle_movement, check_and_eat_pellet
from map import draw_map
from inital_variables import init
from menu import show_start_screen, show_end_screen, show_finish_screen


def play_level(map_level, LEVEL, score, lives, speed):
    TILES = 25
    map_design, PLAYER_SIZE, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, walls_list, pellets_list = init(TILES, map_level)

    pygame.font.init()
    font = pygame.font.SysFont(None, 24)

    # character start position, replcae with P later from map initlization
    x, y = 200, 200

    ###### Pygame code starts here ######
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
    if LEVEL == 1:
        show_start_screen(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Put them here for coloring
    # screen.fill((0, 0, 0))
    # screen.blit(map_design, (0, 0))

    pygame.display.set_caption("P A C M A N")

    running = True
    while running:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((0, 0, 0))
        screen.blit(map_design, (0, 0))

        score_text = font.render(f"Score: {score}   Lives: {lives}   Level: {LEVEL}", True, (255, 0, 0))
        screen.blit(score_text, (10, 5))  # Draw near the top-left

        keys = pygame.key.get_pressed()
        x, y = handle_movement(keys, x, y, speed, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SIZE, PLAYER_SIZE, walls_list)

        if len(pellets_list) == 0:
            if LEVEL == 'END':
                show_finish_screen(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, LEVEL)
                return LEVEL, score, lives
            show_end_screen(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, LEVEL)
            LEVEL += 1
            return LEVEL, score, lives

        for pellet in pellets_list:
            pygame.draw.circle(screen, (255, 255, 255), pellet.center, 4)

        # player
        pygame.draw.rect(screen, (255, 0, 0), (x, y, PLAYER_SIZE, PLAYER_SIZE))
        player_rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        score, pellets_list = check_and_eat_pellet(player_rect, pellets_list, score, map_design, TILE_SIZE)

        pygame.display.update()
