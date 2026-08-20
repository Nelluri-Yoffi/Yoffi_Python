import random, time, os
W, H = 20, 10
def new_grid():
    return [[random.choice([0, 1]) for _ in range(W)] for _ in range(H)]
def step(grid):
    def neighbors(x, y):
        return sum(
            grid[(y+dy) % H][(x+dx) % W]
            for dy in (-1, 0, 1) for dx in (-1, 0, 1)
            if not (dx == 0 and dy == 0)
        )
    return [
        [1 if (grid[y][x] and neighbors(x, y) in (2, 3)) or
              (not grid[y][x] and neighbors(x, y) == 3) else 0
         for x in range(W)]
        for y in range(H)
    ]
def render(grid):
    os.system("cls" if os.name == "nt" else "clear")
    print("\n".join("".join("█" if c else " " for c in row) for row in grid))

grid = new_grid()
while True:
    render(grid)
    grid = step(grid)
    time.sleep(0.2)