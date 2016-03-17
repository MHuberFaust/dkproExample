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
import re

# ------------------------------------------------------------
#  Asking the user for some input
# ------------------------------------------------------------

outputFile = input("Please select directory and add '/poets.txt': ")
wikipedia.set_lang(input("For German Wikipedia press enter, otherwise select language: ") or "de")
gAuthorList = wikipedia.page(input("Please enter Wiki page (press enter for sample): ") or "Liste deutschsprachiger Lyriker")
century = input("Poets of which century? ")

# ------------------------------------------------------------
#  Extract names and save in ~/poets.txt
# ------------------------------------------------------------

with open(outputFile, "w", encoding="utf-8") as file:
    wikipage = gAuthorList.section(century)
    poets = re.sub("[\(\[].*?[\)\]]", "", wikipage)
    file.write(poets)
    print(poets)
