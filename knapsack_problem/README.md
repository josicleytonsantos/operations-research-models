# 0-1 Knapsack Problem

## 📌 Problem Description

The 0-1 Knapsack Problem is a classical combinatorial optimization problem.

Given:
- A set of items
- Each item has a profit (value)
- Each item has a weight
- A knapsack with limited capacity

The objective is to select a subset of items that maximizes total profit without exceeding the capacity.

Each item can either be selected (1) or not selected (0).

This problem is NP-hard and widely used as a benchmark for Integer Programming solvers.

---

## 🧮 Mathematical Formulation

### Sets

- \( i = 1, ..., n \) items

### Parameters

- \( p_i \): profit of item i  
- \( w_i \): weight of item i  
- \( C \): knapsack capacity  

### Decision Variables

$$
x_i \in \{0,1\}
$$

### Objective Function

$$
\max \sum_{i=1}^{n} p_i x_i
$$

### Constraints

$$
\sum_{i=1}^{n} w_i x_i \leq C
$$

$$
x_i \in \{0,1\}
$$

---

## 🛠 Implementation

This problem is implemented using:

- Python
- PuLP
- CBC Solver

Future implementations may include:
- Pyomo
- Gurobi
- SCIP

---

## 📂 Instances

Benchmark instances are obtained from classical literature and public repositories.

Each instance file contains:
- Number of items
- Capacity
- Profits and weights

---

## 📊 Methodology

For each instance:

1. Read data
2. Build the mathematical model
3. Solve using an exact solver
4. Record:
   - Objective value
   - Execution time
   - Solver status
   - Optimality gap (if available)

---

## 📖 References

- Martello, S., & Toth, P. (1990). *Knapsack Problems: Algorithms and Computer Implementations.*
- OR-Library – Beasley (1990)

---

## 📎 Folder Structure


knapsack/
│
├── model.ipynb
├── instances/
│ └── instance_01.txt
└── README.md


---

## 🚀 Status

🟡 In Progress
