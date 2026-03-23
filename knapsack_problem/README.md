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

This benchmark compares two modeling frameworks:

- **PuLP** (CBC internal solver)
- **OR-Tools** (CBC backend)

No external solver installation is required.

---

## 📊 Experimental Procedure

For each benchmark instance:

1. Model construction
2. Solver execution
3. Runtime measurement
4. Objective value comparison against known optimum
5. Statistical comparison of solver performance

Results are automatically saved to:

results/experiment_results.csv

---

## 🚀 How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run experiments:

```bash
cd knapsack_problem
python -m src.run_experiments
```

Run analysis:

```bash
python -m analysis.analyze_results
```

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

---

## 📖 References

- Martello, S., & Toth, P. (1990). *Knapsack Problems: Algorithms and Computer Implementations.*
- Pisinger, D. (2005). Instances of 0/1 Knapsack Problem.

---

## 🚀 Status

🟡 In Progress

---

## 👨‍💻 Author

Josicleyton Santos  
Production Engineer & M.Sc. in Computer Science  
Focus: Optimization and Computational Intelligence