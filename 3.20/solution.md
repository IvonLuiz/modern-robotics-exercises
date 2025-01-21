To find $Tca$ we need $Tab$ and $Tbc$.


### $Tab$:

To make the bicycle move on the ŷ-direction, the wheels need to be rotating on the x accordingly to $\theta$:

$$
Rx = Rot(\hat{x}, \theta) =
\begin{pmatrix}
1 & 0 & 0 \\
0 & \cos(\theta) & -\sin(\theta) \\
0 & \sin(\theta) & \cos(\theta)
\end{pmatrix}
$$

The wheels frames {a} and {b} are separated by L on the global y. They rotate together in relation to the global frame, so $Rab$ will be the identity:

$$
pb_a = 
\begin{pmatrix}
0 & 0 & L
\end{pmatrix}

\\

Rab = I_{3x3}

\\

Tab = 
\begin{pmatrix}
Rab & pb_a \\
0 & 1
\end{pmatrix}

\\

Tab =
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & L \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

### $Tbc$:

The frame {c} is at the top of the {b} frame wheel, which is 2r in the ẑ direction. It also rotates in relation to {b}, since {b} is on the center of the wheel:

$$
pc_b = 
\begin{pmatrix}
0 & 0 & 2r 
\end{pmatrix}

\\

Tbc = 
\begin{pmatrix}
R & pc_b \\
0 & 1
\end{pmatrix}

\\

Tbc =
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & \cos\theta & -\sin\theta & 2r \\
0 & \sin\theta & \cos\theta & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}.



$$

### $Tac$:

$$
Tac = Tab \cdot Tbc \\

T_{ac} =
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & \cos\theta & -\sin\theta & 2r \\
0 & \sin\theta & \cos\theta & L \\
0 & 0 & 0 & 1
\end{pmatrix}.
$$
