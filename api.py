from fastapi import FastAPI
from auth.routes import router as auth_router
from scan.routes import router as scan_router
from simulation.grid_generator import generate_grid
from simulation.decision_engine import find_best_spot, suggest_movement

app = FastAPI()
app.include_router(auth_router)
app.include_router(scan_router)

@app.get("/scan")
def scan(current_x: int = 0, current_y: int = 0):
    grid = generate_grid()
    best = find_best_spot(grid)

    movement = suggest_movement(
        current_x,
        current_y,
        best["x"],
        best["y"]
    )

    return {
        "grid": grid,
        "best_spot": best,
        "current_position": {
            "x": current_x,
            "y": current_y
        },
        "suggestion": movement
    }

