import numpy as np
import matplotlib.pyplot as plt


p1 = np.array([np.sqrt(2), 0, 2])
p1_prime = np.array([0, 2, np.sqrt(2)])

# Find rotation matrix R so p'i = R pi

# formula: u = V × W / ∥V × W∥
# cos(ϕ) = V⋅W
# sin(ϕ) = ∥V×W∥
u = np.cross(p1, p1_prime) / np.linalg.norm(np.cross(p1, p1_prime))

cosTheta = p1 @ p1_prime / (np.linalg.norm(p1) * np.linalg.norm(p1_prime))
sinTheta = np.linalg.norm(np.cross(p1, p1_prime)) / (np.linalg.norm(p1) * np.linalg.norm(p1_prime))

print(u)
print(cosTheta)
print(sinTheta)

# ϕ = Atan2(cos(ϕ),sin(ϕ))
theta = np.arctan2(sinTheta, cosTheta)
print(np.rad2deg(theta))

# R(u, ϕ) = u . u^T + (I − u . u^T) cos(ϕ) + Su . sin(ϕ)
ux = u[0]
uy = u[1]
uz = u[2]
Su = np.array([[0,      -uz,    uy],
              [uz,      0,      -ux],
              [-uy,     ux,     0]])
I = np.identity(3)
phi = theta
R = np.outer(u, u) + (I - np.outer(u, u)) * np.cos(phi) + Su * np.sin(phi)


print(R)
print(R @ p1)
print(p1_prime)
print(R.T @ R)