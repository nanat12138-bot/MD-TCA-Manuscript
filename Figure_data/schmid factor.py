import numpy as np

# loding direction
#[001][011][111][012][125][345][123][122][112]
load_dir = np.array([3,4,5], dtype=float)

# slice direction
#perfect[0,-1,1][1,0,-1][-1,1,0]; [1,0,1][1,1,0][0,-1,1];
#       [0,1,1][1,1,0][1,0,-1]; [0,1,1][1,0,1][-1,1,0]
#Shocckley[1,1,-2][-2,1,1][1,-2,1]; [-1,1,-2][2,1,1][-1,-2,1];
#         [1,-1,-2][-2,-1,1][1,2,1]; [1,1,2][1,-2,-1][-2,1,-1]
slip_dir = np.array([2,-1,1], dtype=float)

# slice plane
#[1,1,1], [-1,1,1], [1,-1,1], [1,1,-1]
plane = np.array([1,1,-1], dtype=float)


def norm(v):
    return np.linalg.norm(v)

def cos_angle(v1, v2):
    return np.dot(v1, v2) / (norm(v1) * norm(v2))

normal = plane  

cos_lambda = cos_angle(load_dir, slip_dir)

cos_phi = cos_angle(load_dir, normal)

schmid = abs(cos_phi * cos_lambda)



print(f"Schmid factor = {schmid:.4f}")