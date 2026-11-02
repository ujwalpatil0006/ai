# Model-Based Agent for Grid Navigation

grid = [
    ['S', '.', '#'],
    ['.', '.', '.'],
    ['.', '.', 'G']
]

position = [0, 0]  # Starting position
goal = [2, 2]

# Internal state
visited = set()

while position != goal:
    x, y = position
    visited.add(tuple(position))

     # Move right if possible
    if y + 1 < 3 and grid[x][y + 1] != '#' and (x, y + 1) not in visited:
        position = [x, y + 1]

    # Move down if possible
    elif x + 1 < 3 and grid[x + 1][y] != '#' and (x + 1, y) not in visited:
        position = [x + 1, y]

    # Move left if possible
    elif y - 1 >= 0 and grid[x][y - 1] != '#' and (x, y - 1) not in visited:
        position = [x, y - 1]

    # Move up if possible
    elif x - 1 >= 0 and grid[x - 1][y] != '#' and (x - 1, y) not in visited:
        position = [x - 1, y]

    else:
        print("No path found!")
        break
    
    print("Current Position:", position)

if position == goal:
    print("Goal Reached!")
