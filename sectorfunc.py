import numpy as np




#example input stocks
Gamestop = ['GME']
Abbvie = ['ABBV']
sp500_ETF = ['SPY']
VIX = ['VIX']


def stockChoiceSample():
    tickernameList = []
    tickernameList.append(Gamestop)
    tickernameList.append(Abbvie)
    tickernameList.append(sp500_ETF)
    tickernameList.append(VIX)
    return tickernameList
#print(stockChoiceSample())


#------------------------------------------------------------------------------


#Sector 1 - Energy 
"""Energy Sector is made up of companies that work in Energy sources
equipment and services e.g. oil and gas companies e.t.c"""


ExxonMobil = ['XOM']
Chevron = ['CVX']
Shell = ['SHEL']
PetroChina = ['PTR']
Gazprom = ['GAZP']
BP = ['BP']

def stock_Energy_Sector_1():
    tickernameList = []
    tickernameList.append(ExxonMobil)
    tickernameList.append(Chevron)
    tickernameList.append(Shell)
    tickernameList.append(PetroChina)
    tickernameList.append(Gazprom)
    tickernameList.append(BP)
    return tickernameList
#print(stock_Energy_Sector_1())    


#Sector 2 - Materials
"""Materials Sector consists of companies that manufacture and market
goods used in manufacturing e.g. chemical companies, construction of 
materials companies, metal making companies e.t.c"""


BHP_Group = ['BHP']
Rio_Tinto_Group = ['RIO']
Vale = ['VALE']
Air_Products_Chemicals = ['APD']
Newmont = ['NEM']


def stock_Materials_Sector_2():
    tickernameList = []
    tickernameList.append(BHP_Group)
    tickernameList.append(Rio_Tinto_Group)
    tickernameList.append(Vale)
    tickernameList.append(Air_Products_Chemicals)
    tickernameList.append(Newmont)
    return tickernameList
#print(stock_Materials_Sector_2())    



#Sector 3 - Industrials
"""Industrials Sector consists of companies across a wide range of goods
and services e.g. construction, engineering companies, transportation,
infrastrucutre e.t.c."""


United_Parcel_service = ['UPS']
Caterpillar = ['CAT']
Automatic_Data_Processing = ['CAT']
Boeing_Company = ['BA']
FEDEX_Corporation = ['FDX']


def stock_Industrials_Sector_3():
    tickernameList = []
    tickernameList.append(United_Parcel_service)
    tickernameList.append(Caterpillar)
    tickernameList.append(Automatic_Data_Processing)
    tickernameList.append(Boeing_Company)
    tickernameList.append(FEDEX_Corporation)
    return tickernameList
#print(stock_Industrials_Sector_3())    



#Sector 4 - Consumer Discretionary
"""Consumer Discretionary Sector consists of companies that produce goods
that consumers want but dont necessarily need e.g. Amazon, Tesla, Home Depot e.t.c"""


Comcast = ['CMCSA']
Walt_Disney = ['DIS']
Nike = ['NKE']
Sony = ['SNE']
Netflix = ['NFLX']
Warner_Bros = ['WBD']
Activision_Blizzard = ['ATVI']


def stock_Consumer_Discretionary_Sector_4():
    tickernameList = []
    tickernameList.append(Comcast)
    tickernameList.append(Walt_Disney)
    tickernameList.append(Nike)
    tickernameList.append(Sony)
    tickernameList.append(Netflix)
    tickernameList.append(Warner_Bros)
    tickernameList.append(Activision_Blizzard)
    return tickernameList
#print(stock_Consumer_Discretionary_Sector_4)    



#Sector 5 - Consumer Staples Sector
"""Consumer Staples Sector consists of companies that maunfacture products
that people view as needs and that sell no matter how the economy is doing, being the
opposite of the Consumer Discretionary Sector, e.g. food, beverages, tobacco, 
household products"""


Walmart = ['WMT']
Coca_cola = ['KO']
PepsiCo = ['PEP']
Costco = ['COST']
Procter_Gamble = ['PG']


def stock_Consumer_Staples_Sector_5():
    tickernameList = []
    tickernameList.append(Walmart)
    tickernameList.append(Coca_cola)
    tickernameList.append(PepsiCo)
    tickernameList.append(Costco)
    tickernameList.append(Procter_Gamble)
    return tickernameList



