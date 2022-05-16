#!/usr/bin/env python3

flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽"
flag = list(flag)


dec = ""

for i in range(len(flag)):
    a = ord(flag[i]) >> 8
    b = ord(flag[i]) % 128
    print(chr(a), a)
    print(chr(b), b)
    dec += chr(a)
    dec += chr(b)

print(dec)
