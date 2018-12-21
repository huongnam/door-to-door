from node import Node

class Graph:
    def __init__(self):
        self.__nodes = []


    def set_nodes(self, nodes):
        self.__nodes = nodes


    def get_nodes(self):
        return self.__nodes


    def distance(self, node1, node2):
        pos1 = node1.get_position()
        pos2 = node2.get_position()
        return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2) ** (1/2)


    def find_path(self):
        nodes = self.get_nodes()
        start = nodes[0]
        path = [start]
        nodes.remove(start)
        while nodes:
            next_node = min(nodes, key=lambda node: self.distance(path[-1], node))

            path.append(next_node)
            nodes.remove(next_node)
        return path

    def total_distance(self, path):
        pass

    def print_result(self):
        path = self.find_path()
        display = []
        for node in path:
            display.append(node.get_name())
        print(display)
