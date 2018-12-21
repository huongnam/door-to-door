class Node:
    def __init__(self, cities):
        self.__name = cities[0]
        self.__node_position = (cities[1], cities[2])
        self.abc = 0

    def get_name(self):
        return self.__name


    def get_position(self):
        return self.__node_position
