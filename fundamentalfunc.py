import numpy as np
import yfinance as yf
from utils import rowElements, columnElements
import matplotlib.pyplot as plt


#------------------------------Fundamental Functions--------------------------------------------------------




"""Function to obtain the data frames box when downloading data from yf"""
def stockBox(stock, startD, endD):
    n= 1000000
    STOCK_df = yf.download(stock, 
                        start= startD, 
                        end= endD, 
    )
    box = STOCK_df.head(n)
    return box
#print(stockBox(Gamestop, startDate, endDate))


"""Function that obtains an array corresponding to the data frames box for the stock
being investigated that is downloaded from yf that contains all neccessary data"""
def stockArray(stock, startD, endD):
    n = 10000000
    STOCK_df = yf.download(stock, 
                        start= startD, 
                        end= endD,
                        progress=False 
    )
    box = STOCK_df.head(n)
    box.to_csv('stock')
    result = np.array(box)
    return result
#print(stockArray(inputStock2, startDate, endDate))


"""Function that obtains an array corresponding to the dates being considered"""
def stockDate(tickername, startD, endD):
    finalDateList = []
    STOCK_df = yf.download(tickername, 
                        start= startD, 
                        end= endD, 
                        progress=False
    )
    dateList = []
    dates = STOCK_df.index.get_level_values('Date')
    dateList.append(dates)
    dateArray = np.array(dateList)
    for i in dateArray:
        finalDateList.append(i)  
    finalArray = np.array(finalDateList)
    [finalResult] = finalArray
    #print(finalDateList)
    return finalResult
#print(stockDate(Gamestop, startDate, endDate))    


"""Function that obtains an array corresponding to the Open Price for the stock for the
range of dates being considered"""
def stockOpen(tickername, startD, endD):
    listOpen = []
    res = stockArray(tickername, startD, endD)
    openP = columnElements(res, 0)
    listOpen.append(openP)
    [finalResult] = listOpen
    return finalResult
#print(stockOpen(Gamestop, startDate, endDate))


"""Function that obtains an array corresponding to the High Price for the stock for the
range of dates being considered"""
def stockHigh(tickername, startD, endD):
    listHigh = []
    res = stockArray(tickername, startD, endD)
    highP = columnElements(res, 1)
    listHigh.append(highP)
    [finalResult] = listHigh
    return finalResult
#print(stockHigh(Gamestop, startDate, endDate))    


"""Function that obtains an array corresponding to the Low Price for the stock for the 
range of dates being considered"""
def stockLow(tickername, startD, endD):
    listLow = []
    res = stockArray(tickername, startD, endD)
    lowP = columnElements(res, 2)
    listLow.append(lowP)
    [finalResult] = listLow
    return finalResult
#print(stockLow(Gamestop, startDate, endDate))    


"""Function that obtains an array corresponding to the Close Price for the stock for the
range of dates being considered"""
def stockClose(tickername, startD, endD):
    listClose = []
    res = stockArray(tickername, startD, endD)
    closeP = columnElements(res, 3)
    listClose.append(closeP)
    [finalResult] = listClose
    return finalResult
#print(stockClose(Gamestop, startDate, inputEndDate))


"""Function that obtains an array corresponding to the Adjusted Close Price for the stock
for the range of dates being considered"""
def stockAdjustedClose(tickername, startD, endD):
    listAdjustedClose = []
    res = stockArray(tickername, startD, endD)
    adjustedCloseP = columnElements(res, 4)
    listAdjustedClose.append(adjustedCloseP)
    [finalResult] = listAdjustedClose
    return finalResult
#print(stockAdjustedClose(Gamestop, inputStartDate, inputEndDate))    


"""Function that obtains an array corresponding to the Volume for the stock for the range
of dates being considered"""
def stockVolume(tickername, startD, endD):
    listVolume = []
    res = stockArray(tickername, startD, endD)
    volumeP = columnElements(res, 5)
    listVolume.append(volumeP)
    [finalResult] = listVolume
    return finalResult
#print(stockVolume(Gamestop, startDate, endDate))    



#----------------------------------End Fundamental Functions-------------------------------------






#-----------------------------------Start Fundamental Plots--------------------------------------





"""Function to obtain Plot of Close Price of stock for specified Dates"""
def stockCloseGraph(stock, startD, endD):
    date = stockDate(stock, startD, endD)    
    close = stockClose(stock, startD, endD)
    plt.plot(date, close, 'g')
    plt.title("Stock Price" + str(stock))
    plt.show()
    return 
#print(stockCloseGraph(Gamestop, startDate, endDate))


"""Function to obtain Plot of Open Price of stock for specified Dates"""
def stockOpenGraph(stock, startD, endD):
    date = stockDate(stock, startD, endD)
    open = stockOpen(stock, startD, endD)
    plt.plot(date, open, 'r')
    plt.title("Stock Open" + str(stock))
    plt.show()
    return 


"""Function to obtain Plot of Low price of stock for specified Dates"""
def stockLowGraph(stock, startD, endD):
    date = stockDate(stock, startD, endD)
    low = stockLow(stock, startD, endD)
    plt.plot(date, low, 'b')
    plt.title("Stock Low" + str(stock))
    plt.show()
    return 


"""Function to obtain Plot of High Price of stock for specified Dates"""
def stockHighGraph(stock, startD, endD):
    date = stockDate(stock, startD, endD)
    high = stockHigh(stock, startD, endD)
    plt.plot(date, high, 'y')
    plt.title("Stock High" + str(stock))
    plt.show()
    return 


"""Function to obtain Plot of Adjusted Close Price of stock for specified Dates"""
def stockAdjustedCloseGraph(stock, startD, endD):
    date = stockDate(stock, startD, endD)
    sOpen = stockAdjustedClose(stock, startD, endD)
    plt.plot(date, sOpen, 'o')
    plt.title("Stock Open" + str(stock))
    plt.show()
    return 


"""Function to obtain Plot of Volume of stock for specified Dates"""
def stockVolumeGraph(stock, startD, endD):
    date = stockDate(stock, startD, endD)
    volume = stockVolume(stock, startD, endD)
    plt.plot(date, volume, 'black')
    plt.title("Stock Volume" + str(stock))
    plt.show()
    return 













