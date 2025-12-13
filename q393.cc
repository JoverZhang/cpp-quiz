#include <iostream>

void check(int and x) { std::cout << "a"; }

void check(int bitand x) { std::cout << "b"; }

int main() { check(3); }
