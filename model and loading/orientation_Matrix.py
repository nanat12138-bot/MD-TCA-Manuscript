xa=4
xb=-3
xc=0
x=(xa**2+xb**2+xc**2)**(1/2)
x1=xa/x
x2=xb/x
x3=xc/x

ya=3
yb=4
yc=-5
y=(ya**2+yb**2+yc**2)**(1/2)
y1=ya/y
y2=yb/y
y3=yc/y

za=3
zb=4
zc=5
z=(za**2+zb**2+zc**2)**(1/2)
z1=za/z
z2=zb/z
z3=zc/z


import numpy as np
X = np.array([x1, x2, x3], dtype=float)   
Y = np.array([y1, y2, y3], dtype=float)   
Z = np.array([z1, z2, z3], dtype=float)  

M = np.column_stack((X, Y, Z))
n = [1,1,1]
N = M @ n 


print(M,"\n\n--",N)