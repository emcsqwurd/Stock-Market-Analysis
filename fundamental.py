import numpy as np
from fundamentalfunc import stockArray, stockBox, stockOpen, stockClose, stockHigh, stockLow
from fundamentalfunc import stockDate, stockAdjustedClose, stockVolume
from stock import totalStock



class Fundamental:


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


    def getBox(self, ticker):
        return self.box(ticker)
    def getSArray(self, ticker):
        return self.sarray(ticker)    
    def getDate(self, ticker):
        return self.date(ticker)  
    def getOpen(self, ticker):
        return self.open(ticker)  
    def getClose(self, ticker):
        return self.close(ticker)
    def getLow(self, ticker):
        return self.low(ticker)
    def getHigh(self, ticker):
        return self.high(ticker)
    def getVolume(self, ticker):
        return self.volume(ticker)
    def getAdjustedClose(self, ticker):
        return self.adjustedClose(ticker) 
                         


        
    

    #Setters
    def __setStartD8(self, startD8):
        self.__parms["startD8"] = startD8
    def __setEndD8(self, endD8):
        self.__parms["endD8"] = endD8 

    """
    def __set_Box(self, ticker):
        return self.box(ticker)
    def __set_SArray(self, ticker):
        return self.sarray(ticker)
    def __set_Date(self, ticker):
        return self.date(ticker)
    def __set_Open(self, ticker):
        return self.open(ticker)
    def __set_Close(self, ticker):
        return self.close(ticker)
    def __set_Low(self, ticker):
        return self.low(ticker)
    def __set_High(self, ticker):
        return self.high(ticker)
    def __set_Volume(self, ticker):
        return self.volume(ticker)
    def __set_AdjustedClose(self, ticker):
        return self.adjustedClose(ticker)
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
        self.__set_Box()
        self.__set_SArray()
        self.__set_Date()        
        self.__set_Open()
        self.__set_Close()
        self.__set_Low()
        self.__set_High()
        self.__set_Volume()
        self.__set_AdjustedClose()
        """



    #Methods

    #TAKENOTE - paramter names must be same as that used in underlying function
    def box(self, ticker):
        b = stockBox(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return b

    def sarray(self, ticker):
        a = stockArray(
            stock = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return a

    def date(self, ticker):
        stockD = stockDate(
            tickername= self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return stockD 

    def open(self, ticker):
        stockO = stockOpen(
            tickername = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return stockO

    def close(self, ticker):
        stockC = stockClose(
            tickername = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return stockC

    def low(self, ticker):
        stockL = stockLow(
            tickername = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return stockL

    def high(self, ticker):
        stockH = stockHigh(
            tickername = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return stockH

    def volume(self, ticker):
        stockV = stockVolume(
            tickername = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return stockV

    def adjustedClose(self, ticker):
        stockAC = stockAdjustedClose(
            tickername = self.getStock(ticker),
            startD = self.getStartDate(),
            endD = self.getEndDate()
        )
        return stockAC          

                 


fun = Fundamental()

print(fun.getLow('SHEL'))



