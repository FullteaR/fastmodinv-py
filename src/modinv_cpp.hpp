#ifndef MODINV_HPP
#define MODINV_HPP

#include <boost/multiprecision/cpp_int.hpp>
#include <tuple>
using Bint = boost::multiprecision::cpp_int;

std::tuple<Bint, Bint, Bint> xgcd(Bint a, Bint b);
std::string modinv_cpp(std::string a, std::string m);

#endif // MODINV_HPP