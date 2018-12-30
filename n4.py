def two_opt(route):
2	    for i in range(1, len(route)-2):
3	       for j in range(i+1, len(route)):
4	            new_route = route[:]
5	            new_route[i:j] = route[j-1:i-1:-1] # this is the 2woptSwap
6
7	    return new_route
8
9	print(two_opt(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'A']))
