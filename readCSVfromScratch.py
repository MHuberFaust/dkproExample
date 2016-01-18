'''
Alternative way of reading the csv-File produced by the dproWrapper version 0.43
author: MHuber

'''
import csv

with open ('/Users/MHuber/Documents/Dariah/dariah-dkpro-wrapper-0.4.2/Abraham.csv', encoding='utf-8') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\t')
    for row in readCSV:
        print(row)
        print(row[1])
        print(row[2])