class Node:
    def __init__(self, cities):
        self.__name = cities[0]
        self.__y = cities[1]
        self.__x = cities[2]

    def get_name(self):
        return self.__name

    def get_position(self):
        return (self.__y, self.__x)
