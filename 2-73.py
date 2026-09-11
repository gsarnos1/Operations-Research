import numpy as np
from scipy.optimize import linprog

# 1. Define the objective function coefficients
# We want to maximize 35(x1)+150(x2)+200(x3)+230(x4)
# which is equivalent to minimizing its negative
c = [-35, -150, -200, -230, 0, 0]

# 2. Define the inequality constraints (A_ub * [x, y] <= b_ub)
A = [
    [-1,  0,  0,  0,  0,  0],       
    [ 0, -1,  0,  0,  0,  0],      
    [ 0,  0, -1,  0,  0,  0],      
    [ 0,  0,  0, -1,  0,  0],      
    [ 1,  0,  0,  0,  0,  0],      
    [ 0,  1,  0,  0,  1,  0],       
    [ 0,  0,  1,  0, -0.8, 1],      
    [ 0,  0,  0,  1,  0, -0.95]    
]

b = [ 0, -25, -25, -25, 400, 1200, 0, 0 ]

#3 Define the equality constraints

# 4. Define the bounds for x and y (x >= 0, y >= 0)
# x_bounds = (0, None)  # None means infinity
# y_bounds = (0, None)

# 5. Solve the linear programming problem
# We use the recommended 'highs' method for modern, fast execution
res = linprog(c, A_ub=A, b_ub=b, method='highs')

# 6. Display the results
if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x1 (Molasses): {res.x[0]:.2f} tons")
    print(f"Optimal value for x2 (Brown Sugar): {res.x[1]:.2f} tons")
    print(f"Optimal value for x3 (White Sugar): {res.x[2]:.2f} tons")
    print(f"Optimal value for x4 (Powdered Sugar): {res.x[3]:.2f} tons")
    print(f"Optimal value for y1 (Brown Sugar Processed): {res.x[4]:.2f} tons")
    print(f"Optimal value for y2 (White Sugar Processed): {res.x[5]:.2f} tons")
    # Negate the result to get the maximum profit
    print(f"Maximum weekly profit: ${-res.fun:,.2f}")
else:
    print("Optimization failed:", res.message)