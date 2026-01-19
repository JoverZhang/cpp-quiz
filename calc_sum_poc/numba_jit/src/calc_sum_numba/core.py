from __future__ import annotations

import numpy as np
from numba import njit


@njit(cache=True)
def _calc_sum_f64_1d(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    n = a.shape[0]
    out = np.empty(n, dtype=np.float64)
    for i in range(n):
        out[i] = a[i] + b[i]
    return out


def calc_sum(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Public API.

    This wrapper enforces float64 1D contiguous inputs for the PoC.
    Numba compiles the jitted kernel on first use and stores an on-disk cache.
    """
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    if a.ndim != 1 or b.ndim != 1:
        raise ValueError("PoC expects 1D arrays")
    if a.shape[0] != b.shape[0]:
        raise ValueError("Shape mismatch")
    if not a.flags.c_contiguous:
        a = np.ascontiguousarray(a)
    if not b.flags.c_contiguous:
        b = np.ascontiguousarray(b)
    return _calc_sum_f64_1d(a, b)
