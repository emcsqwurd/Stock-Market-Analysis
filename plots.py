from fundamentalfunc import stockAdjustedClose, stockDate, stockClose, stockOpen, stockVolume
from fundamentalfunc import stockHigh, stockLow
from investigationfunc import stockDifferenceFromPreviousDayClose, stockDifferenceFromPreviousDayVolume, stockDailyDiffPrice
from volatilityfunc import volatility_GK_t, volatility_P_t, volatility_RS_t, volatility_S_t
from statmodel1func import stockDailyGeometricReturns
from investigationfunc import stockDifferenceCloseToOpen, stockDifferenceCloseToOpenIncrease, stockDifferenceCloseToOpenDecrease
from statmodel1func import  stockDailyArithmeticReturns, stockDailyArithmeticVolume
import numpy as np
import matplotlib.pyplot as plt





#example input stocks
Gamestop = ['GME']
Abbvie = ['ABBV']
sp500_ETF = ['SPY']
VIX = ['VIX']
AmcTheatres = ['AMC']

#example input dates
startDate = '2000-01-01'
endDate = '2022-05-26'


#2008 example input dates
startDate08 = '2008-06-01'
endDate08 = '2009-03-01'


#Range
n = 1000000





"""Function to obtain Plot for the Percentage difference in stock Price for specified 
Dates, that is, difference in Price between days i -> i+1 divided by price of day i"""
def stockDailyArithmeticReturnsGraph(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    percentChange = stockDailyArithmeticReturns(stock, startD, endD)
    plt.plot(dates, percentChange, 'g')
    plt.xlabel("dates")
    plt.ylabel("Arithmetic Returns")
    plt.title("Percentage of Close Price that stock Changed by")
    plt.show()
    return 
#print(stockDailyArithmeticReturnsGraph(Gamestop, startDate, endDate))



"""FUnction to obtain plot for the Daily Geometric Returns of a stock for specified Dates"""
def stockDailyGeometricReturnsGraph(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    GR = stockDailyGeometricReturns(stock, startD, endD)
    plt.plot(dates, GR, 'r')
    plt.xlabel("dates")
    plt.ylabel("Geometric Returns")
    plt.title("Percentage of Close Price that stock Changed by")
    plt.show()
    return 
#print(stockDailyGeometricReturnsGraph(Gamestop, startDate, endDate))



"""Function to obtain Plot for the Percentage difference in stock Volume for specified
Dates, that is, difference in Volume between days i -> i+1 divided by price of day i"""
def stockDailyArithmeticVolumeGraph(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    percentChange = stockDailyArithmeticVolume(stock, startD, endD)
    plt.plot(dates, percentChange, 'b')
    plt.xlabel("dates")
    plt.ylabel("Percentage difference")
    plt.title("Percentage of Volume that stock Changed by")
    plt.show()
    return 
#print(stockDailyArithmeticVolumeGraph(Gamestop, startDate, endDate))






















#--------------------------------------Comparing Two Stocks plots-----------------------------------






#-----FIX ARRAYS FOR DIFFERENT INPUT DATES-----
"""Function that obtains plot that compares Volumes between two input stocks for specified Dates"""
def stockVolumeCompare(stock1, stock2, startD1, startD2, endD1, endD2):
    date1 = stockDate(stock1, startD1, endD1)
    date2 = stockDate(stock2, startD2, endD2)
    volume1 = stockVolume(stock1, startD1, endD1)
    volume2 = stockVolume(stock2, startD2, endD2)
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(date1, volume1, 'r')
    ax2.plot(date2, volume2, 'g-' )
    plt.legend(['GME', 'AMC'])
    plt.title("Comparing Stock Volume between" + str(stock1) + str(stock2))
    ax1.set_ylabel("Volume (shares traded per trading day)" + str(stock1) )
    ax2.set_ylabel("Volume (shares traded per trading day)" + str(stock2))
    ax1.set_xlabel("Date")
    plt.show()
    return
#print(stockVolumeCompare(Gamestop, sp500_ETF, startDate, startDate08, endDate, endDate08))




#---------DATES BEING WEIRD FIX-------------------------
"""Function that compares the Close Price between two input stocks for specified Dates"""
def stockCloseCompare(stock1, stock2, startDate1, startDate2, endDate1, endDate2):
    date1 = stockDate(stock1, startDate1, endDate1)
    date2 = stockDate(stock2, startDate2, endDate2)
    close1 = stockClose(stock1, startDate1, endDate1)
    close2 = stockClose(stock2, startDate2, endDate2)
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(date1, close1, 'purple')
    ax2.plot(date2, close2, 'orange')
    plt.legend(['GME', 'AMC'])
    plt.title("Comparing Stock Close Price between:" + str(stock1) + str(stock2))
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Stock price (USD) of" + str(stock1))
    ax2.set_ylabel("Stock price (USD) of" + str(stock2))
    plt.show()    
    return 
#print(stockCloseCompare(Gamestop, AmcTheatres, startDate, startDate, endDate, endDate))


"""Function that compares the Open Price between two stocks for specified Dates"""
def stockOpenCompare(stock1, stock2, startD1, startD2, endD1, endD2):
    date1 = stockDate(stock1, startD1, endD1)
    date2 = stockDate(stock2, startD2, endD2)
    open1 = stockOpen(stock1, startD1, endD1)
    plt.plot(date1, open1, 'r')
    open2 = stockOpen(stock2, startD2, endD2)
    plt.plot(date2, open1, 'b')
    plt.title("Comparing Stock Open Price between:" + str(stock1) + str(stock2))
    plt.xlabel("Date")
    plt.ylabel("Stock price (USD)")
    plt.show()
    return


"""Function that compares the High Price between two stocks for specified Dates"""
def stockHighCompare(stock1, stock2, startD1, startD2, endD1, endD2):
    date1 = stockDate(stock1, startD1, endD1)
    date2 = stockDate(stock2, startD2, endD2)
    high1 = stockHigh(stock1, startD1, endD1)
    plt.plot(date1, high1, 'r')
    high2 = stockHigh(stock2, startD2, endD2)
    plt.plot(date2, high2, 'b')
    plt.title("Comparing Stock High Price between" + str(stock1) + str(stock2))
    plt.xlabel("Date")
    plt.ylabel("Stock price (USD)")
    plt.show()
    return 


"""Function that compares the Low Price between two input stocks for specified Dates"""
def stockLowCompare(stock1, stock2, startD1, startD2, endD1, endD2):
    date1 = stockDate(stock1, startD1, endD1)
    date2 = stockDate(stock2, startD2, endD2)
    low1 = stockLow(stock1, startD1, endD1)
    plt.plot(date1, low1, 'r')
    low2 = stockLow(stock2, startD2, endD2)
    plt.plot(date2, low2, 'b')
    plt.title("Comparing Stock Low Price between" + str(stock1) + str(stock2))
    plt.xlabel("Date")
    plt.ylabel("Stock price (USD)")
    plt.show()
    return 



"""Function that compares the Daily Difference (Change) in Price between two input stocks
for specified Dates"""
def stockDailyDifferenceCompare(stock1, stock2, startD1, startD2, endD1, endD2):
    date = stockDate(stock1, startD1, endD1)
    date2 =stockDate(stock2, startD2, endD2)
    DDP1 = stockDailyDiffPrice(stock1, startD1, endD1)
    plt.plot(date, DDP1, 'r')
    DDP2 = stockDailyDiffPrice(stock2, startD2, endD2)
    plt.plot(date2, DDP2)
    plt.legend(['GME', 'AMC'])
    plt.xlabel("Date")
    plt.ylabel("Stock price (USD)")
    plt.show()
    return 
#print(stockDailyDifferenceCompare(Gamestop, AmcTheatres, startDate, startDate, endDate, endDate))










#---------------------Comparing Different Data of Same Stock Plots--------------------------------












#-----NEED TO DO DUAL Y AXIS TO ACCURATELY INVESTIGATE-----
"""Function that compares the Percentage Change in Close Price for given stock with
the Close Price of that same Stock for specified Dates"""
def stockCompareDailyArithmeticReturnsWithClose(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    close = stockClose(stock, startD, endD)
    percentChange = stockDailyArithmeticReturns(stock, startD, endD)
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(dates, close, 'r')
    ax2.plot(dates, percentChange, 'b')
    ax1.set_ylabel("Close Price (USD) of" + str(stock) + "RED")
    ax2.set_ylabel("Daily Arithmetirc Return of" + str(stock) + "BLUE")
    plt.title("Comparing Close Price of Stock VS Daily Arithmetic Returns")
    plt.show()
    return 
#print(stockCompareDailyArithmeticReturnsWithClose(Gamestop, startDate, endDate))





#-----NEED TO DO DUAL Y AXIS TO ACCURATELY INVESTIGATE
"""Function that compares the Percentage Change in Volume for given stock with
the Percentage Change in Close for that same stock for specified Date interval"""
def stockComparePercentChangeVolumeAndClose(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    percentChangeV = stockDailyArithmeticVolume(stock, startD, endD)
    percentChangeC = stockDailyArithmeticReturns(stock, startD, endD)
    plt.plot(dates, percentChangeV, 'r')
    plt.plot(dates, percentChangeC, 'b')
    plt.show()
    return 
#print(stockComparePercentChangeVolumeAndClose(Gamestop, startDate, endDate))    



"""Not Right"""
def stockArithmeticVsGeometricGraph(stock, startD, endD):
    arith = stockDailyArithmeticReturns(stock, startD, endD)
    geo = stockDailyGeometricReturns(stock, startD, endD)
    plt.plot(arith, geo, 'r')
    plt.show()
    return 
#print(stockArithmeticVsGeometricGraph(sp500_ETF, startDate, endDate))    



"""Function to obtain a plot representing the difference from the Close Price to the 
Open Price - negative values imply has gone up in price, positive values imply has gone 
down in price"""
def stockDifferenceCloseToOpenGraph(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    difference = stockDifferenceCloseToOpen(stock, startD, endD)
    plt.plot(dates, difference, 'y')
    plt.xlabel("Dates")
    plt.ylabel("Difference in (USD) from Close Price to Open")
    plt.show()
    return
#print(stockDifferenceCloseToOpenGraph(Gamestop, startDate, endDate))



"""Function to obtain plot representing dates displaying a Decrease from the Close Price
to the Open Price - positive difference in USD as plot shows dates from which price has
Decreased""" 
def stockDifferenceCloseToOpenDecreaseGraph(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    difference = stockDifferenceCloseToOpen(stock, startD, endD)
    ax = plt.subplot(1,1,1)
    plt.plot(dates, difference, 'g')
    ax.set_ylim(bottom = 0)
    plt.xlabel("Dates")
    plt.ylabel("Difference in (USD) from Close Price to Open for dates which Decreased")
    plt.show()
    return 
#print(stockDifferenceCloseToOpenDecreaseGraph(Gamestop, startDate, endDate))



"""Function to obtain plot representing dates displaying an Increase from the Close Price
to the Open Price - Negative difference in USD as plot shows dates from which price has
Increased"""
def stockDifferenceCloseToOpenIncreaseGraph(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    difference = stockDifferenceCloseToOpen(stock, startD, endD)
    ax = plt.subplot(1,1,1)
    plt.plot(dates, difference, 'r')
    ax.set_ylim(top = 0)
    plt.xlabel("Dates")
    plt.ylabel("Difference in (USD) from Close Price to Open for dates which Increased")
    plt.show()
    return 
#print(stockDifferenceCloseToOpenIncreaseGraph(Gamestop, startDate, endDate))



"""Function to obtain plot representing dates displaying an Increase from the Close Price
to the Open Price - Negative difference in USD as plot shows dates from which price has
Increased - where axis is now flipped and magnitude taken"""
def stockDifferenceCloseToOpenIncreaseFlippedGraph(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    difference = stockDifferenceCloseToOpen(stock, startD, endD)
    ax = plt.subplot(1,1,1)
    plt.plot(dates, difference, 'r')
    ax.set_ylim(top = 0)
    plt.xlabel("Dates")
    plt.ylabel("Difference in (USD) from Close Price to Open for dates which Increased")
    ax.invert_yaxis()
    plt.show()
    return 
#print(stockDifferenceCloseToOpenIncreaseFlippedGraph(Gamestop, startDate, endDate))




def stockDifferenceCloseToOpenIncreaseAndDecreaseGraph(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    difference = stockDifferenceCloseToOpen(stock, startD, endD)
    ax1 = plt.subplot(1,1,1)
    plt.plot(dates, difference, 'r')
    ax1.set_ylim(top = 0)
    ax1.invert_yaxis()
    plt.show()
    return 
#print(stockDifferenceCloseToOpenIncreaseAndDecreaseGraph(Gamestop, startDate, endDate))







