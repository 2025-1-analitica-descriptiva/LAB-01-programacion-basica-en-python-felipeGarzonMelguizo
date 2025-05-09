"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.getData import getCsvData

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    letters = {}

    data = getCsvData()

    for row in data:
        letter = row[0]
        number = int(row[1])
        letterHasValue = letters.get(letter, False)
        if letterHasValue == False:
            letters[letter] = [number, None]
        else:
            maximun = max(number,letters[letter][0])
            minimun = min(number,letters[letter][1]) if letters[letter][1] != None else min(number,letters[letter][0])
            letters[letter] = [maximun,minimun]

    
    result = [(letter, maxAndMin[0],maxAndMin[1]) for letter, maxAndMin in letters.items()]
    result.sort()

    return result
