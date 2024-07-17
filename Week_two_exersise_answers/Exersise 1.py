import numpy as np

v = np.array([2., 2., 4.])

# Extract the components corresponding to each axis
projection_e0 = v[0]  # projection onto e0 axis
projection_e1 = v[1]  # projection onto e1 axis
projection_e2 = v[2]  # projection onto e2 axis

print(f"Projection onto e0: {projection_e0}")
print(f"Projection onto e1: {projection_e1}")
print(f"Projection onto e2: {projection_e2}")