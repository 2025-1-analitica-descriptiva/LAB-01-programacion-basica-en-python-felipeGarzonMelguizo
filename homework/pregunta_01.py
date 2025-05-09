"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.getData import getCsvData

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    column_values = []

    data = getCsvData()

    for row in data:
        column_values.append(int(row[1]))  
            
    return sum(column_values)
