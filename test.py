import numpy as np
from fundamental import stockDate
from volatility import VolatilityIndicators
from volatilityplots import VolatilityPlots
from fundamental import Fundamental
from investigation import Investigation
import matplotlib.pyplot as plt



vol = VolatilityIndicators()
volPlot = VolatilityPlots()
fun = Fundamental()
inv = Investigation()



def test():
    volitPlot = volPlot.getVol_GKt_Graph('GME')
    return volitPlot
print(test())




