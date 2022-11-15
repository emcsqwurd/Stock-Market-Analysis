import numpy as np
import yfinance as yf
from pickle import FALSE
from fundamentalfunc import stockDate, stockArray, stockClose, stockVolume
from fundamentalfunc import stockOpen
from utils import rowElements
import matplotlib.pyplot as plt




"""Function that counts the number of dates under consideration and appends such
numbers to a list, hence function outputs list counting up to the maximum number of 
dates being considered"""
def countDateList(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    n = len(dates)
    lengthList = []
    for i in range(0, n):
        lengthList.append(i)
    return lengthList
#print(countDateList(Gamestop, startDate, endDate))



"""Function that obtains an array corresponding to the difference in stock price per date
for the number of dates being considered, that is, to obtain the High Price - Low Price
for each day under consideration"""
def stockDailyDiffPrice(stock, startD, endD):
    stockD = countDateList(stock, startD, endD)
    dailyDifferenceList = []
    for i in stockD:
        rows = rowElements(stockArray(stock, startD, endD), i)
        stockH = rows[1]
        stockL = rows[2]
        dailyDifference = stockH - stockL
        dailyDifferenceList.append(dailyDifference)
    return dailyDifferenceList
#print(stockDailyDiffPrice(Gamestop, startDate, endDate))



"""Function that obtains the TOTAL number of dates possible for any given stock under
consideration - this may vary depending on the stock being considered, as each stock 
has different length of dates for being listed on the exchange"""
def totalStockDates(stock):
    dateList = []
    finalDateList = []
    STOCK_df = yf.download(stock, progress=FALSE)
    dates = STOCK_df.index.get_level_values('Date')
    dateList.append(dates)
    dateArray = np.array(dateList)
    for i in dateArray:
        finalDateList.append(i)  
    finalArray = np.array(finalDateList)
    [finalResult] = finalArray
    return finalResult
#print(totalStockDates(Gamestop))



"""FIX"""
#THINK - add date array to box array then apply row function - DOESNT WORK!!!!!
def stockDesiredDateData(stock):
    n = 100000
    STOCK_df = yf.download(stock, progress=FALSE)
    box = STOCK_df.head(n)
    boxArray = np.array(box)
    print(boxArray)
    dateArray = totalStockDates(stock)
    print(dateArray)
    additionOfDate = np.column_stack((boxArray, dateArray))
    return additionOfDate
#print(stockDesiredDateData(Gamestop))



"""Function that obtains List corresponding to the difference in Close Price between 
day i -> i+1 for any given stock for specified dates.  Function gives an indication
of how much the stock moves each day for the dates being considered"""
def stockDifferenceFromPreviousDayClose(stock, startD, endD):
    diffList = []
    close = stockClose(stock, startD, endD)
    lengthClose = len(close)
    for element in range(1, lengthClose):
        diff = close[int(element)] - close[int(element) - 1]
        diffList.append(abs(diff)) #Returns the magnitude of Difference  
    diffList.append(0) #To keep arrays same dimension
    return diffList
#print(stockDifferenceFromPreviousDayClose(Gamestop, startDate, endDate))



"""Function that obtains List corresponding to the difference in Volume
between day i -> i+1 for any given stock for specified dates.  Function gives an 
indication of how much the volume changes between days."""
def stockDifferenceFromPreviousDayVolume(stock, startD, endD):
    diffList = []
    volumeValue = stockVolume(stock, startD, endD)
    lengthVolume = len(volumeValue)
    for element in range(1, lengthVolume):
        diff = volumeValue[int(element)] - volumeValue[int(element) - 1]
        diffList.append(abs(diff))
    diffList.append(0)    
    return diffList
#print(stockDifferenceFromPreviousDayVolume(Gamestop, startDate, endDate))





def stockAverageOfClose(stock, startD, endD):
    return 




def stockAverageOfVolume(stock, startD, endD):
    return 





"""Function to obtain Difference Price from Market Close to Market Open"""
def stockDifferenceCloseToOpen(stock, startD, endD):
    differenceList = []
    closeP = stockClose(stock, startD, endD)
    openP = stockOpen(stock, startD, endD)
    for elementClose in range (0, len(closeP) -1):
        difference = closeP[int(elementClose)] - openP[int(elementClose) + 1]
        differenceList.append(difference)
    differenceList.append(0) #used to keep dimension same - requires cleaning
    return differenceList
#print(stockDifferenceCloseToOpen(Gamestop, startDate, endDate))    




"""Function to show an Increase in Price from Market close to Market Open"""
def stockDifferenceCloseToOpenIncrease(stock, startD, endD):
    increaseList = []
    difference = stockDifferenceCloseToOpen(stock, startD, endD)
    for differenceElement in difference:
        if differenceElement <= 0:
            increaseList.append(differenceElement)
    return increaseList
#print(stockDifferenceCloseToOpenIncrease(Gamestop, startDate, endDate))    



"""Function to show a Decrease in Price from Market Close to Open"""
def stockDifferenceCloseToOpenDecrease(stock, startD, endD):
    decreaseList = []
    difference = stockDifferenceCloseToOpen(stock, startD, endD)
    for differenceElement in difference:
        if differenceElement > 0:
            decreaseList.append(differenceElement)
    return decreaseList
#print(stockDifferenceCloseToOpenDecrease(Gamestop, startDate, endDate))    














#-----------------------Investigation Plots----------------




#-----------------------INVESTIGATIONS--------------------------------------------------




"""Function to obtain Plot for Daily Difference in Stock Price for specified Dates"""
def stockDailyDifferenceGraph(stock, startD, endD):
    date = stockDate(stock, startD, endD)
    difference = stockDailyDiffPrice(stock, startD, endD)
    plt.plot(date, difference, 'r')
    plt.title("Daily Difference in stock price for:" + str(stock))
    plt.show()
    return 



"""Function to obtain Plot of Difference from Previous Day Close Price of stock for
specified Dates """
def stockDifferenceFromPreviousDayCloseGraph(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    diff = stockDifferenceFromPreviousDayClose(stock, startD, endD)
    plt.plot(dates, diff, 'r')
    plt.xlabel("Dates")
    plt.ylabel("Difference from Previous days Close Price (USD)")
    plt.title("Difference in close Price from previous Trading Day")
    plt.show()
    return 
#print(stockDifferenceFromPreviousDayCloseGraph(Gamestop, startDate, endDate))



"""Function to obtain Plot of Difference from Previous Day Volume of stock
for specified Dates"""
def stockDifferenceFromPreviousDayVolumeGraph(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    diff = stockDifferenceFromPreviousDayVolume(stock, startD, endD)
    plt.plot(dates, diff, 'b')
    plt.xlabel("Dates")
    plt.ylabel("Difference from Previous days Volume (STP.TD)")
    plt.title("Difference in Volume from previous Trading Day")
    plt.show()
    return 
#print(stockDifferenceFromPreviousDayVolumeGraph(Gamestop, startDate, endDate))














