import pytest
import networkx as nx
from astar import a_star

def test_grafo_vazio():
    G = nx.Graph()
    with pytest.raises(ValueError):
        a_star(G, 'A', 'B')
