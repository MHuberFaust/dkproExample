#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Jan 4, 2016
get stuff from German Wikipedia via wikipedia module
txt file is adjusted by hand to disambiguate shit

ToDo: get unique wikipedia links to the authors.
-> best solution probably to parse the html using lxml
@author: MHuber
'''

import wikipedia

#print (wikipedia.summary("Wikipedia"))

# ------------------------------------------------------------
#  Asking the user for some input
# ------------------------------------------------------------

outputFile = input("Set output file directory (incl. name of the file + '.txt'), please: ")
wikipedia.set_lang(input("Wiki language (for German press enter)? ") or "de")
gAuthorList = wikipedia.page(input("Wiki page, please: "))

# ------------------------------------------------------------
#  Extract information and save in the txt-file
# ------------------------------------------------------------

if gAuthorList:
    print(gAuthorList)
    with open(outputFile, "w", encoding='utf-8') as f:
        alphabetList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for letter in alphabetList:
            if gAuthorList.section(letter):
                #print(type(gAuthorList.section(letter)))
                f.write(gAuthorList.section(letter).__add__("\n")) # Garantiert new line nach jedem genannten Autor
                print(gAuthorList.section(letter))