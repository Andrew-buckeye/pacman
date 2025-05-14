import pygame
'''Screens before, between, and after levels'''
def show_start_screen(screen, font, screen_width, screen_height):
    waiting = True
    title_font = pygame.font.SysFont(None, 48)
    prompt_font = pygame.font.SysFont(None, 24)
    while waiting:
        screen.fill((0, 0, 0))  # Black background

        title_text = title_font.render("PACMAN", True, (0, 255, 0))
        prompt_text = prompt_font.render("Press SPACE to Start", True, (255, 255, 255))

        # Center the text
        screen.blit(title_text, ((screen_width - title_text.get_width()) // 2, screen_height // 3))
        screen.blit(prompt_text, ((screen_width - prompt_text.get_width()) // 2, screen_height // 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

def show_end_screen(screen, font, screen_width, screen_height, level):
    title_font = pygame.font.SysFont(None, 48)
    prompt_font = pygame.font.SysFont(None, 24)
    waiting = True
    while waiting:
        screen.fill((0, 0, 0))  # Black background

        title_text = title_font.render(f"Beat Level {level}", True, (0, 255, 0))
        prompt_text = prompt_font.render("Press SPACE to Start", True, (255, 255, 255))

        # Center the text
        screen.blit(title_text, ((screen_width - title_text.get_width()) // 2, screen_height // 3))
        screen.blit(prompt_text, ((screen_width - prompt_text.get_width()) // 2, screen_height // 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False


def show_finish_screen(screen, font, screen_width, screen_height, level):
    title_font = pygame.font.SysFont(None, 48)
    prompt_font = pygame.font.SysFont(None, 24)
    waiting = True
    while waiting:
        screen.fill((0, 0, 0))  # Black background

        title_text = title_font.render("Beat all Levels, You Rock!", True, (0, 255, 0))
        prompt_text = prompt_font.render("You're the best", True, (255, 255, 255))
        instruction_text = prompt_font.render("Best SPACE to start again", True, (255, 255, 255))

        # Center the text
        screen.blit(title_text, ((screen_width - title_text.get_width()) // 2, screen_height // 4))
        screen.blit(prompt_text, ((screen_width - prompt_text.get_width()) // 2, screen_height // 3))
        screen.blit(instruction_text, ((screen_width - instruction_text.get_width()) // 2, screen_height // 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False