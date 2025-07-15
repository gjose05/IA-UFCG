"""
Testes para verificar o fluxo do algoritmo A*.
"""

import networkx as nx
from astar import astar


def test_fila():
    """Testa se a fila de prioridade do A* funciona corretamente."""
    grafo = nx.DiGraph()
    grafo.add_edge('A', 'B', weight=10)
    grafo.add_edge('A', 'C', weight=1)
    grafo.add_edge('C', 'B', weight=1)

    caminho = astar(grafo, 'A', 'B', heuristica=lambda u, v: 0)

    assert caminho == ['A', 'C', 'B']


def test_conta_nos_visitados():
    """Testa se o número de nós visitados está correto."""
    grafo = nx.DiGraph()
    grafo.add_edge('A', 'B', weight=1)
    grafo.add_edge('B', 'C', weight=1)

    caminho = astar(grafo, 'A', 'C', heuristica=lambda u, v: 0)

    assert len(caminho) == 3
    assert set(caminho) == {'A', 'B', 'C'}


def test_reconstrucao_do_caminho():
    """Testa se a reconstrução do caminho funciona corretamente."""
    grafo = nx.DiGraph()
    grafo.add_edge('A', 'B', weight=1)
    grafo.add_edge('B', 'C', weight=1)

    caminho = astar(grafo, 'A', 'C', heuristica=lambda u, v: 0)

    assert caminho == ['A', 'B', 'C']


def test_atualiza_custo_quando_acha_caminho_melhor():
    """Testa se o caminho é atualizado quando é encontrado um caminho de menor custo."""
    grafo = nx.DiGraph()
    grafo.add_edge('A', 'B', weight=3)
    grafo.add_edge('A', 'C', weight=1)
    grafo.add_edge('C', 'B', weight=1)

    caminho = astar(grafo, 'A', 'B', heuristica=lambda u, v: 0)

    assert caminho == ['A', 'C', 'B']
