# Analysis of Multiple Knapsack Problem Experiments

This directory contains the analysis of computational experiments for the **Multiple Knapsack Problem (MKP)**.  
The experiments compare two optimization approaches implemented in the project:

- **PuLP** (Python linear programming modeling library)
- **OR-Tools** (Google optimization toolkit)

The experiments were conducted using benchmark instances from the dataset associated with the manuscript:

> Dell'Amico, M., Delorme, M., Iori, M., & Martello, S.  
> *Mathematical models and decomposition methods for the multiple knapsack problem.*  
> Operations Research, 2018.

A **time limit of 300 seconds** was imposed for each solver run.

---

# Files

## `experiment_results.csv`

This file contains the **raw results of each solver execution** on each MKP instance.

Each row corresponds to a single solver run.

### Columns

| Column | Description |
|------|-------------|
| instance | Instance file name |
| solver | Solver used (PuLP or OR-Tools) |
| m_knapsacks | Number of knapsacks |
| n_items | Number of items |
| objective | Objective function value obtained |
| runtime | Solver runtime in seconds |
| status | Solver status (Optimal or Feasible) |
| gap | Reported optimality gap |

---

## `performance_statistics.csv`

This file summarizes **aggregate statistics per solver**.

### Metrics

| Metric | Description |
|------|-------------|
| mean_runtime | Average runtime across all instances |
| median_runtime | Median runtime |
| std_runtime | Standard deviation of runtime |
| mean_objective | Average objective value |
| median_objective | Median objective value |
| mean_relative_gap | Average relative optimality gap |
| optimal_rate | Percentage of runs that reached optimality |
| timeout_rate | Percentage of runs that reached the time limit |

---

## `statistical_test.txt`

Contains the **statistical comparison between solvers** using a non-parametric hypothesis test.

### Wilcoxon Signed-Rank Test

The **Wilcoxon signed-rank test** was used to compare the runtime distributions of the two solvers.

Results:

- **Statistic:** 5413.0  
- **P-value:** 9.515e-05

Since the p-value is much smaller than 0.05, the null hypothesis that both solvers have equal runtime distributions can be rejected, indicating a statistically significant difference in runtime performance.

---

# Generated Visualizations

The following plots summarize the experimental results.

## Relative Gap Distribution

This plot shows the distribution of the **relative optimality gap** achieved by each solver.

- Both solvers achieve very small gaps.
- Most runs are close to optimal.

---

## Objective Value Distribution

This boxplot compares the **objective values obtained by each solver**.

- Both solvers produce very similar objective values.
- This indicates consistent solution quality.

---

## Runtime Distribution

This plot compares the **runtime distributions** of the solvers.

- Large variance appears due to difficult instances.
- Some runs reach the time limit.

---

# Summary

The experiments indicate that:

- **Both solvers produce similar objective values**, indicating comparable solution quality.
- **PuLP achieved a higher optimality rate** across the tested instances.
- **OR-Tools often finds high-quality feasible solutions faster**, especially for smaller instances.
- The **Wilcoxon statistical test confirms a significant difference in runtime behavior**.

Overall, both tools are suitable for solving MKP instances, but they exhibit different performance characteristics depending on instance size and difficulty.

---

# Reproducibility

To reproduce the analysis:

1. Run the experiment scripts in the main project directory.
2. Collect the results in `experiment_results.csv`.
3. Execute the analysis scripts to generate statistics and plots.

Required Python libraries:

pandas
numpy
matplotlib
seaborn
scipy

---