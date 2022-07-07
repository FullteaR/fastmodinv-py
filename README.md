# fastmodinv-py
Calculate Inverse Element.
## requirements
- boost
- python

(Windows not supported?)

## install
```
pip install git+https://github.com/FullteaR/fastmodinv-py.git
```

## usage

```usage.py
import modinv
print(modinv.modinv(31, 100))
# >> 71
# 71*31 mod 100 = 1
```