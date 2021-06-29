import csv
import pandas
import fs as fs

csv_rowlist = [["ProductName","ProductCost","Country"], ["ponds",150,"india"],
               ["boro-plus",200,"portuguese"],["himalaya",500,"spain"]]
with open('users.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_rowlist)

with open('users.csv', 'r',) as file:
    reader = csv.reader(file, delimiter = '\t')
    for row in reader:
        print(row)

tax=10
tax2=20
tax3=30
ProductCost = 150
ProductCost2 = 200
ProductCost3 = 500
df = pandas.read_csv("users.csv")
ProductSalesTax = [tax,tax2,tax3]
df ['ProductSalesTax'] = ProductSalesTax
ProductFinalPrice = [int(ProductCost)+ int((ProductCost*tax)/100),int(ProductCost2)+ int((ProductCost2*tax2)/100),int(ProductCost3)+ int((ProductCost3*tax3)/100)]
df ['ProductFinalPrice'] = ProductFinalPrice
print(df)


with open("output10.csv", "w") as file:
    dfd = repr(df)
    file.write(dfd + "\n")




      