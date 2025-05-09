"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.getData import getCsvData


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    letter_counts = {}

    data = getCsvData()

    for row in data:
        letter = row[0]
        number = row[1]
        letter_counts[letter] = letter_counts.get(letter, 0) + int(number)
    
    result = [(letter, count) for letter, count in letter_counts.items()]
    result.sort()

    return result


