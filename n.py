#!/usr/bin/env python3
import sys
import Node
import Graph



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
    print(cities)
    # for city in cites:
    #     city = Node()
    # graph = Graph(cities)


if __name__ == '__main__':
    main()
