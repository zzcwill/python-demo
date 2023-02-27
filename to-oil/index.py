#!/usr/bin/python3
import tkinter as tk
from oilCost import OilCost, oilTypeList, oilTypePrice

oilType = oilTypeList[0]
oilNum = 0
isDiscount = 0
sumMoney = 0

oilCostClass = OilCost()

page = tk.Tk()

page.title('加油计费')

page.geometry('600x400+500+200')

page.minsize(600, 400)
page.maxsize(600, 400)

top_title = oilCostClass.getOilTxt(oilType) + ':' + oilCostClass.getOilMoneyTxt(oilType)
tk.Label(page, text=top_title).grid(row=4, column=1)

tk.Label(page, text='种类', width=10).grid(row=6, column=2)
tk.Label(page, text='', width=10).grid(row=6, column=3)
tk.Label(page, text='数量：升', width=10).grid(row=6, column=4)

vRadio = tk.IntVar()
vRadio.set(oilType)
for index, item in enumerate(oilTypePrice.keys()):
    txtName = oilCostClass.getOilTxt(item)
    row = 12 + index
    tk.Radiobutton(page, text=txtName, width=10, variable=vRadio, value=item).grid(row=row, column=2)


vCheck = tk.IntVar()
vCheck.set(isDiscount)
discountName = oilCostClass.getOilDiscountTxt()
check1 = tk.Checkbutton(page, text=discountName ,onvalue=1, offvalue=0, variable=vCheck).grid(row=13, column=3)


vInput1 = tk.IntVar()
vInput2 = tk.IntVar()
vInput1.set(oilNum)
vInput2.set(sumMoney)
def toSumMoney():
    global oilType, isDiscount, oilNum, sumMoney
    oilType = vRadio.get()
    isDiscount = vCheck.get()
    oilNum = vInput1.get()
    sumMoney = oilCostClass.toSumMoney(oilType, oilNum, isDiscount)
    vInput2.set(sumMoney)

tk.Entry(page, width=10, textvariable=vInput1).grid(row=12, column=4)
tk.Label(page, text='总价:', width=10).grid(row=13, column=4)
tk.Entry(page, textvariable=vInput2, width=10).grid(row=14, column=4)

tk.Button(page, text="计算", width=10, command=toSumMoney).grid(row=20, column=2)
tk.Label(page, text='', width=10).grid(row=20, column=3)
tk.Button(page, text="退出", width=10, command=page.quit).grid(row=20, column=4)

page.mainloop()