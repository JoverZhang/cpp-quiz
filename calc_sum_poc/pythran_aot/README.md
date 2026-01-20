# calc-sum-pythran

Pythran AOT (ahead-of-time) implementation of `calc_sum(a, b) -> a + b`.

This variant builds a binary extension and then assembles a runnable `output/` tree.
The goal is to ship `output/` (including the `.so`) without shipping the Python implementation source
(`src/calc_sum_pythran/_core_impl.py`).

## Commands

```bash
uv sync
just build
just bench
```

## Portability notes

`output/` contains a platform-specific binary (`_core*.so`). To run on another machine, it must be compatible with:

- OS/arch/libc (e.g. manylinux vs musllinux, x86_64 vs aarch64)
- Python version/ABI

If in doubt, rebuild on the target machine.
