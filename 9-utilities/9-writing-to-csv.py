import csv

with open("data_products.csv","w",newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["transaction_id","product_id","price"])
    writer.writerow([1000,1,15])
    writer.writerow([1002,10,22])
    writer.writerow([1003,12,43])
    writer.writerow([1004,43,12])
    writer.writerow([1005,54,13])