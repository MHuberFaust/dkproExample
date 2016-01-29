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
import itertools
import glob
import os
import networkx as nx
import matplotlib.pyplot as plt
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
                #print (row['Lemma'], row['POS'],row['NamedEntity'])
            else:
                #fill dict
                if lemma:
                    joinedLemma=' '.join(lemma)
                    #print("this is the Lemma "+joinedLemma)
                    necounter[joinedLemma]+=1
                    lemma=[]
                
        #print(necounter['Sancta Clara'])
    #print(necounter['Sancta Clara'])
    return necounter
    #looks like: {Name:Vorkommen,
    #             Name:Vorkommen} e.g. "Sancta Clara": 5
          
def compareNECounter(nedict1,nedict2):
    weight = 0
    for key in nedict1.keys():
        if key in nedict2.keys():
            weight+=1
    print("this is the weight: " + str(weight))
    return weight


def createGraph():
    
    G=nx.Graph()
    fileList=glob.glob('/Users/MHuber/Documents/Dariah/dkproExample/testout/*')
    
    #print("gimme dad fileList")
    #print(fileList)
    
    #maybe redundant since according to http://snap.stanford.edu/class/cs224w-2012/nx_tutorial.pdf
    #adding edges without nodes results in nx adding nodes automatically
    #G.add_nodes_from(fileList)#is it possible to add a list of strings as nodes?
    for a,b in itertools.combinations(fileList,2):
        print(a, b)
        weight = compareNECounter(neCount(a), neCount(b))
        if weight > 0:
            G.add_edge(a, b, {'weight': weight})
            #create edges a->b (weight)
    
    print ("Number of nodes:", G.number_of_nodes(), "  Number of edges: ", G.number_of_edges())
    return G
    
          
#neCount("/Users/MHuber/Documents/Dariah/dariah-dkpro-wrapper-0.4.2/Abraham.csv")
nx.draw(createGraph())
plt.savefig("graph.png")

