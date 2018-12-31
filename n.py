#!/usr/bin/env python3
from argparse import ArgumentParser
from node import Node
from graph import Graph, NearestNeighbor, TwoOpt
from timeit import default_timer
from sys import stderr


def process_argparse():
    parser = ArgumentParser()
    parser.add_argument('F', help='file containing a list of cities to visit',
                        type=str)
    parser.add_argument('--algo', help='specify which algorithm to use for\
                        finding path among [nearest_neighbor|two_opt|both],\
                        default both', type=str, default='both')
    return parser.parse_args()


# reads the file and returns a list with city name and its latitude, longitude
def get_content(file):
    cities = []
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.split(',')
            cities.append([line[0], float(line[1]), float(line[2])])
        return cities
    except Exception:
        stderr.write("Invalid file")


def main():
    # sets start time
    start = default_timer()
    args = process_argparse()
    cities = get_content(args.F)
    nodes = [Node(city) for city in cities]
    graph = Graph()
    if "both" in args.algo:
        # runs Nearest Neighbor algorithm first
        graph = NearestNeighbor()
        graph.set_nodes(nodes)
        # converts the result of Nearest Neighbor algorithm into the format
        # like the previous list
        nearest_neighbor_result = graph.rewrite_list()
        nodes = [Node(city) for city in nearest_neighbor_result]
        graph = TwoOpt()
    elif "nearest_neighbor" in args.algo:
        print("nearest neighbor")
        graph = NearestNeighbor()
    elif "two_opt" in args.algo:
        print("two opt")
        graph = TwoOpt()
    graph.set_nodes(nodes)
    graph.print_result()
    # sets end time
    end = default_timer()
    _time = end - start
    print("And it took {}s to find this!".format(_time))


if __name__ == '__main__':
    main()
