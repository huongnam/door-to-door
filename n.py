#!/usr/bin/env python3
import argparse
from node import Node
from graph import Graph, NearestNeighbor, TwoOpt
from timeit import default_timer

def process_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo', help='specify which algorithm to use for\
                        finding path among [nearest_neighbor|two_opt],\
                        default nam', type=str, default='nam')
    parser.add_argument('F', help='a file containing a list of cities to visit',
                        type=str)
    return parser.parse_args()


def get_content(file):
    cities = []
    with open(file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = line.split(',')
        cities.append([line[0], float(line[1]), float(line[2])])
    return cities


# def set_graph(nodes):
#     graph = Graph()
#     graph.set_nodes(nodes)
#     graph.print_result()


def main():
    start = default_timer()
    args = process_argparse()
    cities = get_content(args.F)
    nodes = [Node(city) for city in cities]
    # graph = NearestNeighbor()
    # print(type(graph))
    # graph = []
    graph = Graph()
    if args.algo == "nam":
        graph = NearestNeighbor()
        graph.set_nodes(nodes)
        new = graph.find_path()
        graph = TwoOpt()
        graph.set_nodes(new)
    elif args.algo == "nearest_neighbor":
        print("nearest_neighbor")
        graph = NearestNeighbor()
    elif args.algo == "two_opt":
        print("two_opt")
        graph = TwoOpt()

    graph.set_nodes(nodes)
    graph.print_result()
    end = default_timer()
    _time = end - start
    print("And it took {}s to find this!".format(_time))
    # print(cities)

    # for city in cities:
    #     city = Node()
    # graph = Graph(cities)



    # lst = args.N
    # if args.gui and len(lst) > 15:
    #     too_large()
    #     exit()
    # if check(lst) == 'Sorted':
    #     if args.algo == 'merge':
    #         merge_sort(lst)
    #     if args.algo == 'quick':
    #         quick_sort(lst, 0, len(lst) - 1)
    #     else:
    #         exit()


if __name__ == '__main__':
    main()
