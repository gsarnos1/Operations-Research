import numpy as np
from scipy.optimize import linprog

# Documentation for linprog: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html

# We want to maximize z = 1.15(x11 + x13) + 1.25(x21 + x22 + x23) + 1.20(x32 + x33) 
# - 0.1333(x11 + x21) - 0.08333(x22 + x32) - 0.09(x13 + x23 + x33)


# 1. Define the objective function coefficients
# We want to maximize, so we minimize its negative
c = [-1.01667, -1.06, -1.11667, -1.16667, -1.16, 1.11667, 1.11]

# 2 Define the inequality constraints 
Aub = [
    [4/3, 0, 4/3, 0, 0, 0, 0],   
    [0, 0, 0, 5/3, 0, 5/3, 0],  
    [0, 2, 0, 0, 2, 0, 2]    
]

bub = [400000,200000,300000]

#3 Define the equality constraints
Aeq = [
    [1, -1, 0,  0,  0, 0,  0],  
    [0,  0, 1, -1,  0, 0,  0],   
    [0,  0, 2,  0, -1, 0,  0],   
    [0,  0, 0,  0,  0, 3, -2]    
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
    print(f"Optimal amount of Drink A: {res.x[0] + res.x[1]:,.2f} lbs")
    print(f"Optimal amount of Drink B: {res.x[2] + res.x[3] + res.x[4]:,.2f} lbs")
    print(f"Optimal amount of Drink C: {res.x[5] + res.x[6]:,.2f} lbs")
    # We negate the result back to get the maximum value
    print(f"Maximum value of the objective function:  ${-res.fun * 1000:,.2f}")
else:
    print("Optimization failed:", res.message)