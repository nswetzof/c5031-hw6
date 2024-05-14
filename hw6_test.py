# -*- coding: utf-8 -*-
"""
Nathan Swetzof
"""

import pytest

@pytest.fixture
def tempFile(file_name, contents):
    with open(file_name, 'w') as file:
            file.write("")
            
    return file_name

class TestGraphBuilder():
    empty_graph = ""
    
    
    @pytest.fixture
    def empty_graph():
        file_name = 'empty_graph.txt'
        with open(file_name, 'w') as file:
            file.write("")
            
        return file_name
        