"""
Nathan Swetzof

Tests for hw6.py
The purpose of each test is explained in the comments above the associated
test function.
"""

import pytest
from hw6 import GraphBuilder

class TestGraphBuilder():
    """ Tests for createMatrix function """
    
    empty_file = 'empty.txt'
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
    two_edge_digraph = [['0', '1', '0'],
                        ['0', '0', '1'],
                        ['0', '0', '0']]
    self_edge_digraph = [['1', '0'],
                         ['1', '0']]
    self_edge_graph = [['1', '0'],
                       ['0', '0']]
    
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
        
    
    def testEdgesTwoEdgeDigraph(self):
        graph = GraphBuilder(self.two_edge_digraph)
        edgeSet = set(['A -> B', 'B -> C'])
        edgeStrings = graph.generateEdges().strip().split('\n')
        assert len(edgeStrings) == 2
        assert edgeStrings[0] in edgeSet
        assert edgeStrings[1] in edgeSet
        
    
    def testEdgesSelfEdge(self):
        graph = GraphBuilder(self.self_edge_digraph)
        edgeSet = set(['B -> A', 'A -> A'])
        edgeStrings = graph.generateEdges().strip().split('\n')
        assert len(edgeStrings) == 2
        assert edgeStrings[0] in edgeSet
        assert edgeStrings[1] in edgeSet
    
        