#Sector 6 - Healthcare Sector
"""Healthcare Sector consists of two categories of companies: healthcare equipment
& services companies and pharmaceutical and biotechnology companies.
e.g. distributions, services, facilities, technology, research, development, and more. """


UnitedHealth = ['UNH']
CVS_Health = ['CVS']
Anthem = ['ANTM']
HCA_Healthcare = ['HCA']
Centene = ['CNC']


def stock_Healthcare_Sector_6():
    tickernameList = []
    tickernameList.append(UnitedHealth)
    tickernameList.append(CVS_Health)
    tickernameList.append(Anthem)
    tickernameList.append(HCA_Healthcare)
    tickernameList.append(Centene)
    return tickernameList


#Sector 7 - Financials Sector
"""Financials Sector consists of companies in areas of finance.  Such industries include
banking, mortgages, financial services, captial markets, insurance and more.  Such companies
include e.g. JPMorgan Chase, Berkshire Hathaway e.t.c"""


JPMorgan = ['JPM']
Citigroup = ['C']
WellsFargo = ['WFC']
BankOfAmerica = ['BAC']
DeutscheBank = ['DB']


def stock_Financial_Sector_7():
    tickernameList = []
    tickernameList.append(JPMorgan)
    tickernameList.append(Citigroup)
    tickernameList.append(WellsFargo)
    tickernameList.append(BankOfAmerica)
    tickernameList.append(DeutscheBank)
    return tickernameList
#print(stock_Financial_Sector_7())


#Sector 8 - Information Technology Sector
"""Information Technology Sector consists of companies involved in the manufacturing, distribution,
market, in addition more of both hardware and software.  Such companies involved include IT services,
Software, Communication, electrical equipment e.t.c."""


Apple = ['AAPL']
Microsoft = ['MSFT']
Google = ['GOOG']
Amazon = ['AMZN']
Tesla = ['TSLA']
Facebook = ['FB']
Adobe = ['ADBE']
Snapchat = ['SNAP']
Twitter = ['TWTR']
Spotify = ['SPOT']


def stock_Information_Tech_Sector_8():
    tickernameList = []
    tickernameList.append(Apple)
    tickernameList.append(Microsoft)
    tickernameList.append(Google)
    tickernameList.append(Amazon)
    tickernameList.append(Tesla)
    tickernameList.append(Facebook)
    tickernameList.append(Adobe)
    tickernameList.append(Snapchat)
    tickernameList.append(Twitter)
    tickernameList.append(Spotify)
    return tickernameList


#Sector 9 - Communication Services Sector
"""Communication Services Sector consists of many companies across two categories of communications:
Telecommunication services and media & entertainment.  The first consists of comapnies regarding
fiber-optic, cable, internet services.  The second consists of companies regarding media and broadcasting
companies, entertainment companies, streaming services, social media e.t.c."""



def stock_Communication_Services_Sector_9():
    return 


#Sector 10 - Utilities Sector
"""Where the Energy Sector includes companies that explore, produce, and store energy sources. 
The utilities sector is made up of those companies that deliver energy sources to consumers. 
It includes electric and gas utilities, water utilities, and many renewable energy companies."""


NextEra_Energy = ['NEE']
Duke_Energy_Corporation = ['DUK']
The_Southern_Company = ['SO']
Dominion_Energy = ['D']
National_Grid = ['NGG']
American_Electric_Power_Company = ['AEP']


def stock_Utilities_Sector_10():
    tickernameList = []
    tickernameList.append(NextEra_Energy)
    tickernameList.append(Duke_Energy_Corporation)
    tickernameList.append(The_Southern_Company)
    tickernameList.append(Dominion_Energy)
    tickernameList.append(National_Grid)
    tickernameList.append(American_Electric_Power_Company)
    return tickernameList



#Sector 11 - Real Estate Sector
"""The Real Estate Sector consists of companies involved in the development and management of 
real estate. A large portion of this sector is made up of real estate investment trusts (REITs), 
but it also includes other real estate leasing, management, and development companies."""


American_Tower_Corporation = ['AMT']
Prologis = ['PLD']
Equinix = ['EQIX']
Public_Storage = ['PSA']
Crown_Castle_International = ['CCI']


def stock_RealEstate_Sector_11():
    tickernameList = []
    tickernameList.append(American_Tower_Corporation)
    tickernameList.append(Prologis)
    tickernameList.append(Equinix)
    tickernameList.append(Public_Storage)
    tickernameList.append(Crown_Castle_International)
    return tickernameList   





