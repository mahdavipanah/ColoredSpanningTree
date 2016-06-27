# Problem describtion
## Multicolored Spanning Trees (Compulsory)
Suppose that you have a connected, undirected graph G = (V, E) where each edge is colored either red or blue.
Given a number k, you are interested in determining whether there is some spanning tree of G that contains
exactly k blue edges.
* Design a polynomial-time algorithm that finds a spanning tree of G containing the minimum possible number of blue edges. Then:
  * Describe your algorithm.
  * Prove that your algorithm finds a spanning tree of G containing the minimum possible number of blue edges.
  * Prove that your algorithm runs in polynomial time.
* Design an algorithm that finds a spanning tree of G containing the maximum possible number of blue edges. Then:
  * Describe your algorithm.
  * Prove that your algorithm finds a spanning tree of G containing the maximum possible number
  *f blue edges.
  * Prove that your algorithm runs in polynomial time.
* Design an algorithm that, given a number k, determines whether there is a spanning tree of G
that contains exactly k blue edges. Note that you don't need to find such a spanning tree; you just need
to determine whether one exists. Your algorithm should run in time polynomial in n and m (the number
of nodes and edges in G), but not in k. Then:
  * Describe your algorithm.
  * Briefly justify why your algorithm determines whether there is a spanning tree of G containing
  exactly k blue edges. You don't need to write a formal proof here, but should give a one-paragraph
  justification as to why your algorithm works.
  * Briefly justify why your algorithm runs in time polynomial in n and m.


# Project's files

* main.py: First and second problem's section's program.
* k.py: Third section of the problem's program.
* input.py: Reads and writes a graph adjacency matrix from and into a file (used by main.py and k.py)
* tree.py: Functionalities for drawing a tree structure in command line.
* input.txt: Input file which you should place your adjacency matrix of the graph you want to be caluculated in it.
* .gitignore: Files and folders to get ignored by git.



# Input rules

## The first section
Suppose W[i][j] is one of the items in adjacency matrix:

W[i][j] =
* **0** *if i = j*
* **1** *if edge is red*
* **2** *if edge is blue*
* **3** *if there is not edge between v<sub>i</sub> and v<sub>j</sub>*


## The Second section
Suppose W[i][j] is one of the items in adjacency matrix:

W[i][j] =
* **0** *if i = j*
* **1** *if edge is blue*
* **2** *if edge is red*
* **3** *if there is not edge between v<sub>i</sub> and v<sub>j</sub>*


## The third section
Same as first section.


# Prerequisites
* Python2 *(python 2.7 is prefered)*
* [asciitree python package](https://github.com/mbr/asciitree):
```shell
pip2 install asciitree
```

# Useful links
* https://en.wikipedia.org/wiki/Prim%27s_algorithm
* http://stackoverflow.com/questions/21706003/finding-a-spanning-tree-using-exactly-k-red-edges-in-a-graph-with-edges-colored
* https://en.wikipedia.org/wiki/Graph_coloring
* https://en.wikipedia.org/wiki/Spanning_tree
* https://en.wikipedia.org/wiki/Minimum_spanning_tree