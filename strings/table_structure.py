""" tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]
output 
   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose
"""

def printTable(tableData):
    # Find max width of each column
    colWidths = [0] * len(tableData)

    for i in range(len(tableData)):
        for item in tableData[i]:
            colWidths[i] = max(colWidths[i], len(item))

    # Print row-wise
    for row in range(len(tableData[0])):
        for col in range(len(tableData)):
            print(tableData[col][row].rjust(colWidths[col]), end=' ')
        print()
