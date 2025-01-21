import numpy as np

class RigidBodyTransformation:
    def __init__(self, T, screw, d_theta):
        """
        Constructor
        One representation of a screw axis
        S is the collection {q, s, h ˆ }, where q 2 R3 is any point on the axis, ˆs is a unit
        vector in the direction of the axis, and h is the screw pitch, which defines the
        ratio of the linear velocity along the screw axis to the angular velocity ˙
        ✓ about the screw axis
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
        
        R = I + np.sin(theta) * w_hat + (1 - np.cos(theta)) * (w_hat @ w_hat)
        p = (I * theta + (1 - np.cos(theta)) * w_hat + (theta - np.sin(theta)) * (w_hat @ w_hat)) @ v
        
        return np.vstack((np.hstack((R, p.reshape(3, 1))), np.array([0, 0, 0, 1])))

    def compute_transformation(self):
        """
        Computes the final configuration of the rigid body.
        """
        S = np.hstack((self.s, np.cross(-self.s, self.q) + self.h * self.s))
        print(S)
        eS = self.matrix_exp6(S, self.d_theta)
        T1 = eS @ self.T
        
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

    rigid_body = RigidBodyTransformation(T, (q, s, h), theta)
    final_T = rigid_body.final_configuration()
    print("Final configuration T1: \n", final_T)