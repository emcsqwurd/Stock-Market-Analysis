import numpy as np
from sectorfunc import stock_Energy_Sector_1, stock_Materials_Sector_2
from sectorfunc import stock_Industrials_Sector_3, stock_Consumer_Discretionary_Sector_4
from sectorfunc import stock_Consumer_Staples_Sector_5, stock_Healthcare_Sector_6
from sectorfunc import stock_Financial_Sector_7, stock_Information_Tech_Sector_8
from sectorfunc import stock_Communication_Services_Sector_9, stock_Utilities_Sector_10
from sectorfunc import stock_RealEstate_Sector_11




class StockSector:


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

    def getEnergy1(self):
        return self.energy1()
    def getMaterials2(self):
        return self.materials2()
    def getIndustrails3(self):
        return self.industrials3()
    def getConsumerDiscretionary4(self):
        return self.consumerDiscretionary4()
    def getConsumerStaples5(self):
        return self.consumerStaples5()
    def getHealthcare6(self):
        return self.healthcare6()
    def getFinancials7(self):
        return self.financial7()
    def getInformationTechnology8(self):
        return self.informationTechnology8()
    def getCommunicationServices9(self):
        return self.communicationServices9()
    def getUtilities10(self):
        return self.utilities10() 
    def getRealEstate11(self):
        return self.realEstate11()                     


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

        #any method functions -> self.__setFUNC()
        


    #Methods    
    def energy1(self):
        stockE = stock_Energy_Sector_1()
        return stockE

    def materials2(self):
        stockM = stock_Materials_Sector_2()
        return stockM

    def industrials3(self):
        stockI = stock_Industrials_Sector_3()
        return stockI

    def consumerDiscretionary4(self):
        stockCD = stock_Consumer_Discretionary_Sector_4()
        return stockCD

    def consumerStaples5(self):
        stockCS = stock_Consumer_Staples_Sector_5()
        return stockCS

    def healthcare6(self):
        stockH = stock_Healthcare_Sector_6()
        return stockH

    def financial7(self):
        stockF = stock_Financial_Sector_7()
        return stockF

    def informationTechnology8(self):
        stockIT = stock_Information_Tech_Sector_8()
        return stockIT

    def communicationServices9(self):
        stockCS = stock_Communication_Services_Sector_9()
        return stockCS

    def utilities10(self):
        stockU = stock_Utilities_Sector_10()
        return stockU

    def realEstate11(self):
        stockRE = stock_RealEstate_Sector_11()
        return stockRE        







