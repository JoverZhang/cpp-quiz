from __future__ import annotations

from setuptools import setup

from pybind11.setup_helpers import Pybind11Extension, build_ext
import numpy as np

ext_modules = [
    Pybind11Extension(
        "calc_sum_cpp._core",
        ["src/calc_sum_cpp/_core.cpp"],
        include_dirs=[np.get_include()],
        cxx_std=17,
        extra_compile_args=["-O3"],
    )
]

setup(
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
