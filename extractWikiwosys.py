#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Jan 4, 2016
@author: MHuber, SSimmler
Description: Extract information from German Wikipedia and save as txt-file
'''

import wikipedia
import re


def create_authors(working_directory, wiki_page, wiki_section):
    """
    Gathers names from Wikipedia

    :param working_directory: path to the output folder
    :param wiki_page: e.g. Liste deutschsprachiger Lyriker
    :param wiki_section: e.g. 12. Jahrhundert
    :return: authors.txt
    """

    print("\nCreating authors.txt ...")
    with open(working_directory + "/authors.txt", "w", encoding='utf-8') as authors:
        full_content = wikipedia.page(wiki_page)
        selected_content = full_content.section(wiki_section)
        only_name = re.sub("[ \t\r\n\f]+[\(].*?[\)]","", selected_content)  # erases characters after full name
        authors.write(only_name)
        print(only_name)


def crawl_wikipedia(authors_file, output_directory):
    """
    Crawls Wikipedia with the content of authors.txt

    :param authors_file: path to the previously created authors.txt
    :param output_directory: path to the output folder
    :return: {author}.txt
    """

    print("\nCrawling Wikipedia ...")
    with open(authors_file, "r", encoding="utf-8") as authors:
        for author in authors.read().splitlines():
            try:
                page_title = wikipedia.page(author)
                if page_title:
                    with open(output_directory + "/" + author + ".txt", "w", encoding='utf-8') as new_author:
                        new_author.write(page_title.content)
                        print(author + ": saved")

                else:
                    print("So sad")

            except wikipedia.exceptions.DisambiguationError:
                pass
            except wikipedia.exceptions.HTTPTimeoutError:
                pass
            except wikipedia.exceptions.RedirectError:
                pass
            except wikipedia.exceptions.PageError:
                pass


def main(working_directory, wiki_page, wiki_section, output_directory):
    wikipedia.set_lang("de")    # change language
    create_authors(working_directory, wiki_page, wiki_section)
    crawl_wikipedia(working_directory + "/authors.txt", output_directory)

main(r"/Users/MHuber/Documents/Dariah/dkproExample", r"Liste_deutschsprachiger_Lyriker", r"A", r"/Users/MHuber/Documents/Dariah/dkproExample")
