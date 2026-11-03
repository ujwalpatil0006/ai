# BFS for Robot Path Planning

grid = [
    ['S', '.', '#'],
    ['.', '.', '.'],
    ['.', '.', 'G']
]

start = (0, 0)
goal = (2, 2)

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    queue = [(start, [])]
    visited = [start]

    while queue:
        position, path = queue.pop(0)

        if position == goal:
            return path

        x, y = position

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy

            if (0 <= nx < 3 and 0 <= ny < 3
                    and grid[nx][ny] != '#'
                    and (nx, ny) not in visited):

                visited.append((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None

path = bfs()

print("Path:", path)
print("Total Steps:", len(path))
