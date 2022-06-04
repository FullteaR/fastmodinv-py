cdef extern from "modinv.cpp":
    string _modinv(string a_, string m_) nogil