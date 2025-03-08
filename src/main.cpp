#include <iostream>
#include <eigen3/Eigen/Dense>

template<typename T>
T getSomthings(const T& ){
    return T{};
}

int main() {

    // Petit test Eigen
    Eigen::Matrix2d m;
    std::cout << "Somthings:\n" << getSomthings(m) << std::endl;

    return 0;
}
