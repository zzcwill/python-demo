#!/usr/bin/python3

import tkinter as tk
from oilCost import OilCost, oilTypeList, oilTypePrice

oilType = oilTypeList[0]
oilNum = 0
isDiscount = False
sumMoney = 0


oilCostClass = OilCost()

root_window = tk.Tk()

root_window.title('加油计费')

root_window.geometry('600x400+500+200')

root_window.minsize(600, 400)
root_window.maxsize(600, 400)

top_title = oilCostClass.getOilTxt(oilType) + ':' + oilCostClass.getOilMoneyTxt(oilType)
tk.Label(root_window, text=top_title).grid(row=4, column=1)

tk.Label(root_window, text='种类', width=10).grid(row=6, column=2)
tk.Label(root_window, text='', width=10).grid(row=6, column=3)
tk.Label(root_window, text='数量：升', width=10).grid(row=6, column=4)



radioMain = tk.Frame(root_window)

vRadio = tk.IntVar()
vRadio.set(oilType)

def changeOilType():
    global oilType, vRadio
    oilType = vRadio.get()
    print(oilType)

for index, item in enumerate(oilTypePrice.keys()):
    txtName = oilCostClass.getOilTxt(item)
    row = 12 + index
    tk.Radiobutton(root_window, text=txtName, width=10, command=changeOilType, variable=vRadio, value=item).grid(row=row, column=2)


vCheck = tk.IntVar()
vCheck.set(isDiscount)
def changeIsDiscount():
    global isDiscount
    checkVal = vCheck.get()
    if checkVal == 1:
        isDiscount = True
    else:
        checkVal = False
    print(isDiscount)

discountName = oilCostClass.getOilDiscountTxt()
check1 = tk.Checkbutton(root_window, text=discountName ,onvalue=1, offvalue=0, variable=vCheck, command=changeIsDiscount).grid(row=13, column=3)


vInput1 = tk.IntVar()
vInput2 = tk.IntVar()
vInput1.set(oilNum)
vInput2.set(sumMoney)

def toSumMoney():
    oilNum = int(vInput1.get())
    sumMoney = oilCostClass.toSumMoney(oilType, oilNum, isDiscount)
    vInput2.set(sumMoney)

tk.Entry(root_window, width=10, textvariable=vInput1).grid(row=12, column=4)
tk.Label(root_window, text='总价:', width=10).grid(row=13, column=4)
tk.Entry(root_window, textvariable=vInput2, width=10).grid(row=14, column=4)



    

tk.Button(root_window, text="计算", width=10, command=toSumMoney).grid(row=20, column=2)
tk.Label(root_window, text='', width=10).grid(row=20, column=3)
tk.Button(root_window, text="退出", width=10, command=root_window.quit).grid(row=20, column=4)


root_window.mainloop()