#include <iostream>

#include "sub_test_folder/sub_test_class.h"
#include "test_class.h"

int main() {
  TestClass tc;
  SubTestClass src;

  size_t ind = 5;
  for (int i = 0; i < ind; ++i) {
    std::cout << i << std::endl;
  }

  return 0;
}
