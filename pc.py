#!/usr/bin/env python
# -*- coding:utf-8 -*-

s = "风朝"

for i in s:
    b = bytes(i,encoding='utf-8')
    print(b)
    s1 = str(b,encoding='utf-8')
    print(s1)