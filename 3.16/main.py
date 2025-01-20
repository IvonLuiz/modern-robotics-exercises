import numpy as np
import matplotlib.pyplot as plt
import os

# {s} frame
xs = np.array([1, 0, 0])
ys = np.array([0, 1, 0])
zs = np.array([0, 0, 1])
origin_s = np.array([0, 0, 0])

# {a} frame
xa = np.array([0, 0, 1])
ya = np.array([-1, 0, 0])
za = np.cross(xa, ya)
origin_a = np.array([3, 0, 0])

# {b} frame
xb = np.array([1, 0, 0])
yb = np.array([0, 0, -1])
zb = np.cross(xb, yb)
origin_b = np.array([0, 2, 0])

## a)
# Plot diagram showing {a} and {b} relative to {s}
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def plot_frame(origin, x, y, z, color="black", frame_name="", ax=ax):
    ax.quiver(*origin, *x, color=color, length=1, normalize=True)
    ax.quiver(*origin, *y, color=color, length=1, normalize=True)
    ax.quiver(*origin, *z, color=color, length=1, normalize=True)

    ax.text(*(origin + x), 'x' + frame_name, color=color)
    ax.text(*(origin + y), 'y' + frame_name, color=color)
    ax.text(*(origin + z), 'z' + frame_name, color=color)

# Plot {s} frame
plot_frame(origin_s, xs, ys, zs, 'black', 's')

# Plot frame {a}
plot_frame(origin_a, xa, ya, za, 'darkred', 'a')

# Plot frame {b}
plot_frame(origin_b, xb, yb, zb, 'darkblue', 'b')

ax.set_xlim([-1, 5])
ax.set_ylim([-3, 3])
ax.set_zlim([-1, 5])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Frames {a} and {b} relative to {s}')

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'diagram.png')

plt.savefig(image_path)

print('a)')
print('Diagram saved to:', image_path)


## b)
# Calculate rotation matrices Rsa and Rsb

print('b)')

Rsa = np.array([xa, ya, za]).T
Rsb = np.array([xb, yb, zb]).T
print("Rsa: \n", Rsa)
print("Rsb: \n", Rsb)

# Calculate transformation matrices Tsa and Tsb
# homogeneous transformation matrices in R3:
# T = [ R p ]
#     [ 0 1 ]

Tsa = np.identity(4)
Tsa[:3, :3] = Rsa
Tsa[:3, 3] = origin_a
print("Tsa: \n", Tsa)

Tsb = np.identity(4)
Tsb[:3, :3] = Rsb
Tsb[:3, 3] = origin_b
print("Tsb: \n", Tsb)


## c)
# Calculating the inverse of Tsb without inversing matrix
print('c)')

# Proposition 3.15. The inverse of a transformation matrix T 2 SE(3) is also 
# a transformation matrix, and it has the following form:
# T = [ R p ]⁻¹ = [ R^T -R^T · p ]
#     [ 0 1 ]     [  0      1    ]

def compute_reverse_transformation(T):
    R = T[:3, :3]
    p = T[:3, 3]
    T_reverse = np.identity(4)
    T_reverse[:3, :3] = R.T
    T_reverse[:3, 3] = -R.T @ p
    return T_reverse

Tsb_inv = compute_reverse_transformation(Tsb)
print("Inverse transformation matrix Tsb: \n", Tsb_inv)

# Plotting the inverse to check if it is correct
origin_b_inv = Tsb_inv[:3, 3]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-1, 5])
ax.set_ylim([-3, 3])
ax.set_zlim([-1, 5])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plot_frame(origin_b, xb, yb, zb, 'darkblue', 'b', ax=ax)
plot_frame(origin_b_inv, Tsb_inv[:3, 0], Tsb_inv[:3, 1], Tsb_inv[:3, 2], 'red', 'b_inv', ax=ax)
image_path = os.path.join(current_dir, 'diagram_with_inverse.png')
plt.savefig(image_path)
print('Diagram saved to:', image_path)

## d)
print('d)')
# Tab = ?
# Changing the reference frame of a vector or a frame. By a subscript
# cancellation rule analogous to that for rotations, for any three reference frames
# {a}, {b}, and {c}, and any vector v expressed in {b} as vb,
# Tab · Tbc = Tac
# Tab · vb = va

# We have Tsb and Tsa, we want Tab, so we use the inverse of Tsa which is equivalent to Tas
# Tab = Tsa⁻¹ · Tsb = Tas · Tsb = Tab
Tsa_inv = compute_reverse_transformation(Tsa)

Tab = Tsa_inv @ Tsb
print("Tab: \n", Tab)

# Plotting the transformation matrix Tab to check if it is correct
origin_ab = Tab[:3, 3]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([0, 4])
ax.set_ylim([-2, 2])
ax.set_zlim([-1, 3])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plot_frame(origin_a, xa, ya, za, 'darkblue', 'a', ax=ax)
plot_frame(origin_b, xb, yb, zb, 'darkblue', 'b', ax=ax)
plot_frame(origin_ab, Tab[:3, 0], Tab[:3, 1], Tab[:3, 2], 'red', 'b_inv', ax=ax)

image_path = os.path.join(current_dir, 'diagram_ab.png')
plt.savefig(image_path)
print('Diagram saved to:', image_path)


## e)
print('e)')

# Whether we pre-multiply or post-multiply Tsb by T = (R, p) determines
# whether the ŵ-axis and p are interpreted as in the fixed frame {s} or in the
# body frame {a}:

# Post-multiplying corresponding to a body frame transformation of Tsa
# here we are rotating and translating the body frame {a} to the fixed frame {s}
T = Tsb
T1 = Tsa @ T
print('T1: \n', T1)
print('Post-multiplying corresponding to a body frame transformation of Tsa, we are rotating and translating the body frame {a} to the fixed frame {s}.')

# Pre-multiplying corresponding to a fixed frame transformation of Tsa
# here we are rotating and translating the fixed frame {s} to the body frame {a}
T2 = T @ Tsa
print('T2: \n', T2)
print('Pre-multiplying corresponding to a fixed frame transformation of Tsa, we are rotating and translating the fixed frame {s} to the body frame {a}.')


## f)
print('f)')

pb = np.array([1, 2, 3]) # point in {b} coordinates
pb_homogeneous = np.append(pb, 1)
ps_homogeneous = Tsb @ pb_homogeneous
ps = ps_homogeneous[:3]

print("Point pb in {b} coordinates: ", pb[:3])
print("Point ps in {s} coordinates: ", ps[:3])


## g)
ps = np.array([1, 2, 3]) # point in {s} coordinates
ps_homogeneous = np.append(ps, 1)

p_prime = Tsb @ ps_homogeneous
pb_double_prime = Tsb_inv @ ps_homogeneous

print("Point ps in {s} coordinates: ", ps[:3])
print("Point p' in {b} coordinates: ", p_prime[:3])
print("Point p'' in {b} coordinates: ", pb_double_prime[:3])

print("Interpretation:")
print("p' should be interpreted as changing coordinates from the {s} frame to the {b} frame without moving the point p.")
print("p'' should be interpreted as changing coordinates from the {s} frame to the {b} frame without moving the point p.")
