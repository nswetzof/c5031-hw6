"""
Nathan Swetzof

Tests for hw6.py
The purpose of each test is explained in the comments above the associated
test function.
"""

import pytest, os
from hw6 import GraphBuilder, createMatrix

class TestGraphBuilder():    
    empty_file = 'empty.txt'
    unequal_row_file = 'unequalrows.txt'
    non_square_file = 'nonsquare.txt'
    square_matrix_file = 'square.txt'
    
    empty_graph = []
    single_node = [['0']]
    disjoint_graph = [['0', '0'],
                      ['0', '0']]
    one_edge_digraph = [['0', '1'],
                        ['0', '0']]
    two_edge_graph = [['0', '1'],
                      ['1', '0']]
    self_edge_digraph = [['1', '0'],
                         ['1', '0']]
    self_edge_graph = [['1', '0'],
                       ['0', '0']]
    
    """ Tests for createMatrix function """
    
    def test_CreateMatrixEmpty(self):
        m = createMatrix(self.empty_file)
        assert m == []
        
    def test_CreateMatrixUnequalRows(self):
        with pytest.raises(ValueError, match='Row lengths must all be equal'):
            createMatrix(self.unequal_row_file)
            
    def test_CreateMatrixNonSquare(self):
        with pytest.raises(ValueError, \
                           match=r'Not a square matrix.  Row and column lengths must be equal.'):
            createMatrix(self.non_square_file)
            
    def test_CreateMatrixSquare(self):
        m = createMatrix(self.square_matrix_file)
        assert m == [['1', '0'], ['0', '0']]
    
    """ Tests for generateNodes() """
    
    # Ensure no nodes are created and no invalid array accesses are performed
    def test_NodesEmptyGraph(self):
        graph = GraphBuilder(self.empty_graph)
        assert graph.generateNodes() == ''
    
    # Verify one node is created
    def testNodesSingleNode(self):
        graph = GraphBuilder(self.single_node)
        assert graph.generateNodes() == 'A\n'
        
    # Verify multiple nodes are correctly generated
    def testNodesMultipleNodes(self):
        graph = GraphBuilder(self.disjoint_graph)
        assert graph.generateNodes() == 'A\nB\n'
        
    """ Tests for generateEdges() """
    
    # Ensure no edges are created and no invalid array accesses are performed
    def test_EdgesEmptyGraph(self):
        graph = GraphBuilder(self.empty_graph)
        assert graph.generateEdges() == ''
        
    # Ensure no edges are created in a non-empty graph
    def testEdgesSingleNode(self):
        graph = GraphBuilder(self.single_node)
        assert graph.generateEdges() == ''
        
    # Ensure no edges are created in a non-empty graph with multiple nodes
    def testEdgesDisjointGraph(self):
        graph = GraphBuilder(self.disjoint_graph)
        assert graph.generateEdges() == ''
        
    # Ensure edges are created in a graph with a single edge
    #   and that graph is treated as a digraph with the correct notation for edges
    def testEdgesOneEdge(self):
        graph = GraphBuilder(self.one_edge_digraph)
        assert graph.generateEdges() == 'A -> B\n'
        
    # Ensure one edge is created in a graph with two edges in the adjacency
    #   matrix between the same two nodes.  Two separate edges are not needed
    #   in an undirected graph between the same two nodes.
    # Verify correct edge notation
    def testEdgesTwoEdgeGraph(self):
        graph = GraphBuilder(self.two_edge_graph)
        edgeSet = set(['B -- A', 'A -- B'])
        edgeStrings = graph.generateEdges().strip().split('\n')
        assert len(edgeStrings) == 1
        assert edgeStrings[0] in edgeSet
        
    # Ensure that self edges are included in a digraph
    def testEdgesSelfEdgeDigraph(self):
        graph = GraphBuilder(self.self_edge_digraph)
        edgeSet = set(['B -> A', 'A -> A'])
        edgeStrings = graph.generateEdges().strip().split('\n')
        assert len(edgeStrings) == 2
        assert edgeStrings[0] in edgeSet
        assert edgeStrings[1] in edgeSet
    
    # Ensure that self edges are included in an undirected graph
    def testEdgesSelfEdgeGraph(self):
        graph = GraphBuilder(self.self_edge_graph)
        assert graph.generateEdges() == 'A -- A\n'
        
    """ Tests for generateGraph() """
    
    # Ensure that no nodes or edges are written to the output file from an empty
    #   graph
    def testGraphEmptyGraph(self):
        graph = GraphBuilder(self.empty_graph)
        expected = 'graph {\n}'
        actual = ''
        
        graph.generateGraph('test.dot')
        
        with open('test.dot', 'r') as file:
            actual = file.read()
            
        assert actual == expected
        
    # Ensure the graph is correctly labeled as a digraph and outputs the nodes
    #   and edges in the proper format
    def testGraphDigraph(self):
        graph = GraphBuilder(self.one_edge_digraph)
        expected = 'digraph {\n\tA\n\tB\n\tA -> B\n}'
        actual = ''
        
        graph.generateGraph('test.dot')
        
        with open('test.dot', 'r') as file:
            actual = file.read()
            
        assert actual == expected
       
    # Ensure the graph is correctly labeled as a graph and outputs the nodes
    #   and edges in the proper format
    def testGraphUndirectedGraph(self):
        graph = GraphBuilder(self.two_edge_graph)
        expected = 'graph {\n\tA\n\tB\n\tB -- A\n}'
        actual = ''
        
        graph.generateGraph('test.dot')
        
        with open('test.dot', 'r') as file:
            actual = file.read()
            
        assert actual == expected
        