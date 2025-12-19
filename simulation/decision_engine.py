def find_best_spot(grid):
    best_speed = -1
    best_position = (0, 0)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            current_speed = grid[y][x]

            if current_speed > best_speed:
                best_speed = current_speed
                best_position = (x, y)

    return {
        "x": best_position[0],
        "y": best_position[1],
        "speed": best_speed
    }

def suggest_movement(current_x, current_y, best_x, best_y):
    if current_x == best_x and current_y == best_y:
        return "You are at the best spot. Stop moving."

    if current_x < best_x:
        return "Move right"

    if current_x > best_x:
        return "Move left"

    if current_y < best_y:
        return "Move forward"

    if current_y > best_y:
        return "Move backward"