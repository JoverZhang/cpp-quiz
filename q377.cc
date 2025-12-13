#include <flat_map>
#include <iostream>

int main() {
  std::flat_map<int, int> map;
  std::cout << std::min(map[1], map[2]);
}
