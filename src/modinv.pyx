def modinv(a, m):
    retval = _modinv(str(a).encode(), str(m).encode())
    return int(retval.decode())