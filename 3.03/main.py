import numpy as np
import matplotlib.pyplot as plt
import os


#def findRotationMatrix(p, p_prime):
#    """
#    Find rotation matrix R so p' = R * p
#    R = p * p'⁻¹
#    """
#    
#    # formula: u = V × W / ∥V × W∥
#    # cos(ϕ) = V⋅W
#    # sin(ϕ) = ∥V×W∥
#    u = np.cross(p, p_prime) / np.linalg.norm(np.cross(p, p_prime))
#
#    cos_phi = p @ p_prime / (np.linalg.norm(p) * np.linalg.norm(p_prime))
#    sin_phi = np.linalg.norm(np.cross(p, p_prime)) / (np.linalg.norm(p) * np.linalg.norm(p_prime))
#
#    #print(u)
#    #print(cos_phi)
#    #print(sin_phi)
#
#    # ϕ = Atan2(cos(ϕ),sin(ϕ))
#    phi = np.arctan2(sin_phi, cos_phi)
#    #print(np.rad2deg(phi))
#
#    # Rodrigues' Rotation matrix formula
#    # R(u, ϕ) = u . u^T + (I − u . u^T) cos(ϕ) + Su . sin(ϕ)
#    I = np.identity(3)
#    ux = u[0]
#    uy = u[1]
#    uz = u[2]
#    Su = np.array([[0,      -uz,    uy],
#                   [uz,     0,      -ux],
#                   [-uy,    ux,     0]])
#
#    R = np.outer(u, u) + (I - np.outer(u, u)) * np.cos(phi) + Su * np.sin(phi)
#
#    return R

def findRotationMatrix(p, p_prime):
    """
    Find rotation matrix R so p' = R * p
    R = p⁻¹ * p'
    """

    p_inv = np.linalg.inv(p)
    R = p_prime @ p_inv
    
    return R
    

def checkRotationMatrix(R, p, p_prime):
    """
    Checks if the Rotation matrix was calculated correctly from p' = R·p.
    """
    print("Rotation matrix calculated: \n")
    print(f"{np.round(R, 2)}\n\n")
    
    # Check if R^T · R is identity
    identity_check = np.round(R.T @ R, 2)
    print("Checking if R^T · R = I:\n")
    print(f"{identity_check}\n")
    
    if np.allclose(identity_check, np.identity(3)):
        print("R^T · R is approximately the identity matrix. ✓\n")
    else:
        print("R^T · R is NOT the identity matrix. ✗\n")
    
    # Check if R·p is the same as p' original
    rotated_p = R @ p
    print("\nOriginal vector after rotation (R · p):\n")
    print(f"{np.round(rotated_p, 2)}\n")
    print("Expected transformed vector (p'):\n")
    print(f"{np.round(p_prime, 2)}\n")
    
    if np.allclose(rotated_p, p_prime):
        print("Rotation is correct. ✓\n")
    else:
        print("Rotation is NOT correct. ✗\n")



print("Initial points: ")
p1 =        np.array([np.sqrt(2), 0, 2])
p2 =        np.array([1, 1, -1])
p3 =        np.array([0, 2*np.sqrt(2), 0])

p1_prime =  np.array([0, 2, np.sqrt(2)])
p2_prime =  np.array([1/np.sqrt(2), 1/np.sqrt(2), -np.sqrt(2)])
p3_prime =  np.array([-np.sqrt(2), np.sqrt(2), -2])

p = np.array([p1, p2, p3]).T
print("Matrices of points: \n", np.round(p, 2))

p_prime = np.array([p1_prime, p2_prime, p3_prime]).T
print("Matrices of points after rotation: \n", np.round(p_prime, 2), "\n")

R = findRotationMatrix(p, p_prime)
checkRotationMatrix(R, p1, p1_prime)