import random

GRID_WIDTH = 5
GRID_HEIGHT = 5

def generate_grid():
    grid = []

    for y in range(GRID_HEIGHT):
        row = []

        for x in range(GRID_WIDTH):
            speed = random.uniform(5, 50)
            row.append(round(speed, 2))

        grid.append(row)

    return grid


if __name__ == "__main__":
    grid = generate_grid()

    for row in grid:
        print(row)