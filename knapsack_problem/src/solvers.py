"""
Knapsack 0-1 Problem
Benchmark using:

- PuLP (CBC internal)
- OR-Tools (CBC backend)

Author: Josicleyton Santos
Repository: https://github.com/josicleytonsantos/operations-research-models/
e-mail: santos.josicleyton@gmail.com
"""

# ==============================
# IMPORTS
# ==============================

import time
import pulp
from ortools.linear_solver import pywraplp

# ==========================================================
# INSTANCE READER
# ==========================================================

def read_knapsack_instance(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    n, capacity = map(int, lines[0].split())
    profits = []
    weights = []

    for i in range(1, n + 1):
        p, w = map(int, lines[i].split())
        profits.append(p)
        weights.append(w)

    known_solution = list(map(int, lines[n + 1].split()))

    return n, capacity, profits, weights, known_solution

# ==========================================================
# SOLVERS
# ==========================================================

def solve_with_pulp(n, capacity, profits, weights):
    model = pulp.LpProblem("Knapsack", pulp.LpMaximize)
    x = [pulp.LpVariable(f"x_{i}", cat="Binary") for i in range(n)]

    model += pulp.lpSum(profits[i] * x[i] for i in range(n))
    model += pulp.lpSum(weights[i] * x[i] for i in range(n)) <= capacity

    start = time.time()
    status = model.solve(pulp.PULP_CBC_CMD(msg=False))
    runtime = time.time() - start

    solution = [int(x[i].value()) for i in range(n)]
    objective = pulp.value(model.objective)
    status_string = pulp.LpStatus[status]

    return solution, objective, runtime, status_string


def solve_with_ortools(n, capacity, profits, weights):
    solver = pywraplp.Solver.CreateSolver("CBC")

    x = [solver.BoolVar(f"x_{i}") for i in range(n)]

    solver.Maximize(sum(profits[i] * x[i] for i in range(n)))
    solver.Add(sum(weights[i] * x[i] for i in range(n)) <= capacity)

    start = time.time()
    status = solver.Solve()
    runtime = time.time() - start

    solution = [int(x[i].solution_value()) for i in range(n)]
    objective = solver.Objective().Value()
    status_string = "Optimal" if status == pywraplp.Solver.OPTIMAL else "Not Optimal"

    return solution, objective, runtime, status_string