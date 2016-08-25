#!/usr/bin/env python
# -*- coding:utf-8 -*-

goods = [{"name":"芯片","price":200},{"name":"耳机","price":40},{"name":"充电器","price":120},{"name":"手机","price":200}]

i = 0
while i< len(goods):
    print(i,goods[i]["name"])
    i += 1


yourBlanceS = input("请输入您的余额：")
yourBlance = int(yourBlanceS)

while yourBlance >0:
    print("目前余额：%d"%yourBlance)
    yourNo = input("请输入商品编号:")
    yourGood = goods[int(yourNo)]["name"]
    yourGoodPrice = goods[int(yourNo)]["price"]
    print("您选择的商品为：%s,价格为：%d"%(yourGood,yourGoodPrice))
    yourBlance -= yourGoodPrice

print("您的余额不足")
