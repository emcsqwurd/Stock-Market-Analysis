import numpy as np
from stock import totalStock
from statmodel1func import stockDailyArithmeticReturns, stockDailyArithmeticVolume, stockDailyGeometricReturns
from statmodel1func import stockContinuouslyCompoundedReturn, stockMean




class StatModel1:

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
        
    def getDailyArithmeticReturns(self, ticker):
        return self.dailyArithmeticReturns(ticker)  
    def getDailyArithmeticVolume(self, ticker):
        return self.dailyArithmeticVolume(ticker)
    def getDailyGeometricReturns(self, ticker):
        return self.dailyGeometricReturns(ticker)
    def getContinuouslyCompoundedReturns(self, ticker):
        return self.continuouslyCompoundedReturns(ticker)
    def getMean(self, ticker):
        return self.mean(ticker)                  
     
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
    def dailyArithmeticReturns(self, ticker):
        DAR = stockDailyArithmeticReturns(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return DAR

    def dailyArithmeticVolume(self, ticker):
        DAV = stockDailyArithmeticVolume(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return DAV

    def dailyGeometricReturns(self, ticker):
        DGR = stockDailyGeometricReturns(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return DGR

    def continuouslyCompoundedReturns(self, ticker):
        CCR = stockContinuouslyCompoundedReturn(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return CCR

    def mean(self, ticker):
        M = stockMean(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return M






