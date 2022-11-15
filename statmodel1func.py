import numpy as np
from fundamentalfunc import stockClose, stockVolume, stockDate
from investigationfunc import stockDifferenceFromPreviousDayClose
from investigationfunc import stockDifferenceFromPreviousDayVolume




#-----------------------------Paper Implementation + Addition-------------------------------------



#Double Check
"""Function that obtains a List corresponding to the Percentage Difference in Change 
in Close Price for a given stock for specified dates being considered, that is,
the difference in Close Price between subsequent days i -> i+1 divided by the Close
Price on day i"""
def stockDailyArithmeticReturns(stock, startD, endD):
    percentageList = []
    closeP = stockClose(stock, startD, endD)
    lengthCloseP = len(closeP)
    diffPrevious = stockDifferenceFromPreviousDayClose(stock, startD, endD)
    for element in range(0, lengthCloseP):
        percent = diffPrevious[int(element)] / closeP[int(element)]
        percentageList.append(percent)
    return percentageList
#print(stockDailyArithmeticReturns(Gamestop, startDate, endDate))    



"""Function that obtains a List corresponding to the Percentage Difference in Change
in Volume for a given stock for specified dates being considered, that is, the Difference
in Volume between subsequent days i -> i+1 divided by the Volume on day i"""
def stockDailyArithmeticVolume(stock, startD, endD):
    percentageList = []
    volume = stockVolume(stock, startD, endD)
    lengthV = len(volume)
    diffPrevious = stockDifferenceFromPreviousDayVolume(stock, startD, endD)
    for element in range(0, lengthV):
        percent = diffPrevious[int(element)] / volume[int(element)]
        percentageList.append(percent)
    return percentageList
#print(stockDailyArithmeticVolume(Gamestop, startDate, endDate))    




"""Function to obtain the Daily Geometric Returns for a given stock over desired Dates"""
def stockDailyGeometricReturns(stock, startD, endD):
    geometricList = []
    closeP = stockClose(stock, startD, endD)
    lengthCloseP = len(closeP)
    for element in range(0, lengthCloseP):
        GR = np.log(closeP[int(element)]) - np.log(closeP[int(element) - 1])
        geometricList.append(GR)
    return geometricList
#print(stockDailyGeometricReturns(Gamestop, startDate, endDate))    




"""Function that obtains a List corresponding to the Continuously Compounded Return for 
a stock for specified Date Interval, that is, the Close Price on day i divided by the
Close Price on day (i-1)"""
def stockContinuouslyCompoundedReturn(stock, startD, endD):
    CCRList = []
    stockC = stockClose(stock, startD, endD)
    lengthStockC = len(stockC)
    for price in range(0, lengthStockC):
        CCR = stockC[int(price)] / stockC[int(price) - 1]
        CCRList.append(CCR)
    return CCRList
#print(stockContinuouslyCompoundedReturn(Gamestop, startDate, endDate))


#-----FIX------
"""Mean of Continuously Compounded Return"""
def stockMean(stock, startD, endD):
    meanL = []
    dates = stockDate(stock, startD, endD)
    lengthDates = len(dates)
    constant = 1 / lengthDates
    CCR = stockContinuouslyCompoundedReturn(stock,startD, endD)
    lengthCCR = len(CCR)
    sum = 0
    for element in range(0, lengthCCR):
        res = CCR[element]
        sum += res 
    finalResult = constant*sum
    meanL.append(finalResult)    
    return meanL
#print(stockMean(Gamestop, startDate, endDate))    







#-------------------------------End Paper Implementation-------------------------------------------




