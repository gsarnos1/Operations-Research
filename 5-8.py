from scipy.optimize import linprog

# Variables: x11, x12, x21, x22, x23, x31, x32, x33

#Objective function
c = [12000, 18000, 30000, 10000, 8000, 20000, 25000, 12000]

# Equality constraints
A_eq = [
    # Supply constraints
    [1, 1, 0, 0, 0, 0, 0, 0],      
    [0, 0, 1, 1, 1, 0, 0, 0],      
    [0, 0, 0, 0, 0, 1, 1, 1],       

    # Demand constraints
    [1, 0, 1, 0, 0, 1, 0, 0],       
    [0, 1, 0, 1, 0, 0, 1, 0],       
    [0, 0, 0, 0, 1, 0, 0, 1]        
]

b_eq = [6, 5, 8, 4, 8, 7]

bounds = [(0, None)] * 8

result = linprog(
    c,
    A_eq=A_eq,
    b_eq=b_eq,
    bounds=bounds,
    method="highs"
)

print("Minimum transportation cost:", result.fun)

print("\nOptimal shipments:")
names = ["x11", "x12", "x21", "x22", "x23", "x31", "x32", "x33"]

for name, value in zip(names, result.x):
    print(f"{name} = {value}")