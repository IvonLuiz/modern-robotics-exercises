import numpy as np
import matplotlib.pyplot as plt


def findRotationMatrix(p, p_prime):
    """
    Find rotation matrix R so p'i = R pi
    """
    
    # formula: u = V × W / ∥V × W∥
    # cos(ϕ) = V⋅W
    # sin(ϕ) = ∥V×W∥
    u = np.cross(p, p_prime) / np.linalg.norm(np.cross(p, p_prime))

    cos_phi = p @ p_prime / (np.linalg.norm(p) * np.linalg.norm(p_prime))
    sin_phi = np.linalg.norm(np.cross(p, p_prime)) / (np.linalg.norm(p) * np.linalg.norm(p_prime))

    #print(u)
    #print(cos_phi)
    #print(sin_phi)

    # ϕ = Atan2(cos(ϕ),sin(ϕ))
    phi = np.arctan2(sin_phi, cos_phi)
    #print(np.rad2deg(phi))

    # R(u, ϕ) = u . u^T + (I − u . u^T) cos(ϕ) + Su . sin(ϕ)
    I = np.identity(3)
    ux = u[0]
    uy = u[1]
    uz = u[2]
    Su = np.array([[0,      -uz,    uy],
                   [uz,     0,      -ux],
                   [-uy,    ux,     0]])

    R = np.outer(u, u) + (I - np.outer(u, u)) * np.cos(phi) + Su * np.sin(phi)

    return R

def checkRotationMatrix(R, p, p_prime):
    """
    Checks if the Rotation matrix was calculated correctly from p' = R·p.
    """
    print("Rotation matrix calculated: \n", R)
    
    # Check if R^T · R is identity
    identity_check = np.round(R.T @ R, 2)
    print("Checking if R^T · R = I:", identity_check)
    
    if np.allclose(identity_check, np.identity(3)):
        print("R^T · R is approximately the identity matrix. ✓")
    else:
        print("R^T · R is NOT the identity matrix. ✗")
    
    # Check if R·p is the same as p' original
    rotated_p = R @ p
    print("\nOriginal vector after rotation (R · p):\n", rotated_p)
    print("Expected transformed vector (p'):\n", p_prime)
    
    if np.allclose(rotated_p, p_prime):
        print("Rotation is correct. ✓")
    else:
        print("Rotation is NOT correct. ✗")
    print()


# a)
print("a)")
p1 =        np.array([np.sqrt(2), 0, 2])
p1_prime =  np.array([0, 2, np.sqrt(2)])
R = findRotationMatrix(p1, p1_prime)
checkRotationMatrix(R, p1, p1_prime)

# b)
print("b)")
p2 =        np.array([1, 1, -1])
p2_prime =  np.array([1/np.sqrt(2), 1/np.sqrt(2), -np.sqrt(2)])
R = findRotationMatrix(p2, p2_prime)
checkRotationMatrix(R, p2, p2_prime)

# c)
print("c)")
p3 =        np.array([np.sqrt(2), 0, 2])
p3_prime =  np.array([0, 2, np.sqrt(2)])
R = findRotationMatrix(p3, p3_prime)
checkRotationMatrix(R, p3, p3_prime)