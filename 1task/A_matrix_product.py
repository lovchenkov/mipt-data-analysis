import numpy as np


def matrix_multiplication(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return (a[:, :, np.newaxis] * b[np.newaxis, :, :]).sum(axis=1)


def test():
    a = np.array([[1, 2, 0], [0, 1, 1]])
    b = np.array([[1, 2], [1, 1], [4, 1]])
    print(matrix_multiplication(a, b))

# 1 2 0    1 2
# 0 1 1    1 1
#          4 1
#

test()

