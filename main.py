
from secrets import choice
import numpy as np
from sectorfunc import stockChoiceSample
from sectorfunc import stock_Energy_Sector_1, stock_Materials_Sector_2
from sectorfunc import stock_Industrials_Sector_3, stock_Consumer_Discretionary_Sector_4
from sectorfunc import stock_Consumer_Staples_Sector_5, stock_Healthcare_Sector_6
from sectorfunc import stock_Financial_Sector_7, stock_Information_Tech_Sector_8
from sectorfunc import stock_Communication_Services_Sector_9, stock_Utilities_Sector_10
from sectorfunc import stock_RealEstate_Sector_11
from fundamentalfunc import stockDate, stockClose, stockOpen, stockHigh, stockLow, stockVolume
from plots import stockCloseGraph, stockDailyDifferenceCompare, stockHighGraph, stockLowGraph, stockOpenGraph, stockVolumeGraph
from plots import stockCloseCompare, stockVolumeCompare, stockLowCompare, stockHighCompare, stockOpenCompare
from fundamentalfunc import stockDailyDifference

def mainStockPrice():
    print("Choose stock ticker to be considered:")
    tickername = input()
    print("-----Stock choice = " + tickername)
    print("Choose start date to be considered:")
    startD = input()
    print("-----Start Date = " + startD)
    print("Choose End Date to be considered:")
    endD = input()
    print("-----End Date = " + endD)
    sampleStocks = stockChoiceSample()
    for stock in sampleStocks:
        if (stock == [tickername]):
            stockCloseGraph(tickername, startD, endD)
        else:
            print("Invalid stock entry.  Run program again.")    
    return 
#print(mainStockPrice())


