"""
Nathan Swetzof
5/##/24
"""

import string

class Graph:
    def __init__(self, file_name):
        self.digraph = False
        self.matrix = []
        
        with open(file_name, 'r') as file:
            for line in file.readlines():
                self.matrix.append(line.strip('\n').split('\t'))
                
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
    
    def isDigraph(self):
        return self.digraph
    

class GraphBuilder:
    LETTER_COUNT = 26
    
    def __init__(self, graph):
        self.graph = graph
        
        if graph.isDigraph():
            self.graph_type = 'digraph'
            self.edge_symbol = '->'
        else:
            self.graph_type = 'graph'
            self.edge_symbol = '--'
            
        self.nodes = []
        
        for i in range(len(graph.matrix)):
            self.nodes.append(str(i + 1))
        
    # def createMatrix(self, file_name):
    #     with open(file_name, 'r') as file:
    #         for line in file.readlines():
    #             self.matrix.append(line.strip('\n').split('\t'))
            
    def generateGraph(self, file_name):
        with open(file_name, 'w') as file:
            file.write(f'{self.graph_type} {{\n')
            file.write(self.generateNodes(1))
            file.write(self.generateEdges(1))
            file.write('}')
            
    def generateNodes(self, current_indent = 0):
        output = ''
        
        for i in range(len(self.nodes)):
            output += '\t' * current_indent + self.nodes[i] + '\n'
            
        return output
            
    def generateEdges(self, current_indent = 0):
        m = self.graph.matrix
        letters = string.ascii_lowercase # TODO: use this, probably move up to affect self.nodes
        output = ''
        max_col = len(m)
        
        for i in range(len(m)):
            if not self.graph.isDigraph():
                max_col = i
            for j in range(max_col):
                if m[i][j] != '0':
                    output += '\t' * current_indent + \
                        f'{self.nodes[i]} {self.edge_symbol} {self.nodes[j]}\n'
                    
        return output

if __name__ == "__main__":
    g = Graph('adj4.txt')
    gb = GraphBuilder(g)
    print(gb.generateEdges())
    gb.generateGraph("output.dot")