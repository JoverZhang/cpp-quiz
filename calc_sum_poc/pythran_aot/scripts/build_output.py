from __future__ import annotations

import shutil
from pathlib import Path


def _copy_package_sources(src_pkg_dir: Path, dst_pkg_dir: Path) -> None:
    for path in src_pkg_dir.rglob("*"):
        if path.name == "__pycache__":
            continue
        if path.is_file() and path.name == "_core_impl.py":
            continue
        if path.is_file() and path.suffix in {".cpp", ".cxx", ".cc", ".o", ".obj", ".pyc"}:
            continue

        rel = path.relative_to(src_pkg_dir)
        dst = dst_pkg_dir / rel

        if path.is_dir():
            dst.mkdir(parents=True, exist_ok=True)
            continue

        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dst)


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    src_pkg_dir = project_root / "src" / "calc_sum_pythran"
    output_root = project_root / "output"
    output_pkg_dir = output_root / "calc_sum_pythran"

    if output_root.exists():
        shutil.rmtree(output_root)
    output_pkg_dir.mkdir(parents=True, exist_ok=True)

    _copy_package_sources(src_pkg_dir=src_pkg_dir, dst_pkg_dir=output_pkg_dir)

    import calc_sum_pythran._core as compiled

    compiled_path = Path(compiled.__file__).resolve()
    shutil.copy2(compiled_path, output_pkg_dir / compiled_path.name)


if __name__ == "__main__":
    main()
