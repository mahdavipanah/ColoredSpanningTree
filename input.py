from os import linesep

# Saves a adjacency matrix to a file
def graph_to_file(W, filename):
    filecontent = ""
    for i in range (0, len(W)):
        for j in range (0, len(W)):
            filecontent += str(W[i][j]) + ' '
        filecontent = filecontent.rstrip(' ')
        filecontent += linesep
    filecontent = filecontent.rstrip(linesep)
    try:
        with open(filename, 'w') as text_file:
            text_file.write(filecontent)
    except:
        raise

# Reads a adjacency matrix from a file
def file_to_graph(filename):
    try:
        with open(filename) as input_file:
            lines = input_file.readlines()
            lines = [line.rstrip(linesep) for line in lines]
            W = [line.split(' ') for line in lines]
    except:
        raise
    return W