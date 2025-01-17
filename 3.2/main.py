import numpy as np
from numpy import sqrt, cos, sin
import matplotlib.pyplot as plt
import os

# Fixed frame x^-y^-z^
p = np.array([1/sqrt(3), -1/sqrt(6), 1/sqrt(2)]) # original point coordenates

# a)
# Rotate 30 degrees on x-axis
theta = np.radians(30)
Rx = np.array([[1,          0,          0],
                [0, cos(theta), -sin(theta)],
                [0, sin(theta),  cos(theta)]])

pRotated = Rx @ p

# Rotate 135 degrees on y-axis
theta = np.radians(135)
Ry = np.array([[cos(theta),  0, sin(theta)],
               [0,           1,          0],
               [-sin(theta), 0, cos(theta)]])

pRotated = Ry @ pRotated

# Rotate -120 degrees on z-axis
theta = np.radians(-120)
Rz = np.array([[cos(theta), -sin(theta),    0],
               [sin(theta),  cos(theta),    0],
               [0,                    0,    1]])

pRotated = Rz @ pRotated

print("Original point: ", p)
print("Rotated point: ", pRotated)

# Calculate magnitudes to test if they are the same (both are one)
magnitude_original = np.linalg.norm(p)
magnitude_rotated = np.linalg.norm(pRotated)
print("Magnitude of original vector: ", np.round(magnitude_original, 2))
print("Magnitude of rotated vector: ", np.round(magnitude_rotated, 2))

# Plot results and save
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(p[0], [1], p[2], label="Original")
ax.scatter(pRotated[0], pRotated[1], pRotated[2], label="Rotated")

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'rotated_point.png')

plt.savefig(image_path)

# b)
# Find R so pRotated = R @ p
R = Rx @ Ry @ Rz
print("R: \n", R)