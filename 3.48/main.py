import numpy as np
import os
import matplotlib.pyplot as plt

class RigidBodyTransformation:
    def __init__(self, T, screw, d_theta):
        """
        Constructor

        """
        self.T = T                      # initial configuration of a rigid body T
        self.q, self.s, self.h = screw  # screw axis {q, s, h} in fixed frame {s}
        self.d_theta = d_theta          # total distance traveled along the screw axis
    

    def skew_symmetric(self, v):
        """
        Returns the skew-symmetric matrix of a vector v.
        """
        return np.array([
            [0, -v[2], v[1]],
            [v[2], 0, -v[0]],
            [v[0], v[1], 0]
        ])

    def matrix_exp6(self, S, theta):
        """
        Computes the matrix exponential of a 6x1 twist vector S.
        """
        w = S[:3]
        v = S[3:]
        w_hat = self.skew_symmetric(w)
        I = np.eye(3)
        
        # Using Rodrigues rotation formula
        R = I + np.sin(theta) * w_hat + (1 - np.cos(theta)) * (w_hat @ w_hat)
        p = (I * theta + (1 - np.cos(theta)) * w_hat + (theta - np.sin(theta)) * (w_hat @ w_hat)) @ v
        
        # Logic to return homogeneous matrix
        return np.vstack((np.hstack((R, p.reshape(3, 1))), np.array([0, 0, 0, 1])))

    def compute_transformation(self, theta):
        """
        Computes the final configuration of the rigid body.
        """
        S = np.hstack((self.s, np.cross(-self.s, self.q) + self.h * self.s))
        eS = self.matrix_exp6(S, theta)
        T1 = eS @ self.T
        
        return T1

    def compute_intermidate_transformations(self):
        """
        Computes the intermediate transformations of the rigid body.
        """
        T1_4 = self.compute_transformation(self.d_theta / 4)
        T1_2 = self.compute_transformation(self.d_theta / 2)
        T3_4 = self.compute_transformation(3 * self.d_theta / 4)
        T = self.compute_transformation(self.d_theta)
        
        return [T1_4, T1_2, T3_4, T]
    
    def plot_frame(self, T, ax, color="black", frame_name=""):
        """
        Plots the frame represented by the transformation matrix T.
        """
        origin = T[:3, 3]
        R = T[:3, :3]
        x = R[:, 0]
        y = R[:, 1]
        z = R[:, 2]
        
        ax.quiver(*origin, *x, color=color, length=1, normalize=True)
        ax.quiver(*origin, *y, color=color, length=1, normalize=True)
        ax.quiver(*origin, *z, color=color, length=1, normalize=True)

        ax.text(*(origin + x), 'x' + frame_name, color=color)
        ax.text(*(origin + y), 'y' + frame_name, color=color)
        ax.text(*(origin + z), 'z' + frame_name, color=color)
        

    def plot_transformations(self):
        """
        Plots the initial, intermediate, and final configurations of the rigid body.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        T1_4, T1_2, T3_4, T1 = self.compute_intermidate_transformations()
        
        # Plot initial, intermidiate and final configurations
        self.plot_frame(self.T, ax, color="blue", frame_name="0")
        self.plot_frame(T1_4, ax, color="black", frame_name="1/4")
        self.plot_frame(T1_2, ax, color="black", frame_name="1/2")
        self.plot_frame(T3_4, ax, color="black", frame_name="3/4")
        self.plot_frame(T1, ax, color="red", frame_name="1")


        # Saving plot
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, 'transformations.png')
        
        plt.savefig(image_path)
        print('Transformations saved to:', image_path)

        return T1


if __name__ == "__main__":
    T = np.array([[1, 0, 0, 2],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])
    q = np.array([0, 2, 0])
    s = np.array([0, 0, 1])
    h = 2
    theta = np.pi

    # Print initial conditions
    print("Initial configuration T:")
    print(T)
    print("\nScrew axis {q, s, h}:")
    print(f"q: {q}")
    print(f"s: {s}")
    print(f"h: {h}")
    print(f"Total distance traveled along the screw axis (theta): {theta}")

    rigid_body = RigidBodyTransformation(T, (q, s, h), theta)
    
    final_T = rigid_body.plot_transformations()
    
    print("Final configuration T1: \n", np.round(final_T, 2))
