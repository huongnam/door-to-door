from node import Node


class Graph:
    def __init__(self):
        self.__nodes = []

    def set_nodes(self, nodes):
        self.__nodes = nodes

    def get_nodes(self):
        return self.__nodes

    # calculate distance between two nodes
    def distance(self, node1, node2):
        pos1 = node1.get_position()
        pos2 = node2.get_position()
        return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2) ** (1/2)

    def total_distance(self, path):
        total_distance = 0
        for i, node in enumerate(path[:-1]):
            total_distance += self.distance(node, path[i + 1])
        return total_distance

    def find_path(self):
        pass

    def print_result(self):
        path = self.find_path()
        display = []
        for node in path:
            display.append(node.get_name())
        print(display)
        print("This covers {} cities and a total distance \
of {}.".format(len(path), self.total_distance(path)))

    # converts the result into the format like the input list
    def rewrite_list(self):
        path = self.find_path()
        new_list = []
        for node in path:
            new_list.append([node.get_name(), node.get_position()[0],
                            node.get_position()[1]])
        return new_list


class NearestNeighbor(Graph):
    def __init__(self):
        super().__init__()

    def find_path(self):
        nodes = self.get_nodes()
        start = nodes[0]
        path = [start]
        nodes.remove(start)
        while nodes:
            next_node = min(nodes, key=lambda node: self.distance(path[-1],
                                                                  node))

            path.append(next_node)
            nodes.remove(next_node)
        return path


class TwoOpt(Graph):
    def __init__(self):
        super().__init__()

    def find_path(self):
        temp = self.get_nodes()
        best = temp
        improved = True
        while improved:
            improved = False
            for i in range(1, len(temp)-2):
                for j in range(i+1, len(temp)):
                    if j-i == 1:
                        # changes nothing, skip then
                        continue
                    # creates a shallow copy of temp
                    new_path = temp[:]
                    new_path[i:j] = temp[j-1:i-1:-1]  # swap
                    # calculate the new total distance and compare it with the
                    # temporary one
                    total_distance = self.total_distance(best)
                    new_total_distance = self.total_distance(new_path)
                    if new_total_distance < total_distance:
                        best = new_path
                        improved = True
            temp = best
        return best
