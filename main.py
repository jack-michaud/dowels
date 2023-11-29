from ortools.linear_solver import pywraplp

# Create the solver
solver = pywraplp.Solver.CreateSolver("SCIP")

# Define segments and quantities in mm
#segments = [43, 86, 129, 172]
#quantities = [38, 38, 40, 15]

#0.5-20k
segments = [86, 172, 258, 344]
quantities = [38, 38, 40, 15]

# Define the kerf in inches
kerf = 1

# Variable number of dowels up to some reasonable upper limit (for the sake of the MIP model)
max_dowels = 50

# Length of the stock we plan to purchase
stock_length = 914

# Initialize variables to represent if segment i is in dowel j
x = {}
for i in range(len(segments)):
        max_count = int(stock_length / (segments[i] + kerf)) #maximum number of segment i in a single dowel
        for j in range(max_dowels):
            x[i, j] = solver.IntVar(0, max_count, f'x[{i},{j}]')

# Variables for whether each dowel is used
used = [solver.BoolVar(f"used[{j}]") for j in range(max_dowels)]

# Add constraints: each segment must be used according to the specified quantities
for i in range(len(segments)):
    solver.Add(solver.Sum([x[i, j] for j in range(max_dowels)]) == quantities[i])

# Add constraints: total length of segments in each dowel must not exceed 36 inches
for j in range(max_dowels):
    solver.Add(
        solver.Sum([x[i, j] * (segments[i] + kerf) for i in range(len(segments))])
        - kerf
        <= stock_length
    )

# Objective: minimize the number of dowels used
solver.Minimize(solver.Sum(used[j] for j in range(max_dowels)))

# Solve the problem, setting a time limit of 1 minute
solver.SetTimeLimit(60000)
solver.EnableOutput()
status = solver.Solve()

# Output results
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    for j in range(max_dowels):
        print(f"Dowel {j+1}:")
        for i in range(len(segments)):
            if x[i, j].solution_value() > 0:
                print(
                    f"  Segment {i+1} length: {segments[i]} - Quantity: {x[i, j].solution_value()}"
                )
else:
    print(f"No solution found: {status}")
