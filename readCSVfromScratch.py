'''
Alternative way of reading the csv-File produced by the dproWrapper version 0.43
author: MHuber

'''

#Schleife bauen, die B-per und I-Per zusammenfasst und in einem dict ablegt
#
#Vorannahme, dass Personennamen im Text zumindest durch ein Satzzeichen getrennt sind
#nur eine Kombination aus B-Per und mindeste 1 I-Per wird als Name gespeichert
##wegen: "Matthäus Megerle und dessen Frau Ursula ->B-BPer (geborene Wagner->BPer)"

#für jeden Text eine Datei in einem Graphendatenformat abspeichern? o. on the fly generieren?
#Gewichtungen sollten bestenfalls gleich hier vorgenommen werden

'''
Weitere Vorgehensweise:
    1. für jedes dict einen Knoten erstellen
    2. dicts vergleichen, bei Match Kante von dict zu dict erstellen
    3. Graph zeichnen

'''

#POS-Tag: row[9]
#NamedEntity: row[14]
import csv
from collections import defaultdict
'''
with open ('/Users/MHuber/Documents/Dariah/dariah-dkpro-wrapper-0.4.2/Abraham.csv', encoding='utf-8') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\t')
    print (readCSV)
    for row in readCSV:
        if row[14]!= "_":
        #print(row)
            print(row[7],row[9],row[14] )

            
'''


def neCount(inputfile):
    necounter=defaultdict(int)
    with open (inputfile, encoding='utf-8') as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter='\t')
        lemma =[]
        
        for row in readCSV:
            if row['NamedEntity']!="_" and row['CPOS']!="PUNC":
                lemma.append(row['Lemma'])
                print (row['Lemma'], row['POS'],row['NamedEntity'])
            else:
                #fill dict
                if lemma:
                    joinedLemma=' '.join(lemma)
                    print("this is the Lemma "+joinedLemma)
                    necounter[joinedLemma]+=1
                    lemma=[]
                
        #print(necounter['Sancta Clara'])
    #print(necounter['Sancta Clara'])
    return necounter
          
          
          
neCount("/Users/MHuber/Documents/Dariah/dariah-dkpro-wrapper-0.4.2/Abraham.csv")      