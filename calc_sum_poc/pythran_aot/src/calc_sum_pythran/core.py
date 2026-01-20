from __future__ import annotations

import numpy as np

from .impl import core


def calc_sum(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Public API.

    This wrapper enforces float64 1D contiguous inputs for the PoC.
    The implementation lives in the compiled extension (`_core*.so`).
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
    return core.calc_sum(a, b)
