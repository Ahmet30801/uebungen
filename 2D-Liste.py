'''
import random
import copy
zeilen=3
spalten=3

ticTacToe= [
    [random.choice(['O','X']) for i in range(spalten)] for i in range(zeilen)]

for row in ticTacToe:
    for elem in row:
        print(elem, end=' ')
    print()'''


#TicTacToe
zeilen=3
spalten=3


tic_tac=[
    ["-"for i in range(spalten)] for x in range(zeilen)]

def printTTT(lst):
    for row in lst:
        for cell in row:
            print(cell, end=' ')
        print()

def setField(lst, para1, para2, para3):
    lst[para2][para3] = para1
    printTTT(lst)


while True:
    xoro = str(input("Type in X or O to put in one of these. "))
    line = int(input("In which line you want to put it? Type 1,2 or 3. "))
    line = line-1
    split = int(input("In which split you want to put it? Type 1,,2 or 3. "))
    split = split-1

    setField(tic_tac, xoro, line, split)

