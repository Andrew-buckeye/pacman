import pygame
from BFS import AI_movement
from inital_variables import init
from menu import show_start_screen, show_end_screen, show_finish_screen
from keys import check_and_eat_pellet


def AI_play_level(map_level, LEVEL, score, lives, speed):
    TILES = 25
    map_design, PLAYER_SIZE, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, walls_list, pellets_list = init(TILES, map_level)

    pygame.font.init()
    font = pygame.font.SysFont(None, 24)

    # character start position, replcae with P later from map initlization
    x, y = 200, 200

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
    if LEVEL == 1:
        show_start_screen(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT)


    pygame.display.set_caption("P A C M A N")

    running = True
    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((0, 0, 0))
        screen.blit(map_design, (0, 0))

        score_text = font.render(f"Score: {score}   Lives: {lives}   Level: {LEVEL}", True, (255, 0, 0))
        screen.blit(score_text, (10, 5))  # Draw near the top-left

        x, y = AI_movement(x, y, walls_list, pellets_list, PLAYER_SIZE)

        pygame.draw.rect(screen, (255, 0, 0), (x, y, PLAYER_SIZE, PLAYER_SIZE))
        player_rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        score, pellets_list = check_and_eat_pellet(player_rect, pellets_list, score, map_design, TILE_SIZE)

        if len(pellets_list) == 0:
            screen.fill((0, 0, 0))
            text = font.render(f"Beat Level {LEVEL}", True, (0, 255, 0))
            screen.blit(text, ((SCREEN_WIDTH - text.get_width()) // 2, SCREEN_HEIGHT // 2))
            pygame.display.update()
            pygame.time.wait(2000)
            return LEVEL, score, lives

        for pellet in pellets_list:
            pygame.draw.circle(screen, (255, 255, 255), pellet.center, 4)


        pygame.display.update()
