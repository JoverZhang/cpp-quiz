from __future__ import annotations

from setuptools import Extension, setup
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        name="calc_sum_cython._core",
        sources=["src/calc_sum_cython/_core.pyx"],
        include_dirs=[np.get_include()],
        language="c",
        extra_compile_args=["-O3"],
    )
]

setup(
    ext_modules=cythonize(
        extensions,
        compiler_directives={"language_level": "3"},
    ),
)
