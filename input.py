from os import linesep
import re

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
    # Convert list of strings to list of integers
    def strListToint(ls):
        return [int(i) for i in ls]
    pattern = re.compile(r'\s+')
    try:
        with open(filename) as input_file:
            lines = []
            for line in input_file:
                # Check if line is empty
                if re.sub(pattern, '', line) == '':
                    # Stop reading from input file
                    break
                else:
                    # Add line to inputed lines
                    lines.append(line.rstrip(linesep))
            W = [strListToint(line.split(' ')) for line in lines]
    except:
        raise
    return W