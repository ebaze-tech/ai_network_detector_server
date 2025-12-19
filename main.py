import json
from simulation.grid_generator import generate_grid
from simulation.decision_engine import find_best_spot, suggest_movement

def run_simulation(current_x, current_y):
    grid = generate_grid()
    best = find_best_spot(grid)

    movement = suggest_movement(
        current_x,
        current_y,
        best["x"],
        best["y"]
    )

    response = {
        "grid": grid,
        "best_spot": best,
        "current_position": {
            "x": current_x,
            "y": current_y
        },
        "suggestion": movement
    }

    return response


if __name__ == "__main__":
    result = run_simulation(0, 0)
    print(json.dumps(result, indent=4))
