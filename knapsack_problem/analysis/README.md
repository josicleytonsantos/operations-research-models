# Knapsack Problem — Solver Benchmark

This experiment compares the performance of two optimization frameworks applied to the 0-1 Knapsack Problem:

- PuLP (using CBC internally)
- OR-Tools (using CBC backend)

The benchmark uses instances from the knapPI dataset, with problem sizes ranging from 100 to 10,000 items.

The analysis evaluates:

- Runtime performance
- Solution quality
- Optimality gap
- Optimal solution detection rate
- Statistical significance

---

# Benchmark Results Analysis

## Solver Performance Comparison

A total of 21 instances were evaluated for each solver.

The experiments highlight a clear trade-off between execution speed and robustness in reaching optimality.

---

# Runtime Performance

OR-Tools demonstrated significantly better computational efficiency.

### Average Runtime

| Solver | Mean Runtime (s) | Median Runtime (s) | Std Runtime |
|-------|-----------------|------------------|------------|
| OR-Tools | 0.092 | 0.039 | 0.125 |
| PuLP | 0.205 | 0.119 | 0.216 |

OR-Tools is approximately 2.2× faster on average.

---

## Statistical Test

**Wilcoxon Signed-Rank Test was applied to compare runtimes.

**Result**

Test: Wilcoxon Signed-Rank
Statistic: 0.0
P-value: 9.5367431640625e-07


This indicates that the runtime difference between the solvers is statistically significant.

---

# Solution Quality

Both solvers produced very similar objective values across the tested instances.

| Solver | Mean Objective | Median Objective |
|------|------|------|
| OR-Tools | 71,370.24 | 18,051 |
| PuLP | 71,371.19 | 18,051 |

This shows that both solvers reach nearly identical solutions for most problems.

---

# Optimality Gap Analysis

PuLP consistently found the optimal solution for all instances.

| Solver | Mean Gap | Median Gap | Mean Relative Gap |
|------|------|------|------|
| OR-Tools | 0.95 | 0.0 | 6.05e-06 |
| PuLP | 0.0 | 0.0 | 0.0 |

The small deviations observed in OR-Tools occur mainly in large-scale instances (5000 and 10000 items).

However, these gaps are extremely small and close to the optimal solution.

---

# Optimal Solution Detection Rate

| Solver | Optimal Solutions |
|------|------|
| PuLP | 100% |
| OR-Tools | 80.95% |


OR-Tools failed to match the known optimal solution in 4 instances, all of them large-scale problems.

No timeouts occurred during the experiments.

---

# Key Observations

### OR-Tools
- Faster runtime
- Better scalability
- Lower median execution time
- Very small optimality gaps in large instances

### PuLP
- Higher runtime
- Greater runtime variability
- Always finds the optimal solution
- Zero optimality gap

---

# Conclusion

The benchmark reveals a clear trade-off:

| Scenario | Recommended Solver |
|---------|-------------------|
| Fast execution required | OR-Tools |
| Guaranteed optimal solution | PuLP |

Overall, OR-Tools provides better performance, while PuLP offers stronger optimality guarantees.

For large-scale optimization workflows, OR-Tools is often the preferred choice due to its speed advantage with minimal loss in solution quality.

---

## 👨‍💻 Author

Josicleyton Santos  
Production Engineer & M.Sc. in Computer Science  
Focus: Optimization and Computational Intelligence