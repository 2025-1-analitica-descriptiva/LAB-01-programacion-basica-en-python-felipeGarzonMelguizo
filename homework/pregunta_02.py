"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    letter_counts = {}


    with open('files/input/data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter='\t') 
        for row in csv_reader:
            letter = row[0]
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    
    # Convert dictionary to list of tuples and sort
    result = [(letter, count) for letter, count in letter_counts.items()]
    result.sort()
        

    return result

pregunta_02()