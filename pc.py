#!/usr/bin/env python
# -*- coding:utf-8 -*-

user = "熊飞"
for ct in user:
    print(ct)
    bt = bytes(ct,encoding='utf8')
    print(bt)
    for c in bt:
        print(c)
    s1 = str(bt,encoding="utf8")
    print(s1)