import fs 
import csv
import json

import pandas as pd

class calculation_of_tax:

    def read_File(self):
        '''
        this function will read the csv file
        '''
        with open('day6/input1.csv', 'r') as file:
            reader = csv.reader(file, delimiter = '\t')
            for row in reader:
                print(row)

    def csv_to_json(self, csvFilePath, jsonFilePath):
        '''
        this function is used to conver csv file to json file
        '''
        jsonArray = []
      
        #read csv file
        with open(csvFilePath, encoding='utf-8') as csvf: 
            #load csv file data using csv library's dictionary reader
            csvReader = csv.DictReader(csvf) 

            #convert each csv row into python dict
            for row in csvReader: 
                #add this python dict to json array
                jsonArray.append(row)
  
        #convert python jsonArray to JSON String and write to file
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
            jsonString = json.dumps(jsonArray, indent=4)
            jsonf.write(jsonString)
          
    def calculate_final_price(self):
        '''
        this function is used for calculation of final price
        '''
        with open('day6/input2.json') as json_file:
            data = json.load(json_file)

        indiatax = data[0]["tax"]
        portuguesetax = data[1]["tax"]
        spaintax = data[2]["tax"]

        indiaProductCost = data[0]["ProductCost"]
        portugueseProductCost = data[1]["ProductCost"]
        spainProductCost = data[2]["ProductCost"]

        df = pd.read_csv("day6/input1.csv")
        ProductSalesTax = [indiatax, portuguesetax, spaintax]
        df ['ProductSalesTax'] = ProductSalesTax
        ProductFinalPrice = [int(indiaProductCost)+ int((int(indiaProductCost)*int(indiatax))/100),int(portugueseProductCost)+ int((int(portugueseProductCost)*int(portuguesetax))/100),int(spainProductCost)+ int((int(spainProductCost)*int(spaintax))/100)]
        df ['ProductFinalPrice'] = ProductFinalPrice
        return df

    def output_to_file(self, df):
        '''
        this function will output the required csv file
        '''
        with open("day6/output10.csv", "w") as file:
            dfd = repr(df)
            file.write(dfd + "\n")


if __name__=='__main__':
    
    c1 = calculation_of_tax()
    csvFilePath = r'day6/input2.csv'
    jsonFilePath = r'day6/input2.json'
    c1.csv_to_json(csvFilePath, jsonFilePath)
    c1.read_File()
    data = c1.calculate_final_price()
    c1.output_to_file(data)

      
