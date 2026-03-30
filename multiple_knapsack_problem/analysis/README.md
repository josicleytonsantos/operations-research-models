# Multiple Knapsack Problem — Solver Benchmark

This experiment compares the performance of two optimization frameworks applied to the **Multiple Knapsack Problem (MKP)**:

* PuLP (using CBC internally)
* OR-Tools (using CBC backend)

The benchmark uses instances derived from the MKP dataset with different configurations of:

* Number of knapsacks
* Number of items
* Instance types (uncorrelated, weakly correlated, strongly correlated)

The analysis evaluates:

* Runtime performance
* Solution quality
* Optimality gap
* Optimal solution detection rate
* Statistical significance

---

# Benchmark Results Analysis

## Solver Performance Comparison

A total of 90 instances were evaluated for each solver.

The experiments show that both solvers are highly reliable for solving MKP instances, consistently reaching optimal solutions. However, some differences appear in runtime behavior, especially in larger instances.

---

# Runtime Performance

The runtime distribution reveals that most instances are solved very quickly by both solvers, but a few large instances significantly increase the average runtime.

![Runtime Distribution](sandbox:/mnt/data/runtime_boxplot.png)

### Average Runtime

| Solver   | Mean Runtime (s) | Median Runtime (s) | Std Runtime |
| -------- | ---------------- | ------------------ | ----------- |
| OR-Tools | 8.10             | 0.086              | 30.59       |
| PuLP     | 6.74             | 0.170              | 27.25       |

Key observations:

* PuLP shows a lower mean runtime, mainly due to fewer extreme runtime outliers.
* OR-Tools has a smaller median runtime, indicating faster performance for the majority of instances.
* Large-scale problems (especially with 40 items and 20 knapsacks) produced the highest runtimes for both solvers.
* Runtime variability is significant due to a few computationally expensive instances.

This behavior is clearly visible in the runtime boxplot, where most solutions cluster near zero runtime while a few outliers reach over 200 seconds.

---

## Statistical Test

A Wilcoxon Signed-Rank Test was applied to compare solver runtimes.

**Result**

Test: Wilcoxon Signed-Rank
Statistic: 1182.0
P-value: 0.0004967503163557723

The result indicates that the runtime difference between the solvers is statistically significant.

---

# Solution Quality

Both solvers produced exactly the same objective values across all instances.

| Solver   | Mean Objective | Median Objective |
| -------- | -------------- | ---------------- |
| OR-Tools | 9,339.09       | 7,619.5          |
| PuLP     | 9,339.09       | 7,619.5          |

This confirms that both frameworks are equally effective in identifying optimal solutions for the tested MKP instances.

The objective value distribution reflects the diversity of the problem instances rather than solver differences.

---

# Optimality Gap Analysis

No optimality gap was observed during the experiments.

| Solver   | Mean Gap | Median Gap | Mean Relative Gap |
| -------- | -------- | ---------- | ----------------- |
| OR-Tools | 0.0      | 0.0        | 0.0               |
| PuLP     | 0.0      | 0.0        | 0.0               |

Both solvers consistently reached the optimal solution for every tested instance.

This indicates that:

* The MKP instances are solvable with high reliability using CBC-based solvers.
* There is no loss in solution quality between the two frameworks.

---

# Optimal Solution Detection Rate

| Solver   | Optimal Solutions |
| -------- | ----------------- |
| PuLP     | 100%              |
| OR-Tools | 100%              |

Additionally:

* No timeouts occurred during the experiments.
* All instances were successfully solved within the computational limits.

---

# Key Observations

### OR-Tools

* Lower median runtime
* Faster for most small and medium instances
* Slightly higher runtime variability due to a few large outliers
* Highly efficient CBC integration

### PuLP

* Lower mean runtime overall
* More stable performance across larger instances
* Similar performance in small instances
* Identical solution quality

---

# Conclusion

The benchmark shows that both solvers perform extremely well for the Multiple Knapsack Problem.

| Scenario                        | Recommended Solver |
| ------------------------------- | ------------------ |
| Faster typical runtime          | OR-Tools           |
| More stable average performance | PuLP               |
| Guaranteed optimal solution     | Both               |

Overall:

* Both solvers achieved 100% optimal solutions.
* Runtime differences exist but are relatively small for most instances.
* Performance divergence mainly appears in larger MKP configurations.

This suggests that either solver can be reliably used for MKP research and benchmarking, with the choice depending mainly on runtime preference and workflow integration.

---

## 👨‍💻 Author

Josicleyton Santos
Production Engineer & M.Sc. in Computer Science
Focus: Optimization and Computational Intelligence