from libcpp.string cimport string

cdef extern from "modinv_cpp.hpp":
    string modinv_cpp(string a, string m) nogil