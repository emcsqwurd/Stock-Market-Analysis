import numpy as np
from stock import totalStock
from investigationfunc import stockDailyDifferenceGraph, stockDifferenceFromPreviousDayCloseGraph
from investigationfunc import stockDifferenceFromPreviousDayVolumeGraph 





class InvestigationPlots:

    #Private Attributes
    __defaultStartDate = '2018-01-01'
    __defaultEndDate = '2022-01-01'


    #Constructor
    def __init__(self) -> None:
        self.__parms = {}
        self.setParms(
            startD8 = self.get__defaultStartDate(),
            endD8 = self.get__defaultEndDate(),
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


    def getDailyDifferenceGraph(self, ticker):
        return self.dailyDifferenceGraph(ticker)
    def getDifferenceFromPreviousDayCloseGraph(self, ticker):
        return self.differenceFromPreviousDayCloseGraph(ticker)
    def getDifferenceFromPreviousDayVolumeGraph(self, ticker):
        return self.differenceFromPreviousDayVolumeGraph(ticker)

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

    def dailyDifferenceGraph(self, ticker):
        DDG = stockDailyDifferenceGraph(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return DDG

    def differenceFromPreviousDayCloseGraph(self, ticker):
        PDC = stockDifferenceFromPreviousDayCloseGraph(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return PDC

    def differenceFromPreviousDayVolumeGraph(self, ticker):
        PDV = stockDifferenceFromPreviousDayVolumeGraph(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return PDV


