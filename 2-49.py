import numpy as np
from scipy.optimize import linprog

# 1. Define the objective function coefficients
# We want to maximize 30(x1)+20(x2)+50x3
# which is equivalent to minimizing its negative
c = [-30, -20, -50]

# 2. Define the inequality constraints (A_ub * [x, y] <= b_ub)
A = [
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, -1],
    [2, 3, 5],
    [4, 2, 7],
    [1, 0.5, 0.33]
]

b = [-200, -200, -150, 4000, 6000, 1500]

#3 Define the equality constraints
Aeq = [
    [2, -3, 0],
    [0, 5, -2]
]

beq = [0, 0]

# 4. Define the bounds for x and y (x >= 0, y >= 0)
# x_bounds = (0, None)  # None means infinity
# y_bounds = (0, None)

# 5. Solve the linear programming problem
# We use the recommended 'highs' method for modern, fast execution
res = linprog(c, A_ub=A, b_ub=b, A_eq = Aeq, b_eq = beq, method='highs')

# 6. Display the results
if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x1: {res.x[0]:.2f}")
    print(f"Optimal value for x2: {res.x[1]:.2f}")
    print(f"Optimal value for x3: {res.x[2]:.2f}")
    # We negate the result back to get the maximum value
    print(f"Maximum value of the objective function: {-res.fun:.2f}")
else:
    print("Optimization failed:", res.message)