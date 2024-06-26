"""
Nathan Swetzof
5/17/24

Create a GraphViz file given an adjacency matrix contained in a tab separated
text file.


"""

import sys, string, pytest

# Create an adjacency matrix based on the contents of a file with the given
#   name, containing tab-separated edge weights
def createMatrix(file_name):
    matrix = []
    row_length = -1
    col_length = 0
    
    with open(file_name, 'r') as file:
        for line in file.readlines():
            row = line.strip('\n').split('\t')
            
            if row_length != len(row):
                if row_length == -1:
                    row_length = len(row)
                else:
                    raise ValueError('Row lengths must all be equal')
                    
            matrix.append(row)
            col_length += 1
        if col_length != row_length and row_length > 0:
            raise ValueError('Not a square matrix.  Row and column lengths must be equal.')
        
    return matrix
    

""" 
GraphBuilder class stores information describing a graph and provides
methods for converting it to GraphViz code
"""
class GraphBuilder:
    LETTER_COUNT = 26
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.digraph = False
        self.edge_symbol = '--'
        self.nodes = []
        
        # check if matrix represents a directed graph
        i = 0
        while not self.digraph and i < len(self.matrix):
            j = 0
            while not self.digraph and j < i:
                if self.matrix[i][j] != self.matrix[j][i]:
                    self.digraph = True
                    self.edge_symbol = '->'
                
                j += 1
            i += 1
        
        for i in range(len(self.matrix)):
            self.nodes.append(self.nodeToString(i))
            
    # Write GraphViz code to the file named with the file_name parameter
    def generateGraph(self, file_name):
        with open(file_name, 'w') as file:
            if self.digraph:
                file.write('digraph {\n')
            else:
                file.write('graph {\n')
            file.write(self.generateNodes(1))
            file.write(self.generateEdges(1))
            file.write('}')
            
    # Return a string representing the nodes in valid GraphViz syntax
    # current_indent applies the given number of indents on each line of the 
    #   returned string to aid in formatting the GraphViz output
    def generateNodes(self, current_indent = 0):
        output = ''
        
        for i in range(len(self.nodes)):
            output += '\t' * current_indent + self.nodes[i] + '\n'
            
        return output
            
    # Return a string representing the set of edges in valid GraphViz syntax
    # current_indent applies the given number of indents on each line of the 
    #   returned string to aid in formatting the GraphViz output
    def generateEdges(self, current_indent = 0):
        output = ''
        max_col = len(self.matrix)
        
        for i in range(len(self.matrix)):
            if not self.digraph:
                max_col = i + 1
            for j in range(max_col):
                if self.matrix[i][j] != '0':
                    output += '\t' * current_indent + \
                        f'{self.nodes[i]} {self.edge_symbol} {self.nodes[j]}\n'
        
        return output
    
    # Helper method converts an integer to a letter representing the node name 
    #   in a graph.  Upon reaching 'Z', an additional letter is added for the 
    #   node name ("AA", "AB", etc.)
    def nodeToString(self, num):
        letters = string.ascii_uppercase
        output = letters[num % self.LETTER_COUNT]
        num = int(num / self.LETTER_COUNT)
        
        while num > 0:
            output += letters[num % self.LETTER_COUNT]
            num = int(num / self.LETTER_COUNT)
        return output

if __name__ == "__main__":
    file_names = ['adj1.txt', 'adj2.txt', 'adj3.txt', 'adj4.txt']
    
    # create GraphViz files
    for file_name in file_names:
        dot_file_name = file_name.split('.')[0] + '.dot'
        matrix = createMatrix(file_name)
        graph = GraphBuilder(matrix)
        graph.generateGraph(dot_file_name)
        print(f"GraphViz file {dot_file_name} created from {file_name}.")
    
    # invoke testing code via pytest
    # "-rA" argument included to list all tests, including passed tests
    sys.exit(pytest.main(["-rA"]))