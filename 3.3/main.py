import numpy as np
import matplotlib.pyplot as plt
import os


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


def checkRotationMatrix(R, p, p_prime, file):
    """
    Checks if the Rotation matrix was calculated correctly from p' = R·p.
    """
    file.write("Rotation matrix calculated: \n")
    file.write(f"{R}\n")
    
    # Check if R^T · R is identity
    identity_check = np.round(R.T @ R, 2)
    file.write("Checking if R^T · R = I:\n")
    file.write(f"{identity_check}\n")
    
    if np.allclose(identity_check, np.identity(3)):
        file.write("R^T · R is approximately the identity matrix. ✓\n")
    else:
        file.write("R^T · R is NOT the identity matrix. ✗\n")
    
    # Check if R·p is the same as p' original
    rotated_p = R @ p
    file.write("\nOriginal vector after rotation (R · p):\n")
    file.write(f"{np.round(rotated_p, 2)}\n")
    file.write("Expected transformed vector (p'):\n")
    file.write(f"{np.round(p_prime, 2)}\n")
    
    if np.allclose(rotated_p, p_prime):
        file.write("Rotation is correct. ✓\n")
    else:
        file.write("Rotation is NOT correct. ✗\n")
    file.write("\n")


results_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results.txt')
with open(results_path, 'w') as file:
    file.write("a)\n")
    p1 =        np.array([np.sqrt(2), 0, 2])
    p1_prime =  np.array([0, 2, np.sqrt(2)])
    R = findRotationMatrix(p1, p1_prime)
    checkRotationMatrix(R, p1, p1_prime, file)

    # b)
    file.write("b)\n")
    p2 =        np.array([1, 1, -1])
    p2_prime =  np.array([1/np.sqrt(2), 1/np.sqrt(2), -np.sqrt(2)])
    R = findRotationMatrix(p2, p2_prime)
    checkRotationMatrix(R, p2, p2_prime, file)

    # c)
    file.write("c)\n")
    p3 =        np.array([np.sqrt(2), 0, 2])
    p3_prime =  np.array([0, 2, np.sqrt(2)])
    R = findRotationMatrix(p3, p3_prime)
    checkRotationMatrix(R, p3, p3_prime, file)