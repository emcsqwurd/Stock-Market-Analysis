import numpy as np
from stock import totalStock
from investigationfunc import countDateList, stockDailyDiffPrice, totalStockDates
from investigationfunc import stockDesiredDateData, stockDifferenceFromPreviousDayClose, stockDifferenceFromPreviousDayVolume
from investigationfunc import stockAverageOfClose, stockAverageOfVolume #NOT COMPLETE
from investigationfunc import stockDifferenceCloseToOpen, stockDifferenceCloseToOpenDecrease, stockDifferenceCloseToOpenIncrease




class Investigation:

    #Private Attributes
    __defaultStartDate = '2018-01-01'
    __defaultEndDate = '2022-01-01'


    #Constructor
    def __init__(self) -> None:
        self.__parms = {}
        self.setParms(
            startD8 = self.get__defaultStartDate(),
            endD8 = self.get__defaultEndDate()
        )


    #Getters
    def get__defaultStartDate(self):
        return self.__defaultStartDate
    def get__defaultEndDate(self):
        return self.__defaultEndDate

    def getStartDate(self):
        return self.__parms["startD8"]
    def getEndDate(self):
        return self.__parms["endD8"] 
        
    def getStock(self, ticker):
        allStocks = totalStock()
        if [ticker] in allStocks:
            return [ticker] 
        else:
            raise TypeError("Stock has not been added.  Please Choose another stock to be considered")     
        
    def getCountDateList(self, ticker):
        return self.countDatesList(ticker)
    def getDailyDiffPrice(self, ticker):
        return self.dailyDiffPrice(ticker)
    def getStockDatesTotal(self, ticker):
        return self.stockDatesTotal(ticker)
    def getDesiredDateData(self, ticker):
        return self.desiredDateData(ticker)
    def getDiffPreviousDayClose(self, ticker):
        return self.diffPreviousDayClose(ticker)
    def getDiffPreviousDayVolume(self, ticker):
        return self.diffPreviousDayClose(ticker)
    def getDiffCloseToOpen(self, ticker):
        return self.diffCloseToOpen(ticker)
    def getDiffCloseToOpenIncrease(self, ticker):
        return self.diffCloseToOpenIncrease(ticker)
    def getDiffCloseToOpenDecrease(self, ticker):
        return self.diffCloseToOpenDecrease(ticker)


    #Setters

    def __setStartD8(self, startD8):
        self.__parms["startD8"] = startD8
    def __setEndD8(self, endD8):
        self.__parms["endD8"] = endD8    

    def setParms(self, **kwargs):
        for arg in kwargs:
            if arg == "startD8":
                startD8 = kwargs.get("startD8")
                self.__setStartD8(startD8)
            if arg == "endD8":
                endD8 = kwargs.get("endD8")
                self.__setEndD8(endD8)  


    #Methods
    def countDatesList(self, ticker):
        CDL = countDateList(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return CDL

    def dailyDiffPrice(self, ticker):
        DDP = stockDailyDiffPrice(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return DDP

    def stockDatesTotal(self, ticker):
        SDT = totalStockDates(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return SDT

    def desiredDateData(self, ticker):
        DDD = stockDesiredDateData(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return DDD

    def diffPreviousDayClose(self, ticker):
        DPDC = stockDifferenceFromPreviousDayClose(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return DPDC

    def diffPreviousDayVolume(self, ticker):
        DPDV = stockDifferenceFromPreviousDayVolume(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return DPDV

    def diffCloseToOpen(self, ticker):
        DCTO = stockDifferenceCloseToOpen(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return DCTO

    def diffCloseToOpenIncrease(self, ticker):
        DCTOI = stockDifferenceCloseToOpenIncrease(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return DCTOI

    def diffCloseToOpenDecrease(self, ticker):
        DCTOD = stockDifferenceCloseToOpenDecrease(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return DCTOD



