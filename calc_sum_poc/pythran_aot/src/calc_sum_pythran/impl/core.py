import numpy as np

# pythran export calc_sum(float64[], float64[])
# runas calc_sum(np.array([1, 2, 3], dtype=np.float64), np.array([4, 5, 6], dtype=np.float64))
# bench a = np.array([1, 2, 3]); b = np.array([4, 5, 6]); calc_sum(a, b)


def calc_sum(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a + b
