import numpy as np
from fundamentalfunc import stockClose, stockDate, stockHigh, stockLow, stockOpen
import matplotlib.pyplot as plt







#-----------------------------------VOLATILITY INDICATORS-----------------------------------



"""Volatility = the rate at which the price of a stock increases or decreases over a particular period."""

""" Implied volatility is derived from the Black-Scholes formula, and using it can provide 
significant benefits to investors. Implied volatility is an estimate of the future 
variability for the asset underlying the options contract."""








"""Logarithmic difference volatility indicator (1999)"""
def volatility_S_t(stock, startD, endD):
    stockH = stockHigh(stock, startD, endD)
    stockL = stockLow(stock, startD, endD)
    V_S_t = np.log(stockH) - np.log(stockL)
    return V_S_t
#print(volatility_S_t(Gamestop, startDate, endDate))    



"""Parkinson (1980) proposes a volatility measure assuming an underlying geometric 
Brownian motion with no drift for the prices"""
def volatility_P_t(stock, startD, endD):
    constant = 0.361
    stockH = stockHigh(stock, startD, endD)
    stockL = stockLow(stock, startD, endD)
    listsDivision = [i / j for i, j in zip(stockH, stockL)]
    V_P_t = constant*(np.log(listsDivision))**2
    return V_P_t
#print(volatility_P_t(Gamestop, startDate, endDate))    



"""Garman and Klass (1980) suggest the following volatility indicator.  According to Chan 
and Lien (2003), both measures are unbiased when the sample data are continuously 
observed with VGK,t being more efficient than VP,t."""
def volatility_GK_t(stock, startD, endD):
    stockH = stockHigh(stock, startD, endD)
    stockL = stockLow(stock, startD, endD)
    stockC = stockClose(stock, startD, endD)
    stockO = stockOpen(stock, startD, endD)
    V_GK_t = 0.5*(np.log(stockH) - np.log(stockL))**2 - ((2*np.log(2) - 1)*(np.log(stockC) - np.log(stockO))**2)
    return V_GK_t
#print(volatility_GK_t(sp500_ETF, startDate, endDate))



"""When the drift term is not zero, neither the Parkinson nor the Garman-Klass measures 
are efficient (Chan and Lien, 2003). Hence, an alternative measure with independent drift 
is required.  Rogers and Satchell (1991) and Rogers, Satchell and Yoon (1994) propose a 
volatility measure which is subject to a downward bias problem:"""
def volatility_RS_t(stock, startD, endD):
    stockH = stockHigh(stock, startD, endD)
    stockL = stockLow(stock, startD, endD)
    stockC = stockClose(stock, startD, endD)
    stockO = stockOpen(stock, startD, endD)
    V_RS_t = (np.log(stockH) - np.log(stockO))*(np.log(stockH) - np.log(stockC)) + (np.log(stockL) - np.log(stockO))*(np.log(stockL) - np.log(stockC))
    return V_RS_t
#print(volatility_RS_t(sp500_ETF, startDate, endDate))    








#-----------------------------END VOLATILITY MODELS--------------------------------------







#------------------------------START VOLATILITY PLOTS------------------------------------







"""Fuction that obtains plot for Volatility indicator V_(S,t) for specified Dates"""
def volatility_S_t_Graph(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    vol = volatility_S_t(stock, startD, endD)
    plt.plot(dates, vol, 'r')
    plt.show()
    return 
#print(volatility_S_t_Graph(sp500_ETF, startDate08, endDate08))


"""Function that obtains plot for Volatility indicator V_(P,t) for specified Dates"""
def volatility_P_t_Graph(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    vol = volatility_P_t(stock, startD, endD)
    plt.plot(dates, vol, 'b')
    plt.show()
    return 
#print(volatility_P_t_Graph(sp500_ETF, startDate08, endDate08))



"""Function that obtains plot for Volatility indicator V_(GK,t) for specified Dates"""
def volatility_GK_t_Graph(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    vol = volatility_GK_t(stock, startD, endD)
    plt.plot(dates, vol, 'g')
    plt.show()
    return 
#print(volatility_GK_t_Graph(sp500_ETF, startDate08, endDate08))



"""Function thast obtains plot for Volatility indicator V_(RS,t) for specified dates"""
def volatility_RS_t_Graph(stock, startD, endD):
    dates = stockDate(stock, startD, endD)
    vol = volatility_RS_t(stock, startD, endD)
    plt.plot(dates, vol, 'g')
    plt.show()
    return 
#print(volatility_RS_t_Graph(sp500_ETF, startDate08, endDate08))



