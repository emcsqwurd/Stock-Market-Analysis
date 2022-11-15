import numpy as np


def readTextFile(path):
    numList = []
    file = open(path, "r") 
    for line in file:
        cleanLine = line.rstrip() # removes newline character
        num = int(cleanLine) # casts to integer type
        numList.append(num) # adds to list
    file.close()
    return numList
#print(readTextFile('rC:\Users\charl\Documents\Projects\Summer 2022'))


#converts integer list input to a text file
def writeIntegerListToTextFile(intList, path):
    outFile = open(path, "w")
    for item in intList:
        outFile.write(str(item) + "\n")
    outFile.close()
    return




def ensureArraySame(array1, array2):
    return 





#-----WRITE ALGORITHM TO FIND ANY PRINT COMMANDS-----



