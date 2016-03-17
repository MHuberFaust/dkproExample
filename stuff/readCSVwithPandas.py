'''
Created on Jan 11, 2016
read CSV with pandas module
@author: MHuber
'''
import pandas as pd
import csv

df = pd.read_csv("/Users/MHuber/Documents/Dariah/dariah-dkpro-wrapper-0.4.2/Abraham.csv", sep="\t", quoting=csv.QUOTE_NONE)

columns_input = ["Lemma", "NamedEntity"]

df = df[columns_input]

#print(df)
print(df['Lemma'][df['NamedEntity']!='_'])
