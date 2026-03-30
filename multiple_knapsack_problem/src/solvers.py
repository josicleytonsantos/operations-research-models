"""
Multiple Knapsack Problem (MKP)
Benchmark Analysis

Solvers evaluated:
- PuLP (CBC internal)
- OR-Tools (CBC backend)

Author: Josicleyton Santos
Repository: https://github.com/josicleytonsantos/operations-research-models/
e-mail: santos.josicleyton@gmail.com
"""

import time
from pulp import (
    LpProblem,
    LpMaximize,
    LpVariable,
    lpSum,
    LpBinary,
    PULP_CBC_CMD,
    LpStatus,
    value,
)
from ortools.linear_solver import pywraplp

# ==========================================================
# INSTANCE READER
# ==========================================================

def read_mkp_instance(file_path):

    with open(file_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    idx = 0

    # Number of knapsacks
    m = int(lines[idx])
    idx += 1

    # Number of items
    n = int(lines[idx])
    idx += 1

    # Capacities
    capacities = []
    for _ in range(m):
        capacities.append(int(lines[idx]))
        idx += 1

    # Weights and profits
    weights = []
    profits = []

    for _ in range(n):
        w, p = map(int, lines[idx].split())
        weights.append(w)
        profits.append(p)
        idx += 1

    return m, n, capacities, weights, profits

# ==========================================================
# PULP SOLVER
# ==========================================================

def solve_with_pulp(m, n, capacities, weights, profits):

    model = LpProblem("MKP", LpMaximize)

    x = LpVariable.dicts(
        "x",
        ((i, j) for i in range(m) for j in range(n)),
        cat=LpBinary
    )

    model += lpSum(
        profits[j] * x[i, j]
        for i in range(m)
        for j in range(n)
    )

    for i in range(m):
        model += lpSum(
            weights[j] * x[i, j]
            for j in range(n)
        ) <= capacities[i]

    for j in range(n):
        model += lpSum(
            x[i, j] for i in range(m)
        ) <= 1

    start = time.time()
    model.solve(PULP_CBC_CMD(msg=False))
    runtime = time.time() - start

    objective = value(model.objective)
    status = LpStatus[model.status]

    solution = [
        (i, j)
        for i in range(m)
        for j in range(n)
        if x[i, j].value() is not None and int(x[i, j].value()) == 1
    ]

    gap = None

    return solution, objective, runtime, status, gap


# ==========================================================
# OR-TOOLS SOLVER
# ==========================================================

def solve_with_ortools(m, n, capacities, weights, profits):

    solver = pywraplp.Solver.CreateSolver("CBC")

    x = {}
    for i in range(m):
        for j in range(n):
            x[i, j] = solver.BoolVar(f"x_{i}_{j}")

    solver.Maximize(
        sum(
            profits[j] * x[i, j]
            for i in range(m)
            for j in range(n)
        )
    )

    for i in range(m):
        solver.Add(
            sum(weights[j] * x[i, j] for j in range(n))
            <= capacities[i]
        )

    for j in range(n):
        solver.Add(
            sum(x[i, j] for i in range(m)) <= 1
        )

    start = time.time()
    status_code = solver.Solve()
    runtime = time.time() - start

    objective = solver.Objective().Value()

    status_map = {
        pywraplp.Solver.OPTIMAL: "Optimal",
        pywraplp.Solver.FEASIBLE: "Feasible",
        pywraplp.Solver.INFEASIBLE: "Infeasible",
        pywraplp.Solver.ABNORMAL: "Abnormal",
        pywraplp.Solver.NOT_SOLVED: "Not Solved",
    }

    status = status_map.get(status_code, "Unknown")

    solution = [
        (i, j)
        for i in range(m)
        for j in range(n)
        if x[i, j].solution_value() > 0.5
    ]

    gap = None

    return solution, objective, runtime, status, gap