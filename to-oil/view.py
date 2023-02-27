import tkinter as tk
import oilData

def main(page):
  oilType = oilData.oilTypeList[0]
  oilNum = 0
  discountType = 0
  oilClass = oilData.OilClass()

  headTitle = oilClass.getOilTxt1(oilType) + '：' + oilClass.getOilTxt2(oilType)
  tk.Label(page, width=20, text=headTitle).grid(row=1, column=1)
  tk.Label(page, text='').grid(row=1, column=2)

  tk.Label(page, text='种类').grid(row=2, column=1)
  tk.Label(page, text='').grid(row=2, column=2)  
  tk.Label(page, text='数量：升').grid(row=2, column=3)  

  vRadio = tk.IntVar()
  vRadio.set(oilType)
  for index, item in enumerate(oilData.oilTypeList):
    oilTxt = oilClass.getOilTxt1(item)
    row = 3 + index
    tk.Radiobutton(page, text=oilTxt, variable=vRadio, value=item).grid(row=row, column=1)

  vCheck = tk.IntVar()
  vCheck.set(discountType)
  checkTitle = oilClass.getOilDiscountTxt()
  print(checkTitle)
  tk.Checkbutton(page, text=checkTitle, variable=vCheck, offvalue=0, onvalue=1).grid(row=4, column=2)

  vInput = tk.IntVar()
  vInput.set(oilNum)  
  vSumInput = tk.IntVar()
  vSumInput.set(0)  
  tk.Entry(page, width=10, textvariable=vInput).grid(row=3, column=3)
  tk.Label(page, text='总价：').grid(row=4, column=3)  
  tk.Entry(page, width=10, textvariable=vSumInput).grid(row=5, column=3) 

  def toSum():
    nonlocal oilType, oilNum, discountType
    oilType = vRadio.get()
    oilNum = vInput.get()
    discountType = vCheck.get()
    summoney = oilClass.toSumData(oilType, oilNum, discountType)
    vSumInput.set(summoney)


  tk.Button(page, width=10, text='计算', command=toSum).grid(row=20, column=1)
  tk.Label(page, text='').grid(row=20, column=2)  
  tk.Button(page, width=10, text='退出', command=page.quit).grid(row=20, column=3)