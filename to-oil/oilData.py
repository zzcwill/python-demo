oilTypeList = [92, 97, 98]

oilPriceList = {
  92: 7.88,
  97: 8.23,
  98: 8.78,
}

discount = 0.95

class OilClass:
    def __init__(self):
        pass
    
    def getOilTxt1(self, oilType):
        return (str(oilType) + '号汽油')
    
    def getOilTxt2(self, oilType):
        return (str(oilPriceList[oilType]) + '元/升')
    
    def getOilDiscountTxt(self):
        return (str(int(discount*100)) + '折')

    def toSumData(self, oilType, oilNum, discountType):
        sum = 0;
        oilPrice = oilPriceList[oilType]
        if discountType == 1:
            sum = oilPrice*oilNum*discount
        else:
            sum = oilPrice*oilNum

        return sum