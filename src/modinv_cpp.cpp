#include "modinv_cpp.hpp"

std::tuple<Bint, Bint, Bint> xgcd(Bint a, Bint b){
    Bint ZERO(0);
    Bint x0(1);
    Bint y0(0);
    Bint x1(0);
    Bint y1(1);
    Bint q;
    while(b!=ZERO){
        q = a/b;
        a = a%b;
        swap(a, b);
        x0 -= q*x1;
        swap(x0, x1);
        y0 -= q*y1;
        swap(y0, y1);
    }
    return forward_as_tuple(a,x0,y0);
}

std::string modinv_cpp(std::string a_, std::string m_){
    Bint a(a_);
    Bint m(m_);
    Bint g,x,y;
    std::tie(g,x,y) = xgcd(a, m);
    Bint retval = x%m;
    return retval.str();
}

