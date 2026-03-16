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

os.makedirs(RESULTS_PATH, exist_ok=True)

OUTPUT_FILE = os.path.join(RESULTS_PATH, "experiment_results.csv")

# ==========================================================
# SOLVERS
# ==========================================================

SOLVERS = {
    "PuLP": solve_with_pulp,
    "OR-Tools": solve_with_ortools,
}

# ==========================================================
# MAIN EXPERIMENT LOOP
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

        # Read TSP instance
        n, dist = read_tsp_instance(instance_path)

        for solver_name, solver_function in SOLVERS.items():

            try:

                objective, runtime, status, gap = solver_function(
                    n,
                    dist
                )

                results.append({
                    "instance": instance_name,
                    "solver": solver_name,
                    "n_nodes": n,
                    "objective": objective,
                    "runtime": runtime,
                    "status": status,
                    "gap": gap
                })

            except Exception as e:

                results.append({
                    "instance": instance_name,
                    "solver": solver_name,
                    "n_nodes": n,
                    "objective": None,
                    "runtime": None,
                    "status": f"Error: {str(e)}",
                    "gap": None
                })

    # ======================================================
    # SAVE RESULTS
    # ======================================================

    df_results = pd.DataFrame(results)

    df_results.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\nExperiment completed successfully.")
    print(f"Results saved to: {OUTPUT_FILE}")


# ==========================================================
# ENTRY POINT
# ==========================================================

if __name__ == "__main__":
    run_experiments()