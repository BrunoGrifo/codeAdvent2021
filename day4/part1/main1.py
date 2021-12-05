import pandas as pd

def getIndexes(dfObj, value):
     
    # Empty list
    listOfPos = []
     
    # isin() method will return a dataframe with
    # boolean values, True at the positions   
    # where element exists
    result = dfObj.isin([value])
     
    # any() method will return
    # a boolean series
    seriesObj = result.any()
 
    # Get list of column names where
    # element exists
    columnNames = list(seriesObj[seriesObj == True].index)
    
    # Iterate over the list of columns and
    # extract the row index where element exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
 
        for row in rows:
            listOfPos.append((row, col))
            dfObj.at[row,col] = 0

    # This list contains a list tuples with
    # the index of element in the dataframe
    return listOfPos


def load():
    matrix = []
    column = 0
    dataframe = pd.DataFrame()
    with open("../file.txt", 'r') as file:
        sequence = next(file).strip().split(",")
        for line in file:
            #print(f"Line {column} : {line.strip()}")
            if line.strip():
                dataframe[column] = line.strip().replace("  ", " ").split(" ")
                column += 1
            else:
                column = 0
                matrix.append(dataframe)
                dataframe = pd.DataFrame()

    return sequence, matrix

def getFinalValue():
    return 0

def checkValue(value, matrix):

    for coor in getIndexes(matrix, value):
        if all(isinstance(x, int) for x in matrix.iloc[coor[0]]):
            print(f"Value: {value}")
            matrix = matrix.astype(int)
            print(f"Result: {int(value) * matrix.values.sum()}")
            exit()
        if all(isinstance(x, int) for x in matrix[coor[1]]):
            print(f"Value: {value}")
            matrix = matrix.astype(int)
            print(f"Result: {int(value) * matrix.values.sum()}")
            exit()


def main():
    sequence, data = load()
    for number in sequence:
        for matrix in data:
            checkValue(number, matrix)
        

if __name__ == "__main__":
    main()
    