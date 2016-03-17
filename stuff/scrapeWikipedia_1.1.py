#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Jan 4, 2016
scrape Wikipedia via author list
@author: MHuber
'''

import wikipedia

# ------------------------------------------------------------
#  Asking for language, set directories
# ------------------------------------------------------------

wikipedia.set_lang(input("Wiki language (for German press enter)? ") or "de")
inputFile = input("File path, please: ")
outputDir = input("Output directory, please: ")

with open(inputFile, "r", encoding='utf-8') as f:
    #authorList = f.readlines()
    for author in list(f):
        print(author)

# ------------------------------------------------------------
#  Skipping errors
# ------------------------------------------------------------

        try:
            pageContent = wikipedia.page(author)
        except wikipedia.exceptions.DisambiguationError:    # Es gibt mehrere Personen mit einem Namen
            pass
        except wikipedia.exceptions.PageError:  # Es gibt keine Seite zum Autor
            continue

        if pageContent:
            print("Check")
        else:
            print("So sad")

# ------------------------------------------------------------
#  Creating a file for each author including the wiki content
# ------------------------------------------------------------

        with open(outputDir+"/"+author, "w", encoding='utf-8') as f:
            f.write(pageContent.content.replace("=", "").replace("==", "").replace("===", "").replace("Bearbeiten", "")) # Markup entfernen eleganter möglich?
            print(author + "---DONE")

# TOTAL 13:22 min für die Liste "Autoren copy.txt" (Liste deutschsprachiger Autoren)
