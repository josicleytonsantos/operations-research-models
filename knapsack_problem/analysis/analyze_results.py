"""
Knapsack 0-1 Problem
Benchmark using:

- PuLP (CBC internal)
- OR-Tools (CBC backend)

Author: Josicleyton Santos
Repository: https://github.com/josicleytonsantos/operations-research-models/
"""

# ==========================================================
# IMPORTS
# ==========================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import friedmanchisquare, wilcoxon

sns.set(style="whitegrid")

# ==========================================================
# PATHS
# ==========================================================

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
RESULTS_DIR = os.path.join(BASE_PATH, "results")
RESULTS_FILE = os.path.join(RESULTS_DIR, "experiment_results.csv")

os.makedirs(RESULTS_DIR, exist_ok=True)

# ==========================================================
# LOAD DATA
# ==========================================================

df = pd.read_csv(RESULTS_FILE)
df = df.dropna(subset=["runtime"])

# ==========================================================
# SAVE PERFORMANCE STATISTICS
# ==========================================================

stats_table = df.groupby("solver").agg(
    mean_runtime=("runtime", "mean"),
    median_runtime=("runtime", "median"),
    std_runtime=("runtime", "std"),
    success_rate=("found_optimal", "mean")
)

stats_table["success_rate"] *= 100

stats_table.to_csv(os.path.join(RESULTS_DIR, "performance_statistics.csv"))

# ==========================================================
# SAVE BOXPLOT
# ==========================================================

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="solver", y="runtime")
plt.title("Runtime Distribution per Solver")
plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, "runtime_boxplot.png"))
plt.close()

# ==========================================================
# SAVE SUCCESS RATE PLOT
# ==========================================================

success_rates = df.groupby("solver")["found_optimal"].mean() * 100

plt.figure(figsize=(8, 5))
success_rates.plot(kind="bar")
plt.ylabel("Success Rate (%)")
plt.title("Optimal Solution Detection Rate")
plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, "success_rate.png"))
plt.close()

# ==========================================================
# STATISTICAL TEST
# ==========================================================

pivot_runtime = df.pivot(
    index="instance",
    columns="solver",
    values="runtime"
).dropna()

test_output_path = os.path.join(RESULTS_DIR, "statistical_test.txt")

with open(test_output_path, "w") as f:

    n_solvers = pivot_runtime.shape[1]

    if n_solvers >= 3:
        statistic, p_value = friedmanchisquare(
            *[pivot_runtime[col] for col in pivot_runtime.columns]
        )
        f.write("Friedman Test\n")
        f.write(f"Statistic: {statistic}\n")
        f.write(f"P-value: {p_value}\n")

    elif n_solvers == 2:
        col1, col2 = pivot_runtime.columns
        stat, p_value = wilcoxon(
            pivot_runtime[col1],
            pivot_runtime[col2]
        )
        f.write("Wilcoxon Signed-Rank Test\n")
        f.write(f"Comparing: {col1} vs {col2}\n")
        f.write(f"Statistic: {stat}\n")
        f.write(f"P-value: {p_value}\n")

    else:
        f.write("Not enough solvers for statistical testing.\n")