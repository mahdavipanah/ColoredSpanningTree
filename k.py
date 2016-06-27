import sys

# Number of the edges
K = 0
try:
    K = int(raw_input("Enter K: "))
except ValueError:
    sys.exit("Invalid number entered.")

from main import *

# Check if K equals minimum number of 2 weighted edges
if edgesWeights[2] == K:
    print("It is possible.")
    sys.exit(0)

# Check if K is lower than minimum number of required 2 weighted edges
if K < edgesWeights[2]:
    print("It is impossible. Min = " + str(edgesWeights[2]) + ".")
    sys.exit(0)

requiredEdges = [e for e in F if W[e[0]][e[1]] == 2]

# Swaps all 2 and 1 in W
# Because now we want to find the maximum of previous 2 weighted edges
#   so now we swap it's weight to 1 in order to be selected sooner
for i in range(0, len(W)):
    for j in range(i, len(W)):
        if i != j and W[i][j] != 3:
            W[i][j] = W[j][i] = 2 if W[i][j] == 1 else 1

# Set of edges
nearest = [0 for i in range(1, len(W))]
distance = [W[0][i] for i in range(1, len(W))]
F = []
# Number of required additional edges
reqadied = K - edgesWeights[2]

for k in range(1, len(W)):
    min = 3
    vnear = 0

    for i in range(1, len(W)):
        if 0 <= distance[i - 1] < min:
            min = distance[i - 1]
            vnear = i

    if min ==  3:
        sys.exit('There is no spanning tree for this graph.')

    newEdge = [vnear, nearest[vnear - 1]]
    F.append(newEdge)

    # Checks if this new edge is the color we want
    # and also if it's not required
    if W[newEdge[0]][newEdge[1]] == 1 and requiredEdges.count(newEdge) == 0:
        # One new edge found!
        reqadied -= 1
        # Checks if we have reached K
        if reqadied == 0:
            print("It is possible.")
            sys.exit(0)

    distance[vnear - 1] = -1

    for i in range(1, len(W)):
        if W[i][vnear] < distance[i - 1]:
            # Check if the tree should be colored
            if colored:
                # Check if any neighbor edge has the same color
                if any((vnear == e[0] or vnear == e[1])
                       and W[e[0]][e[1]] == W[i][vnear]
                       for e in F):
                    continue
            distance[i - 1] = W[i][vnear]
            nearest[i - 1] = vnear

print("It is impossible.")