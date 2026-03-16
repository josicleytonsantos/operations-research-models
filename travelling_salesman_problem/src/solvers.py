"""
Travelling Salesman Problem (TSP)
Benchmark Analysis

Solvers evaluated:
- PuLP (CBC internal)
- OR-Tools (CBC backend)

Author: Josicleyton Santos
Repository: https://github.com/josicleytonsantos/operations-research-models/
"""

import time
import math

from pulp import (
    LpProblem,
    LpMinimize,
    LpVariable,
    lpSum,
    LpBinary,
    PULP_CBC_CMD,
    LpStatus,
    value,
)

from ortools.linear_solver import pywraplp

TIME_LIMIT = 300


# ==========================================================
# INSTANCE READER
# ==========================================================

def read_tsp_instance(file_path):

    nodes = []
    x = []
    y = []

    with open(file_path, "r") as f:
        for line in f:
            if not line.strip():
                continue

            i, xi, yi = line.split()

            nodes.append(int(i))
            x.append(float(xi))
            y.append(float(yi))

    n = len(nodes)

    # Distance matrix
    dist = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):

            dx = x[i] - x[j]
            dy = y[i] - y[j]

            dist[i][j] = math.sqrt(dx*dx + dy*dy)

    return n, dist


# ==========================================================
# PULP SOLVER (MTZ formulation)
# ==========================================================

def solve_with_pulp(n, dist):

    model = LpProblem("TSP", LpMinimize)

    x = LpVariable.dicts(
        "x",
        ((i, j) for i in range(n) for j in range(n) if i != j),
        cat=LpBinary
    )

    u = LpVariable.dicts(
        "u",
        range(n),
        lowBound=0,
        upBound=n-1
    )

    # Objective
    model += lpSum(
        dist[i][j] * x[i, j]
        for i in range(n)
        for j in range(n)
        if i != j
    )

    # Outgoing
    for i in range(n):
        model += lpSum(
            x[i, j] for j in range(n) if i != j
        ) == 1

    # Incoming
    for j in range(n):
        model += lpSum(
            x[i, j] for i in range(n) if i != j
        ) == 1

    # MTZ subtour elimination
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model += (
                    u[i] - u[j] + n * x[i, j] <= n - 1
                )

    solver = PULP_CBC_CMD(timeLimit=TIME_LIMIT, msg=False)

    start = time.time()
    model.solve(solver)
    runtime = time.time() - start

    objective = value(model.objective)
    status = LpStatus[model.status]

    gap = None
    try:
        gap = solver.solutionGap
    except:
        pass

    return objective, runtime, status, gap


# ==========================================================
# ORTOOLS SOLVER
# ==========================================================

def solve_with_ortools(n, dist):

    solver = pywraplp.Solver.CreateSolver("CBC")
    solver.SetTimeLimit(TIME_LIMIT * 1000)

    x = {}

    for i in range(n):
        for j in range(n):
            if i != j:
                x[i, j] = solver.BoolVar(f"x_{i}_{j}")

    u = {}

    for i in range(n):
        u[i] = solver.NumVar(0, n-1, f"u_{i}")

    solver.Minimize(
        sum(
            dist[i][j] * x[i, j]
            for i in range(n)
            for j in range(n)
            if i != j
        )
    )

    for i in range(n):
        solver.Add(
            sum(x[i, j] for j in range(n) if i != j) == 1
        )

    for j in range(n):
        solver.Add(
            sum(x[i, j] for i in range(n) if i != j) == 1
        )

    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                solver.Add(
                    u[i] - u[j] + n * x[i, j] <= n - 1
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

    gap = None
    try:
        gap = solver.MipGap()
    except:
        pass

    return objective, runtime, status, gap