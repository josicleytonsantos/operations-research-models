"""
Travelling Salesman Problem (TSP)
Benchmark Analysis

Solvers evaluated:
- PuLP (CBC internal)
- OR-Tools (CBC backend)

Author: Josicleyton Santos
Repository: https://github.com/josicleytonsantos/operations-research-models/
e-mail: santos.josicleyton@gmail.com
"""

# ==========================================================
# IMPORTS
# ==========================================================

import os
import pandas as pd

from .solvers import (
    read_tsp_instance,
    solve_with_pulp,
    solve_with_ortools,
)

# ==========================================================
# PATHS
# ==========================================================

BASE_PATH = os.path.dirname(os.path.dirname(__file__))

INSTANCES_PATH = os.path.join(BASE_PATH, "instances")
RESULTS_PATH = os.path.join(BASE_PATH, "results")
SOLUTIONS_PATH = os.path.join(RESULTS_PATH, "solutions")

os.makedirs(RESULTS_PATH, exist_ok=True)
os.makedirs(SOLUTIONS_PATH, exist_ok=True)

OUTPUT_FILE = os.path.join(RESULTS_PATH, "experiment_results.csv")

# ==========================================================
# SOLVERS
# ==========================================================

SOLVERS = {
    "PuLP": solve_with_pulp,
    "OR-Tools": solve_with_ortools,
}

# ==========================================================
# MAIN
# ==========================================================

def run_experiments():

    results = []

    instance_files = sorted(os.listdir(INSTANCES_PATH))

    if not instance_files:
        print("No instances found.")
        return

    for instance_name in instance_files:

        print(f"\nRunning instance: {instance_name}")

        instance_path = os.path.join(INSTANCES_PATH, instance_name)

        n, dist = read_tsp_instance(instance_path)

        for solver_name, solver_function in SOLVERS.items():

            try:

                route, objective, runtime, status, gap = solver_function(
                    n, dist
                )

                # ==========================================
                # SAVE SOLUTION
                # ==========================================
                solution_filename = f"{instance_name}_{solver_name}.txt"
                solution_path = os.path.join(SOLUTIONS_PATH, solution_filename)

                with open(solution_path, "w") as f:
                    f.write(f"Instance: {instance_name}\n")
                    f.write(f"Solver: {solver_name}\n")
                    f.write(f"Status: {status}\n")
                    f.write(f"Objective: {objective}\n")
                    f.write(f"Gap: {gap}\n")
                    f.write(f"Runtime: {runtime}\n\n")

                    f.write("Route:\n")

                    if route:
                        for i, j in route:
                            f.write(f"{i} -> {j}\n")
                    else:
                        f.write("No route found.\n")

                # ==========================================
                # SAVE RESULTS
                # ==========================================
                results.append({
                    "instance": instance_name,
                    "solver": solver_name,
                    "n_nodes": n,
                    "objective": objective,
                    "gap": gap,
                    "runtime": runtime,
                    "status": status
                })

            except Exception as e:

                results.append({
                    "instance": instance_name,
                    "solver": solver_name,
                    "n_nodes": n,
                    "objective": None,
                    "gap": None,
                    "runtime": None,
                    "status": f"Error: {str(e)}"
                })

    df_results = pd.DataFrame(results)
    df_results.to_csv(OUTPUT_FILE, index=False)

    print("\nExperiment completed successfully.")
    print(f"Results saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    run_experiments()