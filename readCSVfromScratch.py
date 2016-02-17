'''
Alternative way of reading the csv-File produced by the dproWrapper version 0.42
author: MHuber

'''



import csv
from collections import defaultdict
import itertools
import glob
import os
import networkx as nx
import matplotlib.pyplot as plt
import re
from turtledemo.__main__ import font_sizes

def neCount(inputfile):
    necounter=defaultdict(int)
    with open (inputfile, encoding='utf-8') as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter='\t', quoting=csv.QUOTE_NONE)
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

def extractBasename(filePath):
    newItem = os.path.basename(filePath)
    newerItem = os.path.splitext(newItem)
    newerNewerItem = os.path.splitext(newerItem[0])
    return newerNewerItem[0]

def createGraph():
    #regex =
    G=nx.Graph()
    fileList=glob.glob('/Users/MHuber/Documents/Dariah/dkproExample/testout/*')
    
    #print("gimme dad fileList")
    #print(fileList)
    for item in fileList:
        G.add_node(extractBasename(item))
        
    for a,b in itertools.combinations(fileList,2):
        weight = compareNECounter(neCount(a), neCount(b))
        if weight > 10:
            G.add_edge(extractBasename(a), extractBasename(b), {'weight': weight})
            #create edges a->b (weight)

    print ("Number of nodes:", G.number_of_nodes(), "  Number of edges: ", G.number_of_edges())
    return G
    
          


nx.draw_circular(createGraph(), with_labels=True, node_size = 50, font_size=6, center=None)
plt.axis('off')
plt.savefig("graphcircular1.png", dpi=200)
#nx.draw_spring(createGraph(), with_labels=True, node_size = 50, font_size=6)
#plt.axis('off')
#plt.savefig("graphspring.png", dpi=200)

