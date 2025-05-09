"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    column_values = []
    
    with open('files/input/data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter='\t') 
        
        for row in csv_reader:
            column_values.append(int(row[1]))  
            
    return sum(column_values)
