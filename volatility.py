import numpy as np
from volatilityfunc import volatility_GK_t, volatility_P_t, volatility_RS_t, volatility_S_t
from stock import totalStock




class VolatilityIndicators:
    
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
        
    def getVol_ST(self, ticker):
        return self.vol_ST(ticker)
    def getVol_PT(self, ticker):
        return self.vol_PT(ticker)
    def getVol_GKT(self, ticker):
        return self.vol_GKT(ticker)
    def getVol_RST(self, ticker):
        return self.vol_RST(ticker)             
    

    #Setters
    def __setStartD8(self, startD8):
        self.__parms["startD8"] = startD8
    def __setEndD8(self, endD8):
        self.__parms["endD8"] = endD8    

    
    """
    def __set_Vol_ST(self, ticker):
        return self.vol_ST(ticker)
    def __set_Vol_PT(self, ticker):
        return self.vol_PT(ticker)
    def __set_Vol_GKT(self, ticker):
        return self.vol_GKT(ticker)
    def __set_Vol_RST(self, ticker):
        return self.vol_RST(ticker)  
    """

    def setParms(self, **kwargs):
        for arg in kwargs:
            if arg == "startD8":
                startD8 = kwargs.get("startD8")
                self.__setStartD8(startD8)
            if arg == "endD8":
                endD8 = kwargs.get("endD8")
                self.__setEndD8(endD8)    

        """
        self.__set_Vol_ST()
        self.__set_Vol_PT()
        self.__set_Vol_GKT()
        self.__set_Vol_RST()
        """
    

    #Methods - FIX
    def vol_ST(self, ticker):
        vol = volatility_S_t(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return vol

    def vol_PT(self, ticker):
        vol = volatility_P_t(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return vol

    def vol_GKT(self, ticker):
        vol = volatility_GK_t(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return vol

    def vol_RST(self, ticker):
        vol = volatility_RS_t(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return vol



vol = VolatilityIndicators()
#print(vol.__set_Vol_GKT('GME'))
print(vol.getVol_ST('GME'))



