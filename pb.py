#!/usr/bin/env python
# -*- coding:utf-8 -*-

skill_list = ["C","Java","Python","C++"]

for k,v in enumerate(skill_list):
	print(k,v)

inp = input("your choice is: ")

print(skill_list[int(inp)])
