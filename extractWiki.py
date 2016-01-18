#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Jan 4, 2016
@author: MHuber, SSimmler
Description: Extract information from German Wikipedia and save as txt-file
'''

import wikipedia
import re

# ------------------------------------------------------------
#  Asking for input
# ------------------------------------------------------------

wikipedia.set_lang("de")
outputFile = input("Select directory for author list: ")+("/authors.txt")
gAuthorList = wikipedia.page(input("Enter specific Wiki page: "))
wikiSection = input("Select a section of the page: ")
outputDir = input("Select directory for the output files: ")

# ------------------------------------------------------------
#  Extract names and save in ~/authors.txt
# ------------------------------------------------------------

with open(outputFile, "w", encoding='utf-8') as f:
    wikiPage = gAuthorList.section(wikiSection)
    poets = re.sub("[\(\[].*?[\)\]]", "", wikiPage)
    f.write(poets)
    print("\nFollowing authors successfully saved in 'authors.txt':")
    print(poets)

with open(outputFile, "r", encoding='utf-8') as f:
    for author in list(f):
        print(author)

# ------------------------------------------------------------
#  Skipping errors
# ------------------------------------------------------------

        try:
            pageContent = wikipedia.page(author)
        except wikipedia.exceptions.DisambiguationError:
            pass
        except wikipedia.exceptions.PageError:
            continue

        if pageContent:
            print("Check")
        else:
            print("So sad")

# ------------------------------------------------------------
#  Creating a file for each author including the wiki content
# ------------------------------------------------------------

        with open(outputDir+"/"+re.sub("\s", "", author)+".txt", "w", encoding='utf-8') as f:
            f.write(pageContent.content.replace("=", "").replace("==", "").replace("===", "").replace("Bearbeiten", ""))
            print(author + "---DONE\n")
