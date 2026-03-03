# Benchmark Results Analysis

## Solver Performance Comparison

The experimental results highlight a clear trade-off between execution time and robustness across the evaluated solvers.

### Runtime Performance

OR-Tools achieved superior computational efficiency.  
Its mean runtime was approximately **0.092 seconds**, compared to **0.184 seconds** for PuLP — nearly twice as fast on average.

The runtime boxplot confirms this trend, showing consistently lower medians for OR-Tools across instances.  
The Wilcoxon Signed-Rank test indicates that this performance difference is statistically significant:

- Test: Wilcoxon Signed-Rank
- Statistic: 0.0
- p-value: 9.54e-07

This suggests that OR-Tools is significantly faster than PuLP for the tested instances.

---

### Solution Quality and Robustness

PuLP demonstrated greater reliability in terms of optimality.

- **PuLP:** 100% optimal solutions found
- **OR-Tools:** 80.95% optimal solutions found

OR-Tools exhibited small optimality gaps in some large-scale instances (5000 and 10000 items), while PuLP consistently returned the known optimal solution.

---

## Conclusion

- **OR-Tools** is statistically faster and more computationally efficient.
- **PuLP** is more robust, consistently guaranteeing optimal solutions.
- If execution speed is critical, OR-Tools is preferable.
- If guaranteed optimality is required, PuLP is the safer choice.

The final solver selection depends on the application requirements:  
**speed versus absolute optimality guarantee.**