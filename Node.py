class Node:
   def __init__(self, cities):
       self.name = cities[0]
       self.node_position = (cities[1], cities[2])


   def get_position(self):
       return self.node_position
