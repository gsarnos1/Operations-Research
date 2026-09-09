import numpy as np
from scipy.optimize import linprog

# 1. Define the objective function coefficients
# We want to minimize 30(A1+A2+A3) + 28(B1+B2+B3) +.9(I1+I2) + .75(J1+J2)
c = [30, 30, 30, 28, 28, 28, 0.9, 0.9, 0.75, 0.75]

# 2. Define the inequality constraints (A_ub * [x, y] <= b_ub)
A = [
    [0.75, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0.75, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0.75, 0, 0, 1, 0, 0, 0, 0],
]

b = [3000, 3500, 3000]

#3 Define the equality constraints
Aeq = [
    [1, 0, 0, 0, 0, 0, -1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, -1, 0],
    [0, 1, 0, 0, 0, 0, 1, -1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, -1],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
]

beq = [500, 1000, 5000, 1200, 750, 1200]

# 4. Define the bounds for x and y (x >= 0, y >= 0)
# x_bounds = (0, None)  # None means infinity
# y_bounds = (0, None)

# 5. Solve the linear programming problem
# We use the recommended 'highs' method for modern, fast execution
res = linprog(c, A_ub=A, b_ub=b, A_eq = Aeq, b_eq = beq, method='highs')

# 6. Display the results
if res.success:
    print("Optimization successful!")
    print(f"Optimal value for A1: {res.x[0]:.2f}")
    print(f"Optimal value for A2: {res.x[1]:.2f}")
    print(f"Optimal value for A3: {res.x[2]:.2f}")
    print(f"Optimal value for B1: {res.x[3]:.2f}")
    print(f"Optimal value for B2: {res.x[4]:.2f}")
    print(f"Optimal value for B3: {res.x[5]:.2f}")
    print(f"Optimal value for I1: {res.x[6]:.2f}")
    print(f"Optimal value for I2: {res.x[7]:.2f}")
    print(f"Optimal value for J1: {res.x[8]:.2f}")
    print(f"Optimal value for J2: {res.x[9]:.2f}")
    print(f"Minimum value of the objective function: {res.fun:.2f}")
else:
    print("Optimization failed:", res.message)