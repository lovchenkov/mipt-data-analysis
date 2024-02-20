import numpy as np


def find_nearest_points(a: np.ndarray, b: np.ndarray, k: int) -> np.ndarray:
    d = ((b[:, :, np.newaxis] - a.T[np.newaxis, :, :]) ** 2).sum(axis=1)
    return (np.argsort(d) + 1)[:, 0:k]


A = np.array([
    [0, 0],
    [1, 0],
    [2, 0]
])
B = np.array([
   [0, 1],
   [2, 1]
])
print(find_nearest_points(A, B, 2))

