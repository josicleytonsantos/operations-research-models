# Multiple Knapsack Problem (MKP)

## 📌 Problem Description

The Multiple Knapsack Problem (MKP) is a classical combinatorial optimization problem and a generalization of the 0-1 Knapsack Problem.

Given:

- A set of items
- Each item has a profit (value)
- Each item has a weight
- Multiple knapsacks with limited capacities

The objective is to assign items to knapsacks such that:

- Each item can be assigned to at most one knapsack
- The capacity of each knapsack cannot be exceeded
- The total profit is maximized

Each item may either be assigned to a knapsack or left unused.

The MKP is NP-hard and widely used as a benchmark for Mixed Integer Programming (MILP) solvers.

---

## 🧮 Mathematical Formulation

### Sets

- \( i = 1, ..., m \) knapsacks  
- \( j = 1, ..., n \) items  

### Parameters

- \( p_j \): profit of item \(j\)  
- \( w_j \): weight of item \(j\)  
- \( c_i \): capacity of knapsack \(i\)

### Decision Variables

$$
x_{ij} \in \{0,1\}
$$

Where:

- \(x_{ij} = 1\) if item \(j\) is assigned to knapsack \(i\)

### Objective Function

$$
\max \sum_{i=1}^{m}\sum_{j=1}^{n} p_j x_{ij}
$$

### Constraints

**Knapsack capacity constraints**

$$
\sum_{j=1}^{n} w_j x_{ij} \leq c_i \quad \forall i
$$

**Each item assigned at most once**

$$
\sum_{i=1}^{m} x_{ij} \leq 1 \quad \forall j
$$

**Binary variables**

$$
x_{ij} \in \{0,1\}
$$

---

## 🛠 Implementation

This benchmark compares two modeling frameworks:

- **PuLP** (CBC internal solver)
- **OR-Tools** (CBC backend)

Both implementations solve the MKP using Mixed Integer Linear Programming (MILP).

A **time limit of 120 seconds** is imposed for each run for testing purposes.

---

## 📊 Experimental Procedure

For each benchmark instance:

1. Model construction
2. Solver execution
3. Runtime measurement
4. Objective value comparison
5. Relative gap evaluation
6. Statistical comparison of solver performance

Results are automatically saved to:

```
results/experiment_results.csv
```

The file contains:

- instance name
- solver used
- number of knapsacks
- number of items
- objective value
- runtime
- solver status
- MIP gap

---

## 🚀 How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run experiments:

```bash
cd multiple_knapsack_problem
python -m src.run_experiments
```

Run analysis:

```bash
python -m analysis.analyze_results
```

---

## 📂 Instances

The instances included in this repository are derived from the benchmark set associated with the manuscript:

**Dell'Amico, M., Delorme, M., Iori, M., & Martello, S. (2018)**  
*Mathematical models and decomposition methods for the multiple knapsack problem.*

These instances were used in the **computational experiments section of the paper**.

### Instance Format

Each instance file follows the format:

| Section | Content | Description |
|-------|--------|-------------|
| Line 1 | `m` | Number of knapsacks |
| Line 2 | `n` | Number of items |
| Next m lines | `ci` | Capacity of knapsack i |
| Next n lines | `wj pj` | Weight and profit of item j |

---

## 📖 References

- Dell'Amico, M., Delorme, M., Iori, M., & Martello, S. (2018).  
  *Mathematical models and decomposition methods for the multiple knapsack problem.*

- Martello, S., & Toth, P. (1990).  
  *Knapsack Problems: Algorithms and Computer Implementations.*

---

## 👨‍💻 Author

Josicleyton Santos  
Production Engineer & M.Sc. in Computer Science  
Focus: Optimization and Computational Intelligence