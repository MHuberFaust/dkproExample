'''
Alternative way of reading the csv-File produced by the dproWrapper version 0.43
author: MHuber

'''
import csv

#POS-Tag: row[9]
#NamedEntity: row[14]

'''
with open ('/Users/MHuber/Documents/Dariah/dariah-dkpro-wrapper-0.4.2/Abraham.csv', encoding='utf-8') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\t')
    print (readCSV)
    for row in readCSV:
        if row[14]!= "_":
        #print(row)
            print(row[7],row[9],row[14] )

            
'''
with open ('/Users/MHuber/Documents/Dariah/dariah-dkpro-wrapper-0.4.2/Abraham.csv', encoding='utf-8') as csvfile:
    readCSV = csv.DictReader(csvfile, delimiter='\t')

    for row in readCSV:
        if row['NamedEntity']!="_" and row['CPOS']!="PUNC":
            print (row['Lemma'], row['POS'],row['NamedEntity'])
