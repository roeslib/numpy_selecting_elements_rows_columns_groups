#to take element, elements, rows or columns from
#an array:

import numpy as np

grades = np.array([[87,96,70],[100,87,90],
                   [94,77,90],[100,81,82]])

print(grades)
print()

#para obtener el elemento de la fila 0 columna 1

print(grades[0,1])
print()

#para obtener los valores de la fila 1

print(grades[1])
print()

#para obtener los valores desde la coluna 0 hasta la columna 1

print(grades[0:2])
print()

#para seleccionar la fila 1 y la fila 3

print(grades[[1,3]])
print()

#si queremos seleccionar todas las filas pero solo desde la
#columna 1 hasta la 2

print(grades[:,1:3])
print()

#si queremos seleccionar todas las filas pero solo la comuna 0

print(grades[:,0])
print()

#si queremos sleccionar todas las filas pero solo las columnas 0
#y 2

print(grades[:,[0,2]])
