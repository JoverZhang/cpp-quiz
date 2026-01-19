#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

#include <cstddef>

namespace py = pybind11;

// PoC: float64 1D C-contiguous only
py::array_t<double> calc_sum_f64_1d(py::array_t<double, py::array::c_style | py::array::forcecast> a,
                                   py::array_t<double, py::array::c_style | py::array::forcecast> b) {
    auto a_info = a.request();
    auto b_info = b.request();

    if (a_info.ndim != 1 || b_info.ndim != 1) {
        throw std::runtime_error("PoC expects 1D arrays");
    }
    if (a_info.shape[0] != b_info.shape[0]) {
        throw std::runtime_error("Shape mismatch");
    }

    const auto n = static_cast<std::size_t>(a_info.shape[0]);
    auto out = py::array_t<double>(n);
    auto out_info = out.request();

    const double* ap = static_cast<const double*>(a_info.ptr);
    const double* bp = static_cast<const double*>(b_info.ptr);
    double* op = static_cast<double*>(out_info.ptr);

    for (std::size_t i = 0; i < n; ++i) {
        op[i] = ap[i] + bp[i];
    }

    return out;
}

PYBIND11_MODULE(_core, m) {
    m.doc() = "calc_sum PoC (C++/pybind11)";
    m.def("calc_sum_f64_1d", &calc_sum_f64_1d, "Add two float64 1D arrays");
}
