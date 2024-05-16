# -*- coding: utf-8 -*-
"""
Nathan Swetzof
"""

import pytest
from hw6 import GraphBuilder

# @pytest.fixture
# def create_temp_file(tmpdir, name):
#     sub = tmpdir.mkdir('sub')
#     file = sub.join()

class TestGraphBuilder():
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
    
    """ Tests for generateNodes """
    
    
    def test_NodesEmptyGraph(self):
        graph = GraphBuilder(self.empty_graph)
        assert graph.generateNodes() == ''
        
    def testNodesSingleNode(self):
        graph = GraphBuilder(self.single_node)
        assert graph.generateNodes() == 'A\n'
        
    def testNodesDisjointGraph(self):
        graph = GraphBuilder(self.disjoint_graph)
        assert graph.generateNodes() == 'A\nB\n'
        
    def testNodesOneEdge(self):
        graph = GraphBuilder(self.one_edge_digraph)
        assert graph.generateNodes() == 'A\nB\n'
        
    def testNodesSelfEdge(self):
        graph = GraphBuilder(self.self_edge_digraph)
        assert graph.generateNodes() == 'A\nB\n'
        
    def test_EdgesEmptyGraph(self):
        graph = GraphBuilder(self.empty_graph)
        assert graph.generateEdges() == ''
        
    def testEdgesSingleNode(self):
        graph = GraphBuilder(self.single_node)
        assert graph.generateEdges() == ''
        
    def testEdgesDisjointGraph(self):
        graph = GraphBuilder(self.disjoint_graph)
        assert graph.generateEdges() == ''
        
    def testEdgesOneEdge(self):
        graph = GraphBuilder(self.one_edge_digraph)
        assert graph.generateEdges() == 'A -> B\n'
        
    def testEdgesSelfEdge(self):
        graph = GraphBuilder(self.self_edge_digraph)
        edgeSet = set(['B -> A', 'A -> A'])
        edgeString = graph.generateEdges().split('\n')
        assert edgeString[0] in edgeSet
        assert edgeString[1] in edgeSet
        
    # def create_temp_file(self, tmpdir, file_name):
    #     p = tmpdir.join(file_name)
        
    #     yield p.path
    
        