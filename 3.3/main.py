import numpy as np
import matplotlib.pyplot as plt


p1 = np.array([np.sqrt(2), 0, 2])
p1_prime = np.array([0, 2, np.sqrt(2)])

# Find rotation matrix R so p'i = R pi

# formula: u = V × W / ∥V × W∥
# cos(ϕ) = V⋅W
# sin(ϕ) = ∥V×W∥

cosTheta = np.dot(p1, p1_prime)
sinTheta = np.linalg.norm(np.cross(p1, p1_prime))
print(cosTheta)
print(sinTheta)

# ϕ = Atan2(cos(ϕ),sin(ϕ))
theta = np.arctan2(cosTheta, sinTheta)
print(np.rad2deg(theta))