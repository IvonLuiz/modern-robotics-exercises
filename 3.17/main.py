import numpy as np
import os
import matplotlib.pyplot as plt

def plot_frame(origin, mat, ax, color="black", frame_name=""):
    x = mat[0]
    y = mat[1]
    z = mat[2]
    
    ax.quiver(*origin, *x, color=color, length=1, normalize=True)
    ax.quiver(*origin, *y, color=color, length=1, normalize=True)
    ax.quiver(*origin, *z, color=color, length=1, normalize=True)

    ax.text(*(origin + x), 'x' + frame_name, color=color)
    ax.text(*(origin + y), 'y' + frame_name, color=color)
    ax.text(*(origin + z), 'z' + frame_name, color=color)
    
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

# The fixed frame {a} lies on origin
a_origin = np.array([0, 0, 0])
Ra = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

# The workpiece frame {d} on image lies one unit to the x axis and one unit to the y axis from {a}
d_origin = np.array([-1, 1, 0])
Rd = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

# The camera frrame {c} lies two units above z axis of {d}
c_origin = d_origin + np.array([0, 0, 2])
# Camera frame is rotated 90 degrees around z axis of {a} followed by inversion of z axis
Rc = np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])

## a)
Tad = np.identity(4)
Tad[:3, :3] = np.dot(Rd, Ra.T)
Tad[:3, 3] = d_origin 

print("Tad: \n", Tad)

# Calculate the rotation matrix Rcd
Rcd = Rc @ Rd.T
# Calculate the translation vector pcd
pcd = c_origin - Rcd @ d_origin

Tcd = np.identity(4)
Tcd[:3, :3] = Rcd
Tcd[:3, 3] = pcd
print("Tcd: \n", Tcd)

## b)
Tbc = np.array([
    [1, 0, 0, 4],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

Tac = Tad @ np.linalg.inv(Tcd)
Tab = Tac @ np.linalg.inv(Tbc)

print("Tab: \n", Tab)

b_origin = Tab[:3, 3]
Rb = Tab[:3, :3]

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plot_frame(a_origin, Ra, ax, frame_name="a")
plot_frame(d_origin, Rd, ax, frame_name="d")
plot_frame(c_origin, Rc, ax, frame_name="c")
plot_frame(b_origin, Rb, ax, frame_name="b")

ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Adjust the view to look just like figure from exercise
ax.view_init(30, 30)

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'diagram.png')
plt.savefig(image_path)
