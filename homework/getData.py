import csv

def getCsvData():
    with open('files/input/data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter='\t') 
        return list(csv_reader)

