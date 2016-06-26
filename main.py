from random import randint
import sys
import os.path
import input

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
    # Check if all elements

# Use prim algorithm

# Set of edges
nearest = [0 for i in range(1, len(W))]
distance = [W[0][i] for i in range(1, len(W))]
F = []

for k in range(1, len(W)):
    min = 10
    vnear = 0

    for i in range(1, len(W)):
        if 0 <= distance[i - 1] < min:
            min = distance[i - 1]
            vnear = i

    F.append([vnear, nearest[vnear - 1]])
    distance[vnear - 1] = -1

    for i in range(1, len(W)):
        if W[i][vnear] < distance[i - 1]:
            distance[i - 1] = W[i][vnear]
            nearest[i - 1] = vnear

print(F)