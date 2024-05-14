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
    single_node = [1]
    disjoint_graph = [[0, 0],
                      [0, 0]]
    one_edge_digraph = [[0, 1],
                        [0, 0]]
    one_edge_graph = [[0, 1],
                         [1, 0]]
    two_edge_graph = [[0, 1],
                      [1, 0]]
    
    # @pytest.fixture
    # def empty_graph(self, tmpdir):
    #     file_name = 'empty.txt'
    #     with open(file_name, 'w') as file:
    #         file.write('')
            
    #     return file_name
    
    # @pytest.fixture
    # def single_node(self):
    #     file_name = 'single_node.txt'
    #     with open(file_name, 'w') as file:
    #         file.write('0')
            
    #     return file_name
    
    def test_EmptyGraph(self):
        graph = GraphBuilder(self.empty_graph)
        
        assert graph.generateNodes() == ''
        assert graph.generateEdges() == ''
        
    def testSingleNode(self, capfd):
        graph = GraphBuilder(self.single_node)
        
        assert graph.generateNodes() == '1\n'
        assert graph.generateEdges() == ''
        
    def testDisjointGraph(self):
        graph = GraphBuilder(self.disjoint_graph)
        
        assert graph.generateNodes() == '1\n2\n'
        assert graph.generateEdges() == ''
        
    def testOneEdge(self):
        graph = GraphBuilder(self.one_edge_graph)
        
        assert graph.generateNodes() == '1\n2\n'
        assert graph.generateEdges() == '1 -> 2'
        
    # def create_temp_file(self, tmpdir, file_name):
    #     p = tmpdir.join(file_name)
        
    #     yield p.path
    
        