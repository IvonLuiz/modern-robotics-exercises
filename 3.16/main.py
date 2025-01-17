import numpy as np
import matplotlib.pyplot as plt
import os


xs = np.array([1, 0, 0])
ys = np.array([0, 1, 0])
zs = np.array([0, 0, 1])
origin_s = np.array([0, 0, 0])

xa = np.array([0, 0, 1])
ya = np.array([-1, 0, 0])
za = np.cross(xa, ya)
origin_a = np.array([3, 0, 0])

xb = np.array([1, 0, 0])
yb = np.array([0, 0, -1])
zb = np.cross(xb, yb)
origin_b = np.array([0, 2, 0])

# a)
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

ax.set_xlim([-1, 4])
ax.set_ylim([-1, 3])
ax.set_zlim([-1, 2])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Frames {a} and {b} relative to {s}')

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'diagram.png')

plt.savefig(image_path)

# b)
