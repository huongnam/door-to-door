#!/usr/bin/env python3
import sys
from node import Node
from graph import Graph



def get_content(file):
    cities = []
    with open(file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = line.split(',')
        cities.append([line[0], float(line[1]), float(line[2])])
    return cities

def set_graph(nodes):
    graph = Graph()
    graph.set_nodes(nodes)
    graph.print_result()


def main():
    
    cities = get_content(sys.argv[1])
    nodes = [Node(city) for city in cities]
    set_graph(nodes)


    # print(cities)

    # for city in cites:
    #     city = Node()
    # graph = Graph(cities)


if __name__ == '__main__':
    main()
