# cython: boundscheck=False
# cython: wraparound=False
# cython: nonecheck=False
# cython: cdivision=True

from __future__ import annotations

import numpy as np
cimport numpy as cnp


def calc_sum_f64_1d(cnp.ndarray[cnp.float64_t, ndim=1, mode="c"] a,
                   cnp.ndarray[cnp.float64_t, ndim=1, mode="c"] b):
    """Add two float64 1D C-contiguous NumPy arrays."""
    cdef Py_ssize_t n = a.shape[0]
    cdef cnp.ndarray[cnp.float64_t, ndim=1] out = np.empty(n, dtype=np.float64)
    cdef Py_ssize_t i
    for i in range(n):
        out[i] = a[i] + b[i]
    return out
