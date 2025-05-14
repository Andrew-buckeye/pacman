import pygame

TILE_TYPES = {
    "#": "wall",
    ".": "pellet",
    "P": "player_start",
    " ": "empty"
}

def start_pos(x, y, screen):
    print(f"Player starts at ({x}, {y})")

def draw_map(map_data, screen, TILE_SIZE):
    walls = []
    pellets = []
    for row_idx, row in enumerate(map_data):
        for col_idx, tile in enumerate(row):
            x = col_idx * TILE_SIZE
            y = row_idx * TILE_SIZE
            tile_type = TILE_TYPES.get(tile, "unknown")

            if tile_type == "wall":
                rect = pygame.Rect((x, y, TILE_SIZE, TILE_SIZE))
                walls.append(rect)
                pygame.draw.rect(screen, (0, 255, 0), rect)
            elif tile_type == "pellet":
                # Create a small Rect for the pellet
                pellet_rect = pygame.Rect(x + TILE_SIZE // 2 - 2, y + TILE_SIZE // 2 - 2, 4, 4)
                pellets.append(pellet_rect)
                # Draw the pellet (you still use draw.circle)
                # pygame.draw.circle(screen, (255, 255, 255), pellet_rect.center, 4)

            elif tile_type == "player_start":
                start_pos(x, y, screen)
    return screen, walls, pellets
