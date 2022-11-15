import numpy as np
from sectorfunc import stock_Energy_Sector_1, stock_Materials_Sector_2, stock_Industrials_Sector_3
from sectorfunc import stock_Consumer_Discretionary_Sector_4, stock_Consumer_Staples_Sector_5, stock_Healthcare_Sector_6
from sectorfunc import stock_Financial_Sector_7, stock_Information_Tech_Sector_8, stock_Communication_Services_Sector_9
from sectorfunc import stock_Utilities_Sector_10, stock_RealEstate_Sector_11, stockChoiceSample






def totalStock():
    tickernameList = []
    energy = stock_Energy_Sector_1()
    materials = stock_Materials_Sector_2()
    Industrials = stock_Industrials_Sector_3()
    CD = stock_Consumer_Discretionary_Sector_4()
    CS = stock_Consumer_Staples_Sector_5()
    healthcare = stock_Healthcare_Sector_6()
    financial = stock_Financial_Sector_7()
    IT = stock_Information_Tech_Sector_8()
    communication = stock_Communication_Services_Sector_9()
    utilities = stock_Utilities_Sector_10()
    realEstate = stock_RealEstate_Sector_11()
    extra = stockChoiceSample()
    for stock in energy:
        tickernameList.append(stock)
    for stock in materials:
        tickernameList.append(stock)
    for stock in Industrials:
        tickernameList.append(stock)
    for stock in CD:
        tickernameList.append(stock)
    for stock in CS:
        tickernameList.append(stock)
    for stock in healthcare:
        tickernameList.append(stock)
    for stock in financial:
        tickernameList.append(stock)
    for stock in IT:
        tickernameList.append(stock)
    #for stock in communication:
        #tickernameList.append(stock)
    for stock in utilities:
        tickernameList.append(stock)
    for stock in realEstate:
        tickernameList.append(stock)   
    for stock in extra:
        tickernameList.append(stock)                                     
    return tickernameList
#print(totalStock())  




