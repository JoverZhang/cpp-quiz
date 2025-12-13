CXX := clang++
CXXFLAGS := -g -std=c++23

SRCS := $(wildcard *.cc)

BINS := $(patsubst %.cc, build/%, $(SRCS))

all: build $(BINS)

build:
	mkdir -p build

build/%: %.cc
	$(CXX) $(CXXFLAGS) $< -o $@

run: build
	@name=$$(basename $(FILE) .cc); \
	$(CXX) $(CXXFLAGS) $(FILE) -o build/$$name; \
	./build/$$name

clean:
	rm -rf build

.PHONY: all clean build
