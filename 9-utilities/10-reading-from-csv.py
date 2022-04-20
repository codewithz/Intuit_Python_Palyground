import csv

with open("data_products.csv") as file:
    reader=csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)