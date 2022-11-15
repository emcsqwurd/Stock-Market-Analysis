import numpy as np
from stock import totalStock
from volatilityfunc import volatility_GK_t_Graph, volatility_RS_t_Graph
from volatilityfunc import volatility_P_t_Graph, volatility_S_t_Graph





class VolatilityPlots:


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
            raise TypeError("Stock has not been added. Please Choose another ticker")


    def getVol_St_Graph(self, ticker):
        return self.vol_St_Graph(ticker) 
    def getVol_Pt_Graph(self, ticker):
        return self.vol_Pt_Graph(ticker)
    def getVol_GKt_Graph(self, ticker):
        return self.vol_GKt_Graph(ticker)
    def getVol_RSt_Graph(self, ticker):
        return self.vol_RSt_Graph(ticker)



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

    def vol_St_Graph(self, ticker):
        res = volatility_S_t_Graph(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return res

    def vol_Pt_Graph(self, ticker):
        res = volatility_P_t_Graph(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return res

    def vol_GKt_Graph(self, ticker):
        res = volatility_GK_t_Graph(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return res

    def vol_RSt_Graph(self, ticker):
        res = volatility_RS_t_Graph(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return res





volPlot = VolatilityPlots()

print(volPlot.getVol_GKt_Graph('GME'))


