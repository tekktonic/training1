import csv

def generator():
    with open('phonedata.csv', newline='') as csvfile:
        datareader = csv.reader(csvfile)
        firstline = True
        for row in datareader:
            if firstline:
                firstline = False
                continue
            yield(row)
            
data = generator()

def returnData():
    return data
