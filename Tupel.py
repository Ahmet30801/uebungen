def summe_2d_liste(matrix):
    summe= 0
    for zeile in matrix:
        for element in zeile:
            summe += element
    return summe

mtx= [[1,2,3],[4,5,6],[7,8,9]]

ergebnis = summe_2d_liste(mtx)
print (ergebnis)