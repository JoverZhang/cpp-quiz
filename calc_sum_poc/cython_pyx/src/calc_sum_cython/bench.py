from __future__ import annotations

import argparse
import time

import numpy as np

from . import calc_sum


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=5_000_000, help="vector length")
    p.add_argument("--iters", type=int, default=30, help="timed iterations")
    args = p.parse_args()

    a = np.random.rand(args.n).astype(np.float64)
    b = np.random.rand(args.n).astype(np.float64)

    # Warmup
    out = calc_sum(a, b)
    assert out.shape == a.shape

    t0 = time.perf_counter()
    for _ in range(args.iters):
        out = calc_sum(a, b)
    t1 = time.perf_counter()

    sec = t1 - t0
    gb = (a.nbytes + b.nbytes + out.nbytes) * args.iters / 1e9
    print(f"cython_pyx: n={args.n} iters={args.iters} time={sec:.4f}s  effective_bw≈{gb/sec:.2f} GB/s")


if __name__ == "__main__":
    main()
