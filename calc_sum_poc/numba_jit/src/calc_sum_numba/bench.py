from __future__ import annotations

import argparse
import os
import time

import numpy as np

from . import calc_sum


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=5_000_000, help="vector length")
    p.add_argument("--iters", type=int, default=30, help="timed iterations")
    args = p.parse_args()

    # Put cache under project dir for easy inspection
    cache_dir = os.path.abspath(os.getenv("NUMBA_CACHE_DIR", ".numba_cache"))
    os.environ["NUMBA_CACHE_DIR"] = cache_dir

    a = np.random.rand(args.n).astype(np.float64)
    b = np.random.rand(args.n).astype(np.float64)

    # Warmup triggers compilation (first run may be slow)
    out = calc_sum(a, b)
    assert out.shape == a.shape

    t0 = time.perf_counter()
    for _ in range(args.iters):
        out = calc_sum(a, b)
    t1 = time.perf_counter()

    sec = t1 - t0
    gb = (a.nbytes + b.nbytes + out.nbytes) * args.iters / 1e9
    print(f"numba_jit:  n={args.n} iters={args.iters} time={sec:.4f}s  effective_bw≈{gb/sec:.2f} GB/s")
    print(f"numba cache dir: {cache_dir}")


if __name__ == "__main__":
    main()
