import pytest
import networkx as nx
from astar import astar

def test_grafo_vazio():
    G = nx.Graph()
    with pytest.raises(ValueError):
        astar(G, 'A', 'B')
