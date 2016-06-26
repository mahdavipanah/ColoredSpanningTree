from random import randint
import sys
import os.path
import input
import tree

# Check if user wants the result spanning tree to be colored
colored = False
choose = raw_input("Is the spanning tree colored?(yes/no): ").lower()
if choose == "yes" or choose == "y":
    colored = True
# Adjacency matrix
W = []
# Check if user wants a random graph
choose = raw_input("Generate a random graph?(yes/no): ").lower()
if choose == "yes" or choose == "y":
    try:
        vcount = int(raw_input("Number of vertices: "))
    except ValueError:
        sys.exit("Invalid number entered!")
    # Initial all W contents to -1
    W = [[-1 for i in range(0, vcount)] for j in range(0, vcount)]
    # Generate random graph
    print("Generating random graph...")
    for i in range(0, vcount):
        for j in range(0, vcount):
            if i == j :
                W[i][j] = 0
            elif W[i][j] == -1:
                rnd = randint(1, 3)
                W[i][j] = rnd
                W[j][i] = rnd
    # Save to file
    print("Saving random generated graph to file...")
    try:
        input.graph_to_file(W, 'input.txt')
    except:
        sys.exit("Error happend in opening or writing to input file.")
else :
    # Check if file exists
    if not os.path.isfile('input.txt'):
        sys.exit("Input file does not exist.")
    # Read the adjacency matrix from input file
    try:
        W = input.file_to_graph('input.txt')
    except:
        sys.exit("Error happend in opening or reading from input file.")
    # Check W to be valid
    for i in range(0, len(W)):
        for j in range(i, len(W)):
            try:
                if W[i][j] != W[j][i]:
                    raise
                if not 0 <= W[i][j] <= 3:
                    raise
            except:
                sys.exit("Inputed adjacency matrix is not valid. See README.md.")


# Use prim algorithm

# Set of edges
nearest = [0 for i in range(1, len(W))]
distance = [W[0][i] for i in range(1, len(W))]
F = []

for k in range(1, len(W)):
    min = 3
    vnear = 0

    for i in range(1, len(W)):
        if 0 <= distance[i - 1] < min:
            min = distance[i - 1]
            vnear = i

    if min ==  3:
        sys.exit('There is no spanning tree for this graph.')

    F.append([vnear, nearest[vnear - 1]])
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

# Number of 2 weighted edges
edges2 = 0
# Number of 1 weighted edges
edges1 = 0
# Count 1 and 2 weighted edges
for e in F:
    if W[e[0]][e[1]] == 1:
        edges1 += 1
    else:
        edges2 += 1

print("\nNumber of 1 weighted edges: " + str(edges1))
print(  "Number of 2 weighted edges: " + str(edges2))

tree.draw(0, F)