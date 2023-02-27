#!/usr/bin/python3

oilTypeList = ['92', '97', '98']

oilTypePrice = {
  '92': 7.88,
  '97': 8.23,
  '98': 8.78
}

discountNum = 0.95

class OilCost:
    def __init__(self):
        pass
    
    def getOilTxt(self, oilType):
        return (oilType + '号汽油')

    def getOilMoneyTxt(self, oilType):
        return (str(oilTypePrice[oilType]) + '元/升')
    
    def getOilDiscountTxt(self):
        return (str(int(discountNum*100)) + '折')

    def toSumMoney(self, oilType, oilNum, isDiscount):
        print(oilType, oilNum, isDiscount)
        sum = 0
        price = oilTypePrice[str(oilType)]
        if isDiscount == 0:
            sum = price * oilNum

        if isDiscount == 1:
            sum = price * oilNum * discountNum

        return sum
              
