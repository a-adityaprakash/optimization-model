# Task 4 — Business Optimization using Linear Programming (PuLP)

## Objective
This task demonstrates how linear programming can solve a practical business decision: optimizing production mix to maximize profit subject to limited resources. The notebook and script implement the model, solve it, visualize the feasible region, and provide business insights.

## Problem Summary
- **Products:** Product A and Product B
- **Profits:** A = $20/unit, B = $30/unit
- **Resource usage:**
  - A: 2 machine hrs, 3 labor hrs
  - B: 4 machine hrs, 2 labor hrs
- **Resource availability:** Machine ≤ 100 hrs, Labor ≤ 90 hrs
- **Goal:** Maximize total profit.

## Files
- `task4_lp.py` — Standalone Python script that formulates and solves the LP using PuLP, prints results and saves `feasible_region.png`.
- `task4_optimization.ipynb` — Structured Jupyter notebook containing:
  - Problem description
  - Mathematical formulation
  - PuLP implementation
  - Visualization
  - Insights and extensions
- `feasible_region.png` — (generated) visualization of feasible region and optimal point (if you run the code).

## Requirements
pip install pulp matplotlib numpy

PuLP uses the default CBC solver (bundled) — no external solver required for this notebook.

## How to run
Option A — Run script

python task4_lp.py

This prints the solution and creates feasible_region.png in the current directory.

Option B — Run notebook

1. Start Jupyter:
jupyter notebook task4_optimization.ipynb

2. Execute cells top-to-bottom to reproduce the full analysis, visuals, and interpretation.

Results (example)
Status: Optimal
Optimal Product A: 15.0
Optimal Product B: 17.5
Maximum Profit = $ 825.0

Business Insights

The optimal solution uses machine hours fully; labor is not fully utilized. Machine time is the binding constraint (bottleneck).

If integer (whole unit) production is required, use Integer Linear Programming — the optimal integer solution may differ.

Sensitivity (shadow price) analysis can quantify the value of acquiring extra machine hours.

Extensions

Add demand constraints (upper bounds) to reflect market limits.

Introduce fixed costs / setup decisions (binary variables -> MILP).

Perform sensitivity analysis to compute dual prices and guide investment decisions.
