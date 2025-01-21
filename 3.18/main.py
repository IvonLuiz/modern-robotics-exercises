import numpy as np

# a)
"""
Trs = ?

Using: Tab · Tbc = Tac

Tea · Tar = Ter

Using:    T⁻¹ = [ R^T -R^T p ]
                [ 0      1   ]

Ter⁻¹ = Tre
Ter⁻¹ · Tes = Tre · Tes = Trs
"""

# b)
# To compute origin of {s} (Ose) seen from frame {r} (Osr)

# We have origin {s} seen from {e}
Oe = np.array([[1, 1, 1]]).T
print("Oe ({s} seen from {e}): \n", Oe)

# Calculate inverse of Ter
Ter = np.array([[-1,  0,  0,  1],
                [ 0,  1,  0,  1],
                [ 0,  0, -1,  1],
                [ 0,  0,  0,  1]])

def compute_reverse_transformation(T):
    R = T[:3, :3]
    p = T[:3, 3]
    T_reverse = np.identity(4)
    T_reverse[:3, :3] = R.T
    T_reverse[:3, 3] = -R.T @ p
    return T_reverse

Ter_inv = Tre = compute_reverse_transformation(Ter)
print("Tre: \n", Tre)

# Get Or
# Using: Tab · pb = pa

Oe = np.append(Oe, 1) # transform to homogeneous coordinates

Or = Tre @ Oe

Or = np.delete(Or, -1) # transforrm back to cartesian

print("Or ({s} seen from r): \n", Or)