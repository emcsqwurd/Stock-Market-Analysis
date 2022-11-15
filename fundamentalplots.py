import numpy as np
from stock import totalStock
from fundamentalfunc import stockCloseGraph, stockOpenGraph, stockLowGraph, stockHighGraph
from fundamentalfunc import stockAdjustedCloseGraph, stockVolumeGraph





class FundamentalPlots:
    
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


    def getCloseGraph(self, ticker):
        return self.closeGraph(ticker)
    def getOpenGraph(self, ticker):
        return self.openGraph(ticker)
    def getLowGraph(self, ticker):
        return self.lowGraph(ticker)
    def getHighGraph(self, ticker):
        return self.highGraph(ticker)
    def getAdjustedCloseGraph(self, ticker):
        return self.adjustedCloseGraph(ticker)
    def getVolumeGraph(self, ticker):
        return self.volumeGraph(ticker)                   

     


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

    def closeGraph(self, ticker):
        CG = stockCloseGraph(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return CG

    def openGraph(self, ticker):
        OG = stockOpenGraph(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return OG

    def lowGraph(self, ticker):
        LG = stockLowGraph(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return LG

    def highGraph(self, ticker):
        HG = stockHighGraph(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return HG

    def adjustedCloseGraph(self, ticker):
        ACG = stockAdjustedCloseGraph(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return ACG

    def volumeGraph(self, ticker):
        VG = stockVolumeGraph(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return VG    

    


