"""
0-1 Knapsack Problem
Computational Benchmark

Solvers evaluated:
- PuLP (CBC internal)
- OR-Tools (CBC backend)

Author: Josicleyton Santos
Repository: https://github.com/josicleytonsantos/operations-research-models
e-mail: santos.josicleyton@gmail.com
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
SOLUTIONS_PATH = os.path.join(RESULTS_PATH, "solutions")

os.makedirs(RESULTS_PATH, exist_ok=True)
os.makedirs(SOLUTIONS_PATH, exist_ok=True)

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

                # ==================================================
                # GAP (AGORA CORRETO)
                # ==================================================
                gap = (
                    None if objective is None
                    else known_optimal - objective
                )

                # ==================================================
                # SAVE SOLUTION TO FILE
                # ==================================================
                solution_filename = f"{instance_name}_{solver_name}.txt"
                solution_path = os.path.join(SOLUTIONS_PATH, solution_filename)

                with open(solution_path, "w") as f:
                    f.write(f"Instance: {instance_name}\n")
                    f.write(f"Solver: {solver_name}\n")
                    f.write(f"Status: {status}\n")
                    f.write(f"Objective: {objective}\n")
                    f.write(f"Known optimal: {known_optimal}\n")
                    f.write(f"Gap: {gap}\n")
                    f.write(f"Runtime: {runtime}\n\n")

                    f.write("Solution (x[i]):\n")

                    if solution is not None:
                        for i, val in enumerate(solution):
                            f.write(f"x[{i}] = {val}\n")
                    else:
                        f.write("No solution found.\n")

                # ==================================================
                # SAVE RESULTS
                # ==================================================
                results.append({
                    "instance": instance_name,
                    "solver": solver_name,
                    "n_items": n,
                    "capacity": capacity,
                    "objective": objective,
                    "known_optimal": known_optimal,
                    "gap": gap,
                    "found_optimal": int(objective == known_optimal) if objective is not None else 0,
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
                    "gap": None,
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