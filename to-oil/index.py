#!/usr/bin/python3

import tkinter as tk
from oilCost import OilCost, oilTypeList, oilTypePrice

oilType = oilTypeList[0]
oilNum = 0
isDiscount = False
sumMoney = 0


oilCostClass = OilCost()

def toSumMoney():
    sumMoney = oilCostClass.toSumMoney(oilType, oilNum, isDiscount)
    print(sumMoney)

root_window = tk.Tk()

root_window.title('加油计费')

root_window.geometry('600x400+500+200')

root_window.minsize(600, 400)
root_window.maxsize(600, 400)

top_title = oilCostClass.getOilTxt(oilType) + ':' + oilCostClass.getOilMoneyTxt(oilType)
tk.Label(root_window, text=top_title).grid(row=3)

tk.Label(root_window, text='种类', width=10,).grid(row=6, column=2)
tk.Label(root_window, text='数量：升', width=10,).grid(row=6, column=3)



# v = tk.IntVar()

oilTypePriceKey = list(oilTypePrice.keys())
print(len(oilTypePriceKey))

for index in len(oilTypePriceKey):
    type = oilTypePriceKey[index]
    txtName = oilCostClass.getOilTxt(type)
    row = 6 + index*2
    tk.Label(root_window, text=txtName, width=10, compound=toSumMoney).grid(row=row, column=2)

tk.Button(root_window, text="计算", width=10, command=toSumMoney).grid(row=20, column=2)
tk.Button(root_window, text="退出", width=10, command=root_window.quit).grid(row=20, column=3)


root_window.mainloop()