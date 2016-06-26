from random import randint
import sys
import os.path
import input

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
    for i in range(0, vcount):
        row = []
        for j in range(0, vcount):
            row.append(-1)
        W.append(row)
    # Generate random graph
    print("Generating random graph...")
    for i in range(0, vcount):
        for j in range(0, vcount):
            if W[i][j] == -1:
                rnd = randint(0, 2)
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
