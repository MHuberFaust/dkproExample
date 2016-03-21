#!/usr/bin/env python

import wikipedia
import re


def create_authors(working_directory, wiki_page, wiki_section):
    """Gathers names from Wikipedia"""

    print("\nCreating authors.txt ...")
    with open(working_directory + "/authors.txt", "w", encoding='utf-8') as authors:
        full_content = wikipedia.page(wiki_page)
        selected_content = full_content.section(wiki_section)
        only_name = re.sub("[ \t\r\n\f]+[\(\[].*?[\]\)]","", selected_content)  # erases characters after full name
        authors.write(only_name)
        print(only_name)


def crawl_wikipedia(authors_file, output_directory):
    """Crawls Wikipedia with authors.txt"""

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
                    print("Error: Cannot create variable for wikipedia.page")

            except wikipedia.exceptions.DisambiguationError:
                pass
            except wikipedia.exceptions.HTTPTimeoutError:
                pass
            except wikipedia.exceptions.RedirectError:
                pass
            except wikipedia.exceptions.PageError:
                pass


def main(authors_file, output_directory):
    """
    :param authors_file: e.g. /users/networks/my_own_file.txt
    :param output_directory: e.g. /users/networks/wikis
    """

    wikipedia.set_lang("de")    # change language
    crawl_wikipedia(authors_file, output_directory)

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
