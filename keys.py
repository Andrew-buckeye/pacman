import pygame
'''
x- x coordinate of the character
x- y coordinate of the character
'''
def handle_movement(keys, x, y, speed, screen_width, screen_height, character_height, character_width, obstacles):
    if keys[pygame.K_LEFT] and x>0:
        if not check_collision(x - speed, y, character_width, character_height, obstacles):
            x -= speed
    if keys[pygame.K_RIGHT] and x< screen_width-character_width:
        if not check_collision(x + speed, y, character_width, character_height, obstacles):
            x += speed

    if keys[pygame.K_UP] and y>0:
        if not check_collision(x, y-speed, character_width, character_height, obstacles):
            y-=speed

    if keys[pygame.K_DOWN] and y<screen_height-character_height:
        if not check_collision(x, y+speed, character_width, character_height, obstacles):
            y+=speed

    return x, y

def check_collision(new_x, new_y, character_height, character_width, obstacles):
    player_rect = pygame.Rect(new_x, new_y, character_width, character_height)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            return True
    return False

def check_and_eat_pellet(player_rect, pellets_list, score, map_design, TILE_SIZE):
    for pellet in pellets_list[:]:
        pellet_rect = pygame.Rect(pellet[0] - 4, pellet[1] - 4, 8, 8)
        if player_rect.colliderect(pellet_rect):
            score += 10
            pellets_list.remove(pellet)
    return score, pellets_list





    