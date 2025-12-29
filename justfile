set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

CXX := `which clang++`
CXXFLAGS := `tr '\n' ' ' < compile_flags.txt`

run src:
  mkdir -p build
  mkdir -p build/containers
  {{CXX}} {{CXXFLAGS}} {{src}} -o build/{{trim_end_match(src, ".cc")}}
  ./build/{{trim_end_match(src, ".cc")}}
  echo "$?"

clean:
  rm -rf build

