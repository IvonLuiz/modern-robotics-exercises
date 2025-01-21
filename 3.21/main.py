import numpy as np
from numpy import cos, sin, pi

Tab = np.array([[0, -1,  0, -100],
                [1,  0,  0,  300],
                [0,  0,  1,  500],
                [0,  0,  0,    1]])
pa = np.array([0, 800, 0]).T

print("Tab: \n", Tab)
print("pa: \n", pa)

## a)
# Since rotation matrices are orthogonal, therefore:
# R⁻¹ = R^T

print("a)")

Rab = Tab[:3, :3]
qab = Tab[:3, 3]

def transpose_rotation(R):
    """
    Computes the transpose from a rotation matrix. The same as doing R.T
    """
    R_T = np.zeros([3, 3])
    R_T[0] = R[:, 0]
    R_T[1] = R[:, 1]
    R_T[2] = R[:, 2]
    return R_T

Rab_T = transpose_rotation(Rab)
print("Rab transpose: \n", Rab_T)

#
ra = pa - qab
print("ra: \n", ra)

print("Computing: rb = Rab.T @ ra" )


rb = Rab_T @ ra
print("rb (vector r expressed in {b}-frame coordinates): \n", rb)


# Other way of obtaining same result:
# pa = rb @ Tab
# rb = Tab @ pa

def compute_reverse_transformation(T):
    R = T[:3, :3]
    p = T[:3, 3]
    T_reverse = np.identity(4)
    T_reverse[:3, :3] = R.T
    T_reverse[:3, 3] = -R.T @ p
    return T_reverse

Tab_inv = compute_reverse_transformation(Tab)

rb2 = Tab_inv @ np.append(pa, 1)
rb2 = rb[:3]
print("rb calculated from rb = Tab @ pa: \n", rb2)

## b)
print("b)")

# Rac = Rot(x, 30॰)
# rb = Tbc @ rb

pac = pa

theta = np.deg2rad(30)

Rac = np.array([[1,           0,           0],
                [0,  cos(theta), -sin(theta)],
                [0,  sin(theta),  cos(theta)]])

Tac = np.identity(4)
Tac[:3, :3] = Rac
Tac[:3, 3] = pac
print("Tac: \n", Tac)

print("Computing Tbc = Tba @ Tac")
Tbc = Tab_inv @ Tac
print("Tbc: \n", Tbc)