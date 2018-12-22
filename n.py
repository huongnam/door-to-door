#!/usr/bin/env python3
import sys
from node import Node
from graph import Graph
from timeit import default_timer


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
    start = default_timer()
    cities = get_content(sys.argv[1])
    nodes = [Node(city) for city in cities]
    set_graph(nodes)
    end = default_timer()
    _time = end - start
    print("And it took {}s to find this!".format(_time))
    # print(cities)

    # for city in cites:
    #     city = Node()
    # graph = Graph(cities)


if __name__ == '__main__':
    main()
