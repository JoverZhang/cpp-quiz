# calc-sum-numba

Numba JIT + disk cache implementation of `calc_sum(a, b) -> a + b`.

## Commands

```bash
uv sync
just bench
```

The first run will compile the kernel. Cached object code is stored under `NUMBA_CACHE_DIR`.
