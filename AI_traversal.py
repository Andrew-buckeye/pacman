from collections import deque

'''
(x, y)- current position on the grid
wall_list- where the walls are
pellets_list- where the remaining pellets are, ie where we should go next
tile_size- size of grid spaces, its 25x25



'''

# first think, where are we? When you or I play pacman we use our eyes (sensor) to track position. 
# computers do not have eyes
def pos_to_grid(x, y, tile_size): 
    return (x//tile_size, y//tile_size)
def grid_to_pos(grid, size): 
    return (grid[0] * size, grid[1] * size)


def BFS_movement(x, y, wall_list, pellets_list, tile_size):
    # tile coordintates for starting position
    start = pos_to_grid(x, y, tile_size)
    visited = set()
    parent = {}  # saves space
    queue = deque([start])
    visited.add(start)
   
    wall_set = set((w.left // tile_size, w.top // tile_size) for w in wall_list)
    pellet_grids = set(pos_to_grid(p.centerx, p.centery, tile_size) for p in pellets_list)
    
    found_pellet = None
        
    while queue:
        # print(len(queue)) for the third level, the queue starts to explode, why?
        current = queue.popleft() # Hold the current tile position
        if current in pellet_grids:
            found_pellet = current
            break #exits the while loop
        
        # determines where to go next, North, South, East, West position
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0] + dx, current[1] + dy) 
            if neighbor not in visited and neighbor not in wall_set and neighbor:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
        
    if found_pellet:
        # Backtrack from pellet to start
        current = found_pellet
        path = []
        while current != start:
            path.append(current)
            current = parent[current]
        path.reverse()
        next_tile = path[0] if path else start
        return grid_to_pos(next_tile, tile_size)

    return x, y  # fallback: no pellet found


def DFS_movement(x, y, wall_list, pellets_list, tile_size):
    visited = set()
    wall_set = set((w.left // tile_size, w.top // tile_size) for w in wall_list)
    pellet_grids = set(pos_to_grid(p.centerx, p.centery, tile_size) for p in pellets_list)

    start = pos_to_grid(x, y, tile_size)
    stack = [start]
    parent = {}
    found_pellet = None

    visited.add(start)
    print(f"Starting DFS at {start}")

    while stack:
        current = stack.pop()
        print(f"Currently at {current}, stack size: {len(stack)}")

        if current in pellet_grids:
            found_pellet = current
            print(f"Found pellet at {current}")
            break # found a pellet, go process this

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            print(f"Checking neighbor: {neighbor}")
            if neighbor not in visited and neighbor not in wall_set: # if a new, available node is found
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)
                print(f"Added {neighbor} to stack")



    if found_pellet:
        path = []
        current = found_pellet
        while current != start:
            path.append(current)
            current = parent[current]
        path.reverse()
        next_tile = path[0] if path else start
        print(f"Returning next tile: {next_tile}")
        return grid_to_pos(next_tile, tile_size)
    
    print(f"No pellet found, returning {x, y}")
    return x, y
