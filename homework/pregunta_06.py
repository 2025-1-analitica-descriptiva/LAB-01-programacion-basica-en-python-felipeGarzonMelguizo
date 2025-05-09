"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.getData import getCsvData

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    words = {}

    data = getCsvData()

    for row in data:
        dictionary = row[4].split(",")
        for separation in dictionary:
            word, number = separation.split(":")
            number = int(number)
            wordHasValue = words.get(word, False)
            if wordHasValue == False:
                words[word] = [number, None]
            else:
                maximun = max(number,words[word][0])
                minimun = min(number,words[word][1]) if words[word][1] != None else min(number,words[word][0])
                words[word] = [maximun,minimun]
    
    result = [(word, maxAndMin[1],maxAndMin[0]) for word, maxAndMin in words.items()]
    result.sort()

    print(result)

    return result
