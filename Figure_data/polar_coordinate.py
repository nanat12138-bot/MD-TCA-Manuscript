import numpy as np

def crystal_to_pole_figure(h, k, l):
    # normalize the Miller indices
    vec = np.array([h, k, l], dtype=float)
    norm = np.linalg.norm(vec)
    u, v, w = vec / norm

    # θ and r
    theta = np.arccos(w)
    r = np.tan(theta / 2)

    # calculate
    if np.sqrt(u**2 + v**2) < 1e-8:
        x, y = 0.0, 0.0
    else:
        x = r * u / np.sqrt(u**2 + v**2)
        y = r * v / np.sqrt(u**2 + v**2)

    return x, y


# change here~
y, x = crystal_to_pole_figure(0, 1, 2)
print(f"在极图中的坐标为: x = {x:.6f}, y = {y:.6f}")