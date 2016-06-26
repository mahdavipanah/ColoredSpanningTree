from asciitree import LeftAligned
from collections import OrderedDict as OD

# Return a child nodes of a tree with specific root and edges recursively
def recDraw(root, edges):
    # Check if tree is empty
    if len(edges) < 1:
        return OD()

    # Edges containing root
    rootEdges = [e for e in edges if e[0] == root or e[1] == root]
    # Update edges list and remove edges that contain root
    edges =  [e for e in edges if e[0] != root and e[1] != root]
    # Sorted list of root's child nodes
    childsList = [e[0] if (e[1] == root) else e[1] for e in rootEdges]
    # An ordered list from childs with their subtree
    childs = OD()

    for child in childsList:
        childs[child] = recDraw(child, edges)

    return childs

# Draw a tree from it's edges with a specific root element
def draw(root, edges):
    tree = {root: recDraw(root, edges)}
    tr = LeftAligned()
    print tr(tree)
