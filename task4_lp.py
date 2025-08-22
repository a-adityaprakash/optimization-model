"""
task4_lp.py

Linear Programming solution for the Factory Production Optimization problem
using PuLP. This is a standalone script you can run with Python.

Produces:
 - Console output of status, optimal decision variables, and objective value
 - Saves a visualization as `feasible_region.png` in the current directory

Usage:
    python task4_lp.py
"""

import pulp
import numpy as np
import matplotlib.pyplot as plt
import os

def build_and_solve():
    # 1. Define the LP problem (maximize)
    model = pulp.LpProblem("Factory_Optimization", pulp.LpMaximize)

    # 2. Decision variables
    xA = pulp.LpVariable("Product_A", lowBound=0, cat="Continuous")
    xB = pulp.LpVariable("Product_B", lowBound=0, cat="Continuous")

    # 3. Objective: Maximize profit
    model += 20 * xA + 30 * xB, "Total_Profit"

    # 4. Constraints
    model += 2 * xA + 4 * xB <= 100, "Machine_Time"
    model += 3 * xA + 2 * xB <= 90, "Labor_Time"

    # 5. Solve (CBC solver by default)
    model.solve(pulp.PULP_CBC_CMD(msg=False))

    return model, xA, xB

def plot_feasible_region(xA_val, xB_val, out_path="feasible_region.png"):
    x = np.linspace(0, 50, 400)

    # Constraint lines (solved for xB)
    # From 2*xA + 4*xB <= 100  => xB <= (100 - 2*xA)/4
    y_machine = (100 - 2 * x) / 4
    # From 3*xA + 2*xB <= 90   => xB <= (90 - 3*xA)/2
    y_labor = (90 - 3 * x) / 2

    # Clip negative values for plotting (feasible region is xB >= 0)
    y_machine = np.maximum(y_machine, 0)
    y_labor = np.maximum(y_labor, 0)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y_machine, label="Machine time constraint: 2xA + 4xB = 100")
    plt.plot(x, y_labor, label="Labor time constraint: 3xA + 2xB = 90")
    plt.fill_between(x, np.minimum(y_machine, y_labor), 0, alpha=0.25)

    plt.plot(xA_val, xB_val, "ro", label=f"Optimal ({xA_val:.2f}, {xB_val:.2f})")
    plt.xlabel("Product A (units)")
    plt.ylabel("Product B (units)")
    plt.title("Feasible Region and Optimal Solution")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()

def main():
    model, xA, xB = build_and_solve()

    status = pulp.LpStatus[model.status]
    xA_val = pulp.value(xA)
    xB_val = pulp.value(xB)
    profit = pulp.value(model.objective)

    print("=== Factory Production Optimization (PuLP) ===")
    print("Status:", status)
    print(f"Optimal Product A: {xA_val}")
    print(f"Optimal Product B: {xB_val}")
    print(f"Maximum Profit = ${profit}")

    # Save visualization
    out_file = "feasible_region.png"
    plot_feasible_region(xA_val, xB_val, out_file)
    print(f"Feasible region plot saved to: {os.path.abspath(out_file)}")

if __name__ == "__main__":
    main()
