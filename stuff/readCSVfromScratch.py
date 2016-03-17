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


## xtracts node-names from file names
## file names look like Goethe.txt.csv

def extractBasename(filePath):
    fileName_txt_csv = os.path.basename(filePath)
    fileName_txt = os.path.splitext(fileName_txt_csv)
    fileName = os.path.splitext(fileName_txt[0])
    return fileName[0]

## extracts Named Entities (NE) from a csv-File genereated by dkproWrapper
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


## compares            
def compareNECounter(nedict1,nedict2):
    weight = 0
    for key in nedict1.keys():
        if key in nedict2.keys():
            weight+=1
    print("this is the weight: " + str(weight))
    return weight


## creates a list of authors file titles
## extracts their names: every name is represented as a node
## if there are more than 10 matches between 2 nodes an edge is added
def createGraph():
    G=nx.Graph()
    fileList=glob.glob('/Users/MHuber/Documents/Dariah/dkproExample/testout/*')

    for item in fileList:
        G.add_node(extractBasename(item))
        
    for a,b in itertools.combinations(fileList,2):
        weight = compareNECounter(neCount(a), neCount(b))
        if weight > 10:
            G.add_edge(extractBasename(a), extractBasename(b), {'weight': weight})
            #create edges a->b (weight)

    print ("Number of nodes:", G.number_of_nodes(), "  Number of edges: ", G.number_of_edges())
    return G
    
          

## 
nx.draw_circular(createGraph(), with_labels=True, node_size = 50, font_size=6, center=None)
plt.axis('off')
plt.savefig("graphcircular.png", dpi=200)


