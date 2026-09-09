import numpy as np
from scipy.optimize import linprog

# Documentation for linprog: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html

# We want to maximize z = 1.2(x1)+1.3(x2)+.8(x3)+.95(x4)+1.065(b4)

# Define variables as follows
# x[0] = x1, x[1] = x2, x[2] = x3
# x[3] = x4, x[4] = b1, x[5] = b2
# x[6] = b3, x[7] = b4


# 1. Define the objective function coefficients
# We want to maximize, so we minimize its negative
c = [0, 0, 0, 0, 0, 0, 0, 0, -1]

# 2 Define the inequality constraints 
Aub = [
#   x1    x2   x3   x4   b1  b2  b3  b4 b5
   [ 1,   1,   0,  1,  1,  0,  0,  0, 0],    
]

bub = [10]

#3 Define the equality constraints
Aeq = [
    [0.5, 0.6 , -1, 0.4, 1.065, -1, 0, 0, 0],
    [0.3, 0.2, 0.8, 0.6, 0, 1.065, -1, 0, 0],
    [1.8, 1.5, 1.9, 1.8, 0, 0, 1.065, -1, 0],
    [1.2, 1.3, 0.8, 0.95, 0, 0, 0, 1.065, -1]
]

beq = [0, 0, 0, 0]

# 4. Define the bounds 
x_bounds = (0, None)  # None means infinity
y_bounds = (0, None)

# 5. Solve the linear programming problem
# We use the recommended 'highs' method for modern, fast execution
res = linprog(c, A_ub=Aub, b_ub=bub, A_eq = Aeq, b_eq = beq, method='highs')

# 6. Display the results
if res.success:
    print(f"Optimal value for x1: ${res.x[0] * 1000:,.2f}")
    print(f"Optimal value for x2: ${res.x[1] * 1000:,.2f}")
    print(f"Optimal value for x3: ${res.x[2] * 1000:,.2f}")
    print(f"Optimal value for x4: ${res.x[3] * 1000:,.2f}")
    print(f"Optimal value for b1: ${res.x[4] * 1000:,.2f}")
    print(f"Optimal value for b2: ${res.x[5] * 1000:,.2f}")
    print(f"Optimal value for b3: ${res.x[6] * 1000:,.2f}")
    print(f"Optimal value for b4: ${res.x[7] * 1000:,.2f}")
    # We negate the result back to get the maximum value
    print(f"Maximum value of the objective function:  ${-res.fun * 1000:,.2f}")
else:
    print("Optimization failed:", res.message)