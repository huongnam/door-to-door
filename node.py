class Node:
    def __init__(self, cities):
        self.__name = cities[0]
        self.__y = cities[1]
        self.__x = cities [2]
        self.__node_position = (cities[1], cities[2])


        self.abc = 'haah'
    #
    # def __setattr__(self, property, value):
    #     self.property = value
    #     return





    # def __setattr__(self,__node_position, (cities[1], cities[2])):
    #     return

    def get_name(self):
        return self.__name

    def get_position(self):
        return (self.__y, self.__x)
    #
    # def __getattribute__(self, attr):
    #     return self.name
#
#     # def __getattribute__(self, attr):
#     #     __dict__ = super(Node, self).__getattribute__('__dict__')
#     #     if attr in __dict__:
#     #         return super(Node, self).__getattribute__(attr)
#     #     print(attr.upper())
#     #     return attr.upper()
#
# lst = ['a', 'b', 'c']
# a = Node(lst)
#

class SubNode(Node):
    pass
    # get attribute
# print(a.abc)
