"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.getData import getCsvData

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    letter_sums = {}
    data = getCsvData()
    
    for row in data:
        letter = row[0]  # Get letter from column 1
        values = row[4].split(',')  # Split column 5 into key-value pairs
        
        # Initialize sum for this letter if not exists
        if letter not in letter_sums:
            letter_sums[letter] = 0
            
        # Add all values for this letter
        for pair in values:
            _, value = pair.split(':')  # Split into key:value
            letter_sums[letter] += int(value)
    
    return dict(sorted(letter_sums.items()))
