def modinv(a, m):
    cdef:
        string a_string = str(a).encode()
        string m_string = str(m).encode()
        string retval
    retval = modinv_cpp(a_string, m_string)
    return int(retval.decode())%m