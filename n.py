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


def main():
    cities = get_content(sys.argv[1])
    nodes = [Node(city) for city in cities]

    graph = Graph()
    graph.set_nodes(nodes)
    path = graph.find_path()
    display = []
    for node in path:
        display.append(node.get_name())


    graph.nodes = 'fsdf'
    print(display)
    # print(cities)

    # for city in cites:
    #     city = Node()
    # graph = Graph(cities)


if __name__ == '__main__':
    main()
