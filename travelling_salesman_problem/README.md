# Traveling Salesman Problem (TSP)

## 📌 Problem Description

The Traveling Salesman Problem (TSP) is one of the most studied combinatorial optimization problems.

Given:

* A set of cities (nodes)
* The distance between each pair of cities

The objective is to determine a tour such that:

* Each city is visited exactly once
* The tour returns to the starting city
* The total travel distance is minimized

The TSP is NP-hard and serves as a fundamental benchmark for optimization algorithms and Mixed Integer Programming (MILP) solvers.

---

## 🧮 Mathematical Formulation

### Sets

* ( i, j = 1, ..., n ) cities

### Parameters

* ( d_{ij} ): distance from city (i) to city (j)

### Decision Variables

$$
x_{ij} \in {0,1}
$$

Where:

* (x_{ij} = 1) if the tour goes directly from city (i) to city (j)

### Auxiliary Variables (MTZ formulation)

$$
u_i \in \mathbb{R}
$$

Used to eliminate subtours.

---

### Objective Function

$$
\min \sum_{i=1}^{n} \sum_{j=1}^{n} d_{ij} x_{ij}
$$

---

### Constraints

**Each city has exactly one outgoing edge**

$$
\sum_{j=1, j \neq i}^{n} x_{ij} = 1 \quad \forall i
$$

**Each city has exactly one incoming edge**

$$
\sum_{i=1, i \neq j}^{n} x_{ij} = 1 \quad \forall j
$$

**Subtour elimination (MTZ constraints)**

$$
u_i - u_j + n x_{ij} \leq n - 1 \quad \forall i \neq j, ; i,j \geq 2
$$

**Binary variables**

$$
x_{ij} \in {0,1}
$$

---

## 🛠 Implementation

This benchmark compares two modeling frameworks:

* **PuLP** (CBC internal solver)
* **OR-Tools** (CBC backend)

Both implementations solve the TSP using a Mixed Integer Linear Programming (MILP) formulation based on the **Miller-Tucker-Zemlin (MTZ)** subtour elimination approach.

⚠️ **No time limit is imposed** — solvers run until optimality is reached or infeasibility is proven.

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

* instance name
* solver used
* number of nodes
* objective value
* runtime
* solver status
* MIP gap

Additionally, individual solutions (routes) are stored in:

```
results/solutions/
```

---

## 🚀 How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run experiments:

```bash
cd travelling_salesman_problem
python -m src.run_experiments
```

Run analysis:

```bash
python -m analysis.analyze_results
```

---

## 📂 Instances

The instances used in this repository follow a standard coordinate-based format, commonly used in TSP benchmarks.

### Instance Format

Each instance file follows the format:

| Section   | Content   | Description                    |
| --------- | --------- | ------------------------------ |
| Each line | `i xi yi` | Node index and its coordinates |

Where:

* `i`: node identifier
* `xi`, `yi`: Cartesian coordinates of node (i)

The distance matrix is computed using the Euclidean distance:

$$
d_{ij} = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}
$$

---

## 📖 References

* Miller, C. E., Tucker, A. W., & Zemlin, R. A. (1960).
  *Integer Programming Formulation of Traveling Salesman Problems.*

* Applegate, D., Bixby, R., Chvátal, V., & Cook, W. (2006).
  *The Traveling Salesman Problem: A Computational Study.*

* Reinelt, G. (1991).
  *TSPLIB — A Traveling Salesman Problem Library.*

---

## 🚀 Status

🟡 In Progress

---

## 👨‍💻 Author

Josicleyton Santos
Production Engineer & M.Sc. in Computer Science
Focus: Optimization and Computational Intelligence

---

Se quiser, posso no próximo passo:

👉 padronizar TODOS os READMEs do seu repositório (Knapsack, MKP, TSP) num nível de portfólio profissional forte / GitHub destaque.