def mainStockScript():
    print("Select a number representing the Stock Sector to be considered:")
    print("(1): Energy Sector")
    print("(2): Materials Sector")
    print("(3): Industrials Sector")
    print("(4): Consumer Discretionary Sector")
    print("(5): Consumer Staples Sector")
    print("(6): Healthcare Sector")
    print("(7): Financials Sector")
    print("(8): Information Technology Sector")
    print("(9): Communication Services Sector")
    print("(10): Utilities Sector")
    print("(11): Real Estate Sector")
    print("(100): Compare given Stocks")
    choiceOfSector = input()
    if (int(choiceOfSector) == int(1)):
        energyStocks = stock_Energy_Sector_1()
        print("Stocks within the Energy Sector:")
        print(energyStocks) 
        print("Choose Stock to be considered:")
        stockConsidered = input()
        print("-----Stock Choice = " + stockConsidered)
        print("Choose start date to be considered:")
        startD = input()
        print("-----Start Date = " + startD)
        print("Choose End Date to be considered:")
        endD = input()
        print("-----End Date = " + endD)
        print("Choose what to investigate:")
        print("(1): Daily Close")
        print("(2): Daily Low")
        print("(3): Daily High")
        print("(4): Daily Volume")
        print("(5): Daily Open")
        toBeInvestigated = input()
        if (int(toBeInvestigated) == int(1)):
            stockCloseGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(2)):
            stockLowGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(3)):
            stockHighGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(4)):
            stockVolumeGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(5)):
            stockOpenGraph([stockConsidered], startD, endD)
    if (int(choiceOfSector) == int(2)):
        materialsStocks = stock_Materials_Sector_2()
        print("Stocks within the Materials Sector:")
        print(materialsStocks) 
        print("Choose Stock to be considered:")
        stockConsidered = input()
        print("-----Stock Choice = " + stockConsidered)
        print("Choose start date to be considered:")
        startD = input()
        print("-----Start Date = " + startD)
        print("Choose End Date to be considered:")
        endD = input()
        print("-----End Date = " + endD)
        print("Choose what to investigate:")
        print("(1): Daily Price")
        print("(2): Daily Low")
        print("(3): Daily High")
        print("(4): Daily Volume")
        print("(5): Open Price")
        toBeInvestigated = input()
        if (int(toBeInvestigated) == int(1)):
            stockCloseGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(2)):
            stockLowGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(3)):
            stockHighGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(4)):
            stockVolumeGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(5)):
            stockOpenGraph([stockConsidered], startD, endD)
    if (int(choiceOfSector) == int(3)):
        industrialStocks = stock_Industrials_Sector_3()
        print("Stocks within the Industrial Sector:")
        print(industrialStocks)
        print("Choose Stock to be considered:")
        stockConsidered = input()
        print("-----Stock Choice = " + stockConsidered)
        print("Choose start date to be considered:")
        startD = input()
        print("-----Start Date = " + startD)
        print("Choose End Date to be considered:")
        endD = input()
        print("-----End Date = " + endD)
        print("Choose what to investigate:")
        print("(1): Daily Price")
        print("(2): Daily Low")
        print("(3): Daily High")
        print("(4): Daily Volume")
        print("(5): Open Price")
        toBeInvestigated = input()
        if (int(toBeInvestigated) == int(1)):
            stockCloseGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(2)):
            stockLowGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(3)):
            stockHighGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(4)):
            stockVolumeGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(5)):
            stockOpenGraph([stockConsidered], startD, endD)
    if (int(choiceOfSector) == int(4)):
        consumerDiscretionaryStocks = stock_Consumer_Discretionary_Sector_4()
        print("Stocks within the Consumer Discretionary Sector")
        print(consumerDiscretionaryStocks)
        print("Choose Stock to be considered:")
        stockConsidered = input()
        print("-----Stock Choice = " + stockConsidered)
        print("Choose start date to be considered:")
        startD = input()
        print("-----Start Date = " + startD)
        print("Choose End Date to be considered:")
        endD = input()
        print("-----End Date = " + endD)
        print("Choose what to investigate:")
        print("(1): Daily Price")
        print("(2): Daily Low")
        print("(3): Daily High")
        print("(4): Daily Volume")
        print("(5): Open Price")
        toBeInvestigated = input()
        if (int(toBeInvestigated) == int(1)):
            stockCloseGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(2)):
            stockLowGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(3)):
            stockHighGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(4)):
            stockVolumeGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(5)):
            stockOpenGraph([stockConsidered], startD, endD)
    if (int(choiceOfSector) == int(5)):
        consumerStaplesStocks = stock_Consumer_Staples_Sector_5()
        print("Stocks within the Consumer Staples Sector")
        print(consumerStaplesStocks)
        print("Choose Stock to be considered:")
        stockConsidered = input()
        print("-----Stock Choice = " + stockConsidered)
        print("Choose start date to be considered:")
        startD = input()
        print("-----Start Date = " + startD)
        print("Choose End Date to be considered:")
        endD = input()
        print("-----End Date = " + endD)
        print("Choose what to investigate:")
        print("(1): Daily Price")
        print("(2): Daily Low")
        print("(3): Daily High")
        print("(4): Daily Volume")
        print("(5): Open Price")
        toBeInvestigated = input()
        if (int(toBeInvestigated) == int(1)):
            stockCloseGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(2)):
            stockLowGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(3)):
            stockHighGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(4)):
            stockVolumeGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(5)):
            stockOpenGraph([stockConsidered], startD, endD)
    if (int(choiceOfSector) == int(6)):
        healthcareStocks = stock_Healthcare_Sector_6()
        print("Stocks within the Healthcare Sector")
        print(healthcareStocks)
        print("Choose Stock to be considered:")
        stockConsidered = input()
        print("-----Stock Choice = " + stockConsidered)
        print("Choose start date to be considered:")
        startD = input()
        print("-----Start Date = " + startD)
        print("Choose End Date to be considered:")
        endD = input()
        print("-----End Date = " + endD)
        print("Choose what to investigate:")
        print("(1): Daily Price")
        print("(2): Daily Low")
        print("(3): Daily High")
        print("(4): Daily Volume")
        print("(5): Open Price")
        toBeInvestigated = input()
        if (int(toBeInvestigated) == int(1)):
            stockCloseGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(2)):
            stockLowGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(3)):
            stockHighGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(4)):
            stockVolumeGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(5)):
            stockOpenGraph([stockConsidered], startD, endD)
    if (int(choiceOfSector) == int(7)):
        financialStocks = stock_Financial_Sector_7()
        print("Stocks within the Financial Sector")
        print(financialStocks)
        print("Choose Stock to be considered:")
        stockConsidered = input()
        print("-----Stock Choice = " + stockConsidered)
        print("Choose start date to be considered:")
        startD = input()
        print("-----Start Date = " + startD)
        print("Choose End Date to be considered:")
        endD = input()
        print("-----End Date = " + endD)
        print("Choose what to investigate:")
        print("(1): Daily Price")
        print("(2): Daily Low")
        print("(3): Daily High")
        print("(4): Daily Volume")
        print("(5): Open Price")
        toBeInvestigated = input()
        if (int(toBeInvestigated) == int(1)):
            stockCloseGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(2)):
            stockLowGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(3)):
            stockHighGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(4)):
            stockVolumeGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(5)):
            stockOpenGraph([stockConsidered], startD, endD)
    if (int(choiceOfSector) == int(8)):
        informationTechStocks = stock_Information_Tech_Sector_8()
        print("Stocks within the Information Technology Sector")
        print(informationTechStocks)
        print("Choose Stock to be considered:")
        stockConsidered = input()
        print("-----Stock Choice = " + stockConsidered)
        print("Choose start date to be considered:")
        startD = input()
        print("-----Start Date = " + startD)
        print("Choose End Date to be considered:")
        endD = input()
        print("-----End Date = " + endD)
        print("Choose what to investigate:")
        print("(1): Daily Price")
        print("(2): Daily Low")
        print("(3): Daily High")
        print("(4): Daily Volume")
        print("(5): Open Price")
        toBeInvestigated = input()
        if (int(toBeInvestigated) == int(1)):
            stockCloseGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(2)):
            stockLowGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(3)):
            stockHighGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(4)):
            stockVolumeGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(5)):
            stockOpenGraph([stockConsidered], startD, endD)
    if (int(choiceOfSector) == int(9)):
        communicationStocks = stock_Communication_Services_Sector_9()
        print("Stocks within the Communication Sector")
        print(communicationStocks)
        print("Choose Stock to be considered:")
        stockConsidered = input()
        print("-----Stock Choice = " + stockConsidered)
        print("Choose start date to be considered:")
        startD = input()
        print("-----Start Date = " + startD)
        print("Choose End Date to be considered:")
        endD = input()
        print("-----End Date = " + endD)
        print("Choose what to investigate:")
        print("(1): Daily Price")
        print("(2): Daily Low")
        print("(3): Daily High")
        print("(4): Daily Volume")
        print("(5): Open Price")
        toBeInvestigated = input()
        if (int(toBeInvestigated) == int(1)):
            stockCloseGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(2)):
            stockLowGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(3)):
            stockHighGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(4)):
            stockVolumeGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(5)):
            stockOpenGraph([stockConsidered], startD, endD)
    if (int(choiceOfSector) == int(10)):
        utilitiesStocks = stock_Utilities_Sector_10()
        print("Stocks within the Utilities Sector")
        print(utilitiesStocks)
        print("Choose Stock to be considered:")
        stockConsidered = input()
        print("-----Stock Choice = " + stockConsidered)
        print("Choose start date to be considered:")
        startD = input()
        print("-----Start Date = " + startD)
        print("Choose End Date to be considered:")
        endD = input()
        print("-----End Date = " + endD)
        print("Choose what to investigate:")
        print("(1): Daily Price")
        print("(2): Daily Low")
        print("(3): Daily High")
        print("(4): Daily Volume")
        print("(5): Open Price")
        toBeInvestigated = input()
        if (int(toBeInvestigated) == int(1)):
            stockCloseGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(2)):
            stockLowGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(3)):
            stockHighGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(4)):
            stockVolumeGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(5)):
            stockOpenGraph([stockConsidered], startD, endD)
    if (int(choiceOfSector) == int(11)):
        realEstateStocks = stock_RealEstate_Sector_11()
        print("Stocks within the Real Estate Sector")
        print(realEstateStocks)   
        print("Choose Stock to be considered:")
        stockConsidered = input()     
        print("-----Stock Choice = " + stockConsidered)  
        print("Choose start date to be considered:")
        startD = input()
        print("-----Start Date = " + startD)
        print("Choose End Date to be considered:")
        endD = input()
        print("-----End Date = " + endD)  
        print("Choose what to investigate:")
        print("(1): Daily Price")
        print("(2): Daily Low")
        print("(3): Daily High")
        print("(4): Daily Volume")
        print("(5): Open Price")  
        toBeInvestigated = input()
        if (int(toBeInvestigated) == int(1)):
            stockCloseGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(2)):
            stockLowGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(3)):
            stockHighGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(4)):
            stockVolumeGraph([stockConsidered], startD, endD)
        if (int(toBeInvestigated) == int(5)):
            stockOpenGraph([stockConsidered], startD, endD)   


    if (int(choiceOfSector) == int(100)):
        print("Select number for desired choice:")
        print("(1): Compare stocks")   
        print("(2): Find statistics")
        initialChoice = input()
        if (int(initialChoice) == int(1)):
            print("Select number for given category:")
            print("(1): Comparing Daily Close Prices of Stocks")
            print("(2): Comparing Daily Volumes of Stocks")
            print("(3): Comparing Daily Open Prices of Stocks")
            print("(4): Comparing Daily Low Prices of Stocks")
            print("(5): Comparing Daily High Prices of Stocks")
            categoryChoice = input()
            if (int(categoryChoice) == int(1)):
                print("Select Choice for what to obtain:")
                print("(1): Comparing Graphs for Given Daily Close Prices of Stocks")
                print("(2): Difference in Daily Close Prices between stocks")
                obtainedChoice = input()
                if (int(obtainedChoice) == int(1)):
                    print("Enter ticker symbol for stock(1) under consideration:")
                    stock1 = input()
                    print("----- Choice for stock(1) = " + stock1)
                    print("Enter start Date for stock(1):")
                    startD8_1 = input()
                    print("----- Start Date for stock(1) = " + startD8_1)
                    print("Enter End Date for stock(1):")
                    endD8_1 = input()
                    print("----- End Date for stock(1) = " + endD8_1)
                    print("Enter ticker symbol for stock(2) under consideration:")
                    stock2 = input()
                    print("----- Choice for stock(2) = " + stock2)
                    print("Enter Start Date for stock(2):")
                    startD8_2 = input()
                    print("----- Start Date for stock(2) = " + startD8_2)
                    print("Enter End Date for stock(2):")
                    endD8_2 = input()
                    print("----- End Date for stock(2) = " + endD8_2)
                    print("The following gives both plots together")
                    stockCloseCompare([stock1], [stock2], startD8_1, startD8_2, endD8_1, endD8_2)
                if (int(obtainedChoice) == int(2)):
                    return    
            if (int(categoryChoice) == int(2)):
                print("Select Choice for what to obtain:")
                print("(1): Comparing Graphs for Given Daily Volumes of Stocks")
                print("(2): Difference in Daily Volumes between stocks")
                obtainedChoice2 = input()
                if (int(obtainedChoice2) == int(1)):
                    print("Enter ticker symbol for stock(1) under consideration:")
                    stock1 = input()
                    print("----- Choice for stock(1) = " + stock1)
                    print("Enter start Date for stock(1):")
                    startD8_1 = input()
                    print("----- Start Date for stock(1) = " + startD8_1)
                    print("Enter End Date for stock(1):")
                    endD8_1 = input()
                    print("----- End Date for stock(1) = " + endD8_1)
                    print("Enter ticker symbol for stock(2) under consideration:")
                    stock2 = input()
                    print("----- Choice for stock(2) = " + stock2)
                    print("Enter Start Date for stock(2):")
                    startD8_2 = input()
                    print("----- Start Date for stock(2) = " + startD8_2)
                    print("Enter End Date for stock(2):")
                    endD8_2 = input()
                    print("----- End Date for stock(2) = " + endD8_2)
                    print("The following gives both plots together")
                    stockVolumeCompare(stock1, stock2, startD8_1, startD8_2, endD8_1, endD8_2)
                if (int(obtainedChoice2) == int(2)):
                    return 
            if (int(categoryChoice) == int(3)):
                print("Select Choice for what to obtain:")
                print("(1): Comparing Graphs for Given Daily Open Prices of Stocks")
                print("(2): Difference in Daily Open Prices between stocks")
                obtainedChoice3 = input()
                if (int(obtainedChoice3) == int(1)):
                    print("Enter ticker symbol for stock(1) under consideration:")
                    stock1 = input()
                    print("----- Choice for stock(1) = " + stock1)
                    print("Enter start Date for stock(1):")
                    startD8_1 = input()
                    print("----- Start Date for stock(1) = " + startD8_1)
                    print("Enter End Date for stock(1):")
                    endD8_1 = input()
                    print("----- End Date for stock(1) = " + endD8_1)
                    print("Enter ticker symbol for stock(2) under consideration:")
                    stock2 = input()
                    print("----- Choice for stock(2) = " + stock2)
                    print("Enter Start Date for stock(2):")
                    startD8_2 = input()
                    print("----- Start Date for stock(2) = " + startD8_2)
                    print("Enter End Date for stock(2):")
                    endD8_2 = input()
                    print("----- End Date for stock(2) = " + endD8_2)
                    print("The following gives both plots together")
                    stockOpenCompare(stock1, stock2, startD8_1, startD8_2, endD8_1, endD8_2)
                if (int(obtainedChoice3) == int(2)):
                    return 
            if (int(categoryChoice) == int(4)):
                print("Select Choice for what to obtain:")
                print("(1): Comparing Graphs for Given Daily Low Prices of Stocks")
                print("(2): Difference in Daily low Prices between stocks")  
                obtainedChoice4 = input()
                if (int(obtainedChoice4) == int(1)):
                    print("Enter ticker symbol for stock(1) under consideration:")
                    stock1 = input()
                    print("----- Choice for stock(1) = " + stock1)
                    print("Enter start Date for stock(1):")
                    startD8_1 = input()
                    print("----- Start Date for stock(1) = " + startD8_1)
                    print("Enter End Date for stock(1):")
                    endD8_1 = input()
                    print("----- End Date for stock(1) = " + endD8_1)
                    print("Enter ticker symbol for stock(2) under consideration:")
                    stock2 = input()
                    print("----- Choice for stock(2) = " + stock2)
                    print("Enter Start Date for stock(2):")
                    startD8_2 = input()
                    print("----- Start Date for stock(2) = " + startD8_2)
                    print("Enter End Date for stock(2):")
                    endD8_2 = input()
                    print("----- End Date for stock(2) = " + endD8_2)
                    print("The following gives both plots together")
                    stockLowCompare(stock1, stock2, startD8_1, startD8_2, endD8_1, endD8_2)
                if (int(obtainedChoice4) == int(2)):
                    return  
            if (int(categoryChoice) == int(5)):
                print("Select Choice for what to obtain:")
                print("(1): Comparing Graphs for Given Daily High Prices of Stocks")
                print("(2): Difference in Daily high Prices between stocks") 
                obtainedChoice5 = input()
                if (int(obtainedChoice5) == int(1)):
                    print("Enter ticker symbol for stock(1) under consideration:")
                    stock1 = input()
                    print("----- Choice for stock(1) = " + stock1)
                    print("Enter start Date for stock(1):")
                    startD8_1 = input()
                    print("----- Start Date for stock(1) = " + startD8_1)
                    print("Enter End Date for stock(1):")
                    endD8_1 = input()
                    print("----- End Date for stock(1) = " + endD8_1)
                    print("Enter ticker symbol for stock(2) under consideration:")
                    stock2 = input()
                    print("----- Choice for stock(2) = " + stock2)
                    print("Enter Start Date for stock(2):")
                    startD8_2 = input()
                    print("----- Start Date for stock(2) = " + startD8_2)
                    print("Enter End Date for stock(2):")
                    endD8_2 = input()
                    print("----- End Date for stock(2) = " + endD8_2)
                    print("The following gives both plots together")
                    stockHighCompare(stock1, stock2, startD8_1, startD8_2, endD8_1, endD8_2)
                if (int(obtainedChoice5) == int(2)):
                    return     
        if (int(initialChoice) == int(2)):
            print("Select what is wished to be Investigated:")
            print("(1): Daily Difference between Open and Close for Given Stock")
            print("(2): Comparing Daily Differences between stocks")
            investChoice = input()
            if (int(investChoice) == int(1)):
                print("Enter ticker symbol for stock(1) under consideration:")
                stock1 = input()
                print("----- Choice for stock(1) = " + stock1)
                print("Enter start Date for stock(1):")
                startD8_1 = input()
                print("----- Start Date for stock(1) = " + startD8_1)
                print("Enter End Date for stock(1):")
                endD8_1 = input()
                print("----- End Date for stock(1) = " + endD8_1)
                stockDailyDifference(stock1, startD8_1, endD8_1)
            if (int(investChoice) == int(2)):
                print("Enter ticker symbol for stock(1) under consideration:")
                stock1 = input()
                print("----- Choice for stock(1) = " + stock1)
                print("Enter start Date for stock(1):")
                startD8_1 = input()
                print("----- Start Date for stock(1) = " + startD8_1)
                print("Enter End Date for stock(1):")
                endD8_1 = input()
                print("----- End Date for stock(1) = " + endD8_1)
                print("Enter ticker symbol for stock(2) under consideration:")
                stock2 = input()
                print("----- Choice for stock(2) = " + stock2)
                print("Enter Start Date for stock(2):")
                startD8_2 = input()
                print("----- Start Date for stock(2) = " + startD8_2)
                print("Enter End Date for stock(2):")
                endD8_2 = input()
                print("----- End Date for stock(2) = " + endD8_2)
                stockDailyDifferenceCompare(stock1, stock2, startD8_1, startD8_2, endD8_1, endD8_2)
    return 
print(mainStockScript())




#--- Introduce function that resizes 1D arrays, look into shape and how to change shape
#--- if tuple element values are different for different arrays when dates are input 
#--- This might arise for certain stocks on different exchanges and hence, for the same 
#--- difference between start date and end date, the resulting arrays for such will be different



#--- Think about calculating average value of stock prices for sector e.g. for a given date
#--- for all close prices of stocks being considered, calculate avergae to give indication
#--- of how that sector has performed for given date gaps.













