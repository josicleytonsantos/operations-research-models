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
- \( c \): knapsack capacity  

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
\sum_{i=1}^{n} w_i x_i \leq c
$$

$$
x_i \in \{0,1\}
$$

---

## 🛠 Implementation

This problem is implemented using:

- Python
- PuLP
- OR-Tools
- Pyomo
- CBC and GLPK solvers

The structure allows easy extension to other solvers such as Gurobi or SCIP.

---

## 📂 Instances

Benchmark instances are taken from the knapPI dataset proposed by David Pisinger (2005), a widely used benchmark in the literature.

Each instance file contains:

- Problem size and capacity
- Profit and weight for each item
- A reference optimal solution

| Section       | Content                                      | Description                                    |
|---------------|----------------------------------------------|------------------------------------------------|
| Line 1        | `n C`                                       | `n` → number of items<br>`C` → knapsack capacity |
| Next n lines  | `profit weight`                              | Profit and weight of each item                |
| Last line     | Binary vector                                | Known optimal solution (`0` = not selected, `1` = selected) |

## 📊 Methodology

For each instance:

- The model is built using different frameworks
- The solver runtime is measured
- The objective value is recorded
- Results are saved for comparison

This enables reproducible computational benchmarking.

---

## 📖 References

- Martello, S., & Toth, P. (1990). *Knapsack Problems: Algorithms and Computer Implementations.*
- Pisinger, D. (2005). Instances of 0/1 Knapsack Problem.

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
