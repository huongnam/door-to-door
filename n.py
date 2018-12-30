#!/usr/bin/env python3
from argparse import ArgumentParser
from node import Node
from graph import Graph, NearestNeighbor, TwoOpt
from timeit import default_timer
from sys import stderr

def process_argparse():
    parser = ArgumentParser()
    parser.add_argument('F', help='a file containing a list of cities to visit',
                        type=str)
    parser.add_argument('--algo', help='specify which algorithm to use for\
                        finding path among [nearest_neighbor|two_opt],\
                        default nam', type=str, default='nam')
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
        exit()



# def set_graph(nodes):
#     graph = Graph()
#     graph.set_nodes(nodes)
#     graph.print_result()


def main():
    # sets start time
    start = default_timer()
    args = process_argparse()
    cities = get_content(args.F)
    nodes = [Node(city) for city in cities]
    # graph = NearestNeighbor()
    # print(type(graph))
    # graph = []
    graph = Graph()
    if "nam" in args.algo:
        graph = NearestNeighbor()
        graph.set_nodes(nodes)
        new = graph.find_path()

        graph = TwoOpt()
        graph.set_nodes(new)
    elif "nearest_neighbor" in args.algo:
        print("nearest_neighbor")
        graph = NearestNeighbor()
    elif "two_opt" in args.algo:
        print("two_opt")
        graph = TwoOpt()

    graph.set_nodes(nodes)
    print("toi set")


    graph.print_result()
    print("toi print")
    # print(graph.rewrite_list())
    print("toi viet")
    # sets end time
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
