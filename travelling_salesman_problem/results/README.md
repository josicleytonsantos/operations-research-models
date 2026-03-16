# Results Directory

This directory contains the results generated from the computational experiments for the **Multiple Knapsack Problem (MKP)**.

The experiments evaluate the performance of the following optimization solvers:

- **PuLP** (using CBC internally)
- **OR-Tools** (using the CBC backend)

All results were generated automatically by the script:

```
analysis/analyse_results.py
```

The script reads the raw experiment results and produces **performance statistics, plots, and statistical tests**.

---

# Files

## experiment_results.csv

This file contains the **raw results from each experiment execution**.

Each row represents **one solver run on one MKP instance**.

### Columns

| Column | Description |
|------|-------------|
| instance | Name of the MKP instance file |
| solver | Solver used in the experiment (PuLP or OR-Tools) |
| m_knapsacks | Number of knapsacks in the instance |
| n_items | Number of items in the instance |
| objective | Objective function value obtained |
| runtime | Execution time in seconds |
| status | Solver termination status |
| gap | Optimality gap reported by the solver |

This dataset is used as the **input for the analysis script**.

---

# Generated Analysis Files

The following files are produced automatically by the analysis script.

---

## performance_statistics.csv

This file contains **aggregated performance metrics per solver**.

Each row corresponds to a solver and summarizes its performance across all instances.

### Metrics

| Metric | Description |
|------|-------------|
| mean_runtime | Average runtime across all instances |
| median_runtime | Median runtime |
| std_runtime | Standard deviation of runtime |
| mean_objective | Average objective value |
| median_objective | Median objective value |
| mean_gap | Average solver gap |
| median_gap | Median solver gap |
| mean_relative_gap | Average relative gap with respect to the best solution found for each instance |
| optimal_rate | Fraction of runs that reached optimality |
| timeout_rate | Fraction of runs that did not finish within the time limit |

---

## runtime_boxplot.png

This plot shows the **distribution of solver runtimes**.

It allows a visual comparison of:

- Typical runtime behavior
- Variability across instances
- Presence of slow or difficult instances

The boxplot represents:

- Median runtime
- Interquartile range
- Outliers

---

## objective_boxplot.png

This plot compares the **distribution of objective values** obtained by each solver.

It helps verify whether:

- Both solvers reach similar solution quality
- Some solver consistently finds better solutions
- There is variability in the obtained objective values

---

## gap_boxplot.png

This plot shows the **distribution of the relative optimality gap**.

The relative gap is calculated as:

```
(best_known - objective) / best_known
```

Where:

- `best_known` is the best objective value found for each instance across all solvers.

A **gap close to zero** indicates that the solver found a solution very close to the best known.

---

## statistical_test.txt

This file contains the **results of the statistical comparison between solvers**.

The script automatically chooses the appropriate test depending on the number of solvers.

### Two solvers

If two solvers are present, the script performs the:

**Wilcoxon Signed-Rank Test**

This non-parametric test evaluates whether the **runtime distributions of the two solvers are statistically different**.

### Three or more solvers

If three or more solvers are evaluated, the script performs the:

**Friedman Test**

This test compares multiple algorithms across multiple problem instances.

### Output

The file reports:

- Test statistic
- P-value
- Solvers being compared

A **small p-value (< 0.05)** indicates that the difference in performance is statistically significant.

---

# Summary of the Analysis Workflow

The experimental workflow is:

1. Run experiments using:

```
src/run_experiments.py
```

2. Store raw results in:

```
results/experiment_results.csv
```

3. Run the analysis script:

```
analysis/analyse_results.py
```

4. The script generates:

```
performance_statistics.csv
runtime_boxplot.png
objective_boxplot.png
gap_boxplot.png
statistical_test.txt
```

---

# Reproducibility

To reproduce the analysis, the following Python libraries are required:

```
pandas
numpy
matplotlib
seaborn
scipy
```

They can be installed using:

```
pip install -r requirements.txt
```

---

# Author

**Josicleyton Santos**

GitHub  
https://github.com/josicleytonsantos/operations-research-models/

Email  
santos.josicleyton@gmail.com