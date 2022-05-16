#!/usr/bin/env python3

import string
k = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"

for c in k:
    if c in string.ascii_lowercase:
        n = ord(c) - ord("a")
        x = chr(ord("a") +  ((n + 13) % 26))
        print(x, end='')
    elif c in string.ascii_uppercase:
        n = ord(c) - ord("A")
        x = chr(ord("A") +  ((n + 13) % 26))
        print(x, end='')
    else:
        print(c, end='')
