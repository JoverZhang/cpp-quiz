# calc_sum PoC: Cython (.pyx) vs C++ (pybind11) vs Numba (JIT + disk cache) vs Pythran (AOT)

This PoC contains independent projects (separate `pyproject.toml`, separate dependency resolution via `uv`).

All three expose the same public API:

```python
import numpy as np

def calc_sum(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a + b
```

## Projects

- `cython_pyx/`  — Cython extension module built from `.pyx`.
- `cpp_pybind/`  — C++ extension module built with `pybind11`.
- `numba_jit/`   — Pure Python + Numba JIT with on-disk cache.
- `pythran_aot/` — Pythran AOT extension, with a runnable `output/` tree.

## Quickstart

Each project can be run independently.

Example (Cython):

```bash
cd cython_pyx
uv sync
just build
just bench
```

There is also a top-level `justfile` to run all benchmarks.
