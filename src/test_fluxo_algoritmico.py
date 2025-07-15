import pytest
import networkx as nx
from astar import astar


# Teste da fila de prioridade

def test_fila():
    grafo = nx.DiGraph()
    grafo.add_edge('A', 'B', weight=10)  
    grafo.add_edge('A', 'C', weight=1)   
    grafo.add_edge('C', 'B', weight=1)
    
    caminho = astar(grafo, 'A', 'B', heuristica=lambda u, v: 0)

    assert caminho == ['A', 'C', 'B']

# Teste dos nos visitados

def test_conta_nos_visitados():
    grafo = nx.DiGraph()
    grafo.add_edge('A', 'B', weight=1)
    grafo.add_edge('B', 'C', weight=1)
    
    caminho = astar(grafo, 'A', 'C', heuristica=lambda u, v: 0)
    
    assert len(caminho) == 3
    assert set(caminho) == {'A', 'B', 'C'}

# Testa a reconstruçaão do caminho funciona corretamente

def test_reconstrucao_do_caminho():
    grafo = nx.DiGraph()
    grafo.add_edge('A', 'B', weight=1)
    grafo.add_edge('B', 'C', weight=1)
    
    caminho = astar(grafo, 'A', 'C', heuristica=lambda u, v: 0)
    
    assert caminho == ['A', 'B', 'C']

# Testa se o caminho se atualiza corretamente

def test_atualiza_custo_quando_acha_caminho_melhor():
    G = nx.DiGraph()
    G.add_edge('A', 'B', weight=3)
    G.add_edge('A', 'C', weight=1)
    G.add_edge('C', 'B', weight=1)  
    
    caminho = astar(G, 'A', 'B', lambda u, v: 0)
    
    assert caminho == ['A', 'C', 'B']  