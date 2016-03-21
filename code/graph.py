#!/usr/bin/env python

import csv
from collections import defaultdict
import itertools
import glob
import os
import networkx as nx
import matplotlib.pyplot as plt
import re


def ne_count(input_file):
    """Extracts only Named Entities"""

    ne_counter = defaultdict(int)
    with open(input_file, encoding='utf-8') as csv_file:
        read_csv = csv.DictReader(csv_file, delimiter='\t', quoting=csv.QUOTE_NONE)
        lemma = []

        for row in read_csv:
            if row['NamedEntity'] != "_" and row['CPOS'] != "PUNC":
                lemma.append(row['Lemma'])
            else:
                if lemma:
                    joined_lemma = ' '.join(lemma)
                    ne_counter[joined_lemma] += 1
                    lemma = []
    return ne_counter


def compare_ne_counter(ne_dict1, ne_dict2):
    """Compares two dictionaries"""

    weight = 0
    for key in ne_dict1.keys():
        if key in ne_dict2.keys():
            weight += 1
    print("this is the weight: " + str(weight))
    return weight


def extract_basename(file_path):
    """Extracts names from file names"""

    file_name_txt_csv = os.path.basename(file_path)
    file_name_txt = os.path.splitext(file_name_txt_csv)
    file_name = os.path.splitext(file_name_txt[0])
    return file_name[0]


def create_graph(input_folder):
    """Creates graph including nodes and edges"""

    G = nx.Graph()
    file_list = glob.glob(input_folder)

    for item in file_list:
        G.add_node(extract_basename(item))

    for a, b in itertools.combinations(file_list, 2):
        weight = compare_ne_counter(ne_count(a), ne_count(b))
        if weight > 10:
            G.add_edge(extract_basename(a), extract_basename(b), {'weight': weight})
            # create edges a->b (weight)

    print("Number of nodes:", G.number_of_nodes(), "  Number of edges: ", G.number_of_edges())
    return G


def main(input_folder, output_folder):
    """
    :param input_folder: e.g. /users/networks/csv
    :param output_folder: e.g. /users/networks
    """

    G = create_graph(input_folder + "/*")
    # In case of circular drawing place '#' before every line of the remaining block
    pos = nx.spring_layout(G)
    nx.draw_networkx_labels(G, pos, font_size='8', font_color='r')
    nx.draw_networkx_edges(G, pos, alpha=0.1)
    plt.axis('off')
    plt.savefig(output_folder + "/graph.png")

    # Circular drawing:
    # nx.draw_circular(G, with_labels=True, alpha=0.3, font_size='8')
    # plt.axis('off')
    # plt.savefig(output_folder + "/circular.png")


if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
