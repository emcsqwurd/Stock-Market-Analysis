import numpy as np




"""Function to obtain column elements from a matrix (yf array)"""
def columnElements(matrix, i):
    desiredColumn = [row[i] for row in matrix]
    return desiredColumn

"""Function to obtain row elements from a matrix (yf array)"""
def rowElements(matrix, i):
    desiredRow = matrix[i, :] 
    return desiredRow

"""Function to obtain the first item from array"""
def firstElementOfArray(array):
    return array[0]

"""Function to obtain last item from array"""
def lastElementOfArray(array):
    return array[-1]



