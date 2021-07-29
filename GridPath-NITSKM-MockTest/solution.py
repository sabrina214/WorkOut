def try_right(grid, x, y, n):
    jumps = grid[x][y]

    if jumps > n - 1 - y:
        jumps = n - 1 - y
    while 0 < jumps:
        if grid[x][y+jumps] != 0:
            return [x, y + jumps]
        else:
            jumps -= 1
    return False


def try_down(grid, x, y, n):
    jumps = grid[x][y]

    if jumps > n - 1 - x:
        jumps = n - 1 - x
    while 0 < jumps:
        if grid[x+jumps][y] != 0:
            return [x + jumps, y]
        else:
            jumps -= 1
    return False


def find_path(grid, n):
    path = [[0, 0]]
    visited = [[0 for i in range(n)] for j in range(n)]

    while path:
        coord = path[-1]
        x, y = coord[0], coord[1]

        if (x, y) == (n-1, n-1):
            break

        if visited[x][y] == 0:
            visited[x][y] = 1
            next = try_right(grid, x, y, n)
            if next:
                path.append(next)
        elif visited[x][y] == 1:
            visited[x][y] = 2
            next = try_down(grid, x, y, n)
            if not next:
                path.pop()
            else:
                path.append(next)
        elif visited[x][y] == 2:
            return -1
    
    path_grid = get_grid_path(path)
    return path_grid


def get_grid_path(path):
    path_grid = [[0 for j in range(n)] for i in range(n)]
    for coord in path:
        path_grid[coord[0]][coord[1]] = 1
    return path_grid


n = int(input())
grid = [[int(i) for i in input().split()] for j in range(n)]
path = find_path(grid, n)

print()
for i in path:
    print(*i)
