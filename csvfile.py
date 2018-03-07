import csv

def generator():
    with open('phonedata.csv', newline='') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            yield(row)


data = generator()

def returnData():
    return data
