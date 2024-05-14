"""
Nathan Swetzof
5/##/24
"""

import sys, string, pytest

def createMatrix(file_name):
    matrix = []
    
    with open(file_name, 'r') as file:
            for line in file.readlines():
                matrix.append(line.strip('\n').split('\t'))
                
    return matrix
    

class GraphBuilder:
    LETTER_COUNT = 26
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.digraph = False
        
        # check if matrix represents an undirected graph
        i = 0
        while not self.digraph and i < len(self.matrix):
            j = 0
            while not self.digraph and j < i:
                if self.matrix[i][j] != self.matrix[j][i]:
                    self.digraph = True
                    self.edge_symbol = '->'
                
                j += 1
            i += 1
            
        self.nodes = []
        
        for i in range(len(self.matrix)):
            self.nodes.append(str(i + 1))
            
    def generateGraph(self, file_name):
        with open(file_name, 'w') as file:
            if self.digraph:
                file.write('digraph {\n')
            else:
                file.write('graph {\n')
            file.write(self.generateNodes(1))
            file.write(self.generateEdges(1))
            file.write('}')
            
    def generateNodes(self, current_indent = 0):
        output = ''
        
        for i in range(len(self.nodes)):
            output += '\t' * current_indent + self.nodes[i] + '\n'
            
        return output
            
    def generateEdges(self, current_indent = 0):
        letters = string.ascii_lowercase # TODO: use this, probably move up to affect self.nodes
        output = ''
        max_col = len(self.matrix)
        
        for i in range(len(self.matrix)):
            if not self.digraph:
                max_col = i
            for j in range(max_col):
                if self.matrix[i][j] != '0':
                    output += '\t' * current_indent + \
                        f'{self.nodes[i]} {self.edge_symbol} {self.nodes[j]}\n'
                    
        return output
    
    def __str__(self):
        return self.generateNodes() + self.generateEdges()

if __name__ == "__main__":
    # gb = GraphBuilder('adj4.txt')
    # print(gb.generateEdges())
    # gb.generateGraph("output.dot")
    
    # invoke testing code via pytest
    # "-rA" argument included to list all tests, including passed tests
    sys.exit(pytest.main(["-rA"]))