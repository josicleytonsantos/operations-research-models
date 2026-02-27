"""
0-1 Knapsack Problem
Computational Benchmark

Solvers evaluated:
- PuLP (CBC internal)
- OR-Tools (CBC backend)

Author: Josicleyton Santos
Repository: https://github.com/josicleytonsantos/operations-research-models
"""

# ==========================================================
# IMPORTS
# ==========================================================

import os
import pandas as pd
from .solvers import (
    read_knapsack_instance,
    solve_with_pulp,
    solve_with_ortools,
)

# ==========================================================
# PATH CONFIGURATION
# ==========================================================

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
INSTANCES_PATH = os.path.join(BASE_PATH, "instances")
RESULTS_PATH = os.path.join(BASE_PATH, "results")

os.makedirs(RESULTS_PATH, exist_ok=True)

OUTPUT_FILE = os.path.join(RESULTS_PATH, "experiment_results.csv")

# ==========================================================
# AVAILABLE SOLVERS
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

    for instance_name in instance_files:

        instance_path = os.path.join(INSTANCES_PATH, instance_name)

        print(f"Running instance: {instance_name}")

        n, capacity, profits, weights, known_solution = \
            read_knapsack_instance(instance_path)

        known_optimal = sum(
            profits[i] * known_solution[i]
            for i in range(n)
        )

        for solver_name, solver_function in SOLVERS.items():

            try:
                solution, objective, runtime, status = solver_function(
                    n, capacity, profits, weights
                )

                results.append({
                    "instance": instance_name,
                    "solver": solver_name,
                    "n_items": n,
                    "capacity": capacity,
                    "objective": objective,
                    "known_optimal": known_optimal,
                    "optimality_gap": (
                        0 if objective is None
                        else known_optimal - objective
                    ),
                    "found_optimal": int(objective == known_optimal),
                    "runtime": runtime,
                    "status": status
                })

            except Exception as e:

                results.append({
                    "instance": instance_name,
                    "solver": solver_name,
                    "n_items": n,
                    "capacity": capacity,
                    "objective": None,
                    "known_optimal": known_optimal,
                    "optimality_gap": None,
                    "found_optimal": 0,
                    "runtime": None,
                    "status": f"Error: {str(e)}"
                })

    df_results = pd.DataFrame(results)
    df_results.to_csv(OUTPUT_FILE, index=False)

    print("\nExperiment completed successfully.")
    print(f"Results saved to: {OUTPUT_FILE}")


# ==========================================================
# ENTRY POINT
# ==========================================================

if __name__ == "__main__":
    run_experiments()