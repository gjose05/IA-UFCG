import networkx as nx
import pytest

from astar                     import astar
from util.distancia_euclidiana import distancia_euclidiana
from util.calcular_custo       import calcular_custo


def test_caminho_simples():
    G = nx.DiGraph()
    G.add_edge('A', 'B', weight=1)
    path = astar(G, 'A', 'B', heuristica=lambda u, v: 0)
    assert path == ['A', 'B']

def test_caminho_com_multiplos_nos():
    G = nx.path_graph(['A', 'B', 'C', 'D'])
    nx.set_edge_attributes(G, 1, 'weight')
    path = astar(G, 'A', 'D', heuristica=lambda u, v: 0)
    assert path == ['A', 'B', 'C', 'D']

def test_caminho_com_multiplas_possibilidades_mesma_distancia():
    G = nx.DiGraph()
    G.add_edge('A', 'B', weight=1)
    G.add_edge('B', 'D', weight=1)
    G.add_edge('A', 'C', weight=1)
    G.add_edge('C', 'D', weight=1)
    path = astar(G, 'A', 'D', heuristica=lambda u, v: 0)
    assert calcular_custo(G, path) == 2
    assert path[0] == 'A' and path[-1] == 'D'

def test_caminho_com_custo_diferente_nao_curto():
    G = nx.DiGraph()
    G.add_edge('A', 'B', weight=1)
    G.add_edge('B', 'D', weight=1)
    G.add_edge('A', 'C', weight=2)
    G.add_edge('C', 'D', weight=2)
    path = astar(G, 'A', 'D', heuristica=lambda u, v: 0)
    assert path == ['A', 'B', 'D']

def test_caminho_mais_longo_mas_com_menor_custo():
    G = nx.DiGraph()
    G.add_edge('A', 'B', weight=10)
    G.add_edge('B', 'D', weight=10)
    G.add_edge('A', 'C', weight=1)
    G.add_edge('C', 'E', weight=1)
    G.add_edge('E', 'D', weight=1)
    path = astar(G, 'A', 'D', heuristica=lambda u, v: 0)
    assert calcular_custo(G, path) == 3
    assert path == ['A', 'C', 'E', 'D']

def test_grafo_com_ciclos():
    G = nx.cycle_graph(['A', 'B', 'C', 'D'])
    nx.set_edge_attributes(G, 1, 'weight')
    path = astar(G, 'A', 'C', heuristica=lambda u, v: 0)
    assert calcular_custo(G, path) == 2
    assert path[0] == 'A' and path[-1] == 'C'

def test_grafo_com_pesos_iguais():
    G = nx.complete_graph(5)
    nx.set_edge_attributes(G, 1, 'weight')
    path = astar(G, 0, 4, heuristica=lambda u, v: 0)
    assert path[0] == 0 and path[-1] == 4
    assert calcular_custo(G, path) == 1

def test_grafo_denso():
    G = nx.complete_graph(6)
    nx.set_edge_attributes(G, 1, 'weight')
    path = astar(G, 0, 5, heuristica=lambda u, v: 0)
    assert path[0] == 0 and path[-1] == 5
    assert calcular_custo(G, path) == 1

def test_grafo_esparso():
    G = nx.path_graph(6)
    nx.set_edge_attributes(G, 1, 'weight')
    path = astar(G, 0, 5, heuristica=lambda u, v: 0)
    assert path == [0, 1, 2, 3, 4, 5]
    assert calcular_custo(G, path) == 5

def test_caminho_com_heuristicaa_euclidiana():
    G = nx.DiGraph()
    posicoes = {
        'A': (0, 0),
        'B': (1, 1),
        'C': (2, 0),
        'D': (3, 1),
    }
    for node, pos in posicoes.items():
        G.add_node(node, pos=pos)
    G.add_edge('A', 'B', weight=1.5)
    G.add_edge('B', 'D', weight=1.5)
    G.add_edge('A', 'C', weight=1)
    G.add_edge('C', 'D', weight=1)

    path = astar(G, 'A', 'D', heuristica=lambda u, v: distancia_euclidiana(u, v, G))
    assert path == ['A', 'C', 'D']
    assert calcular_custo(G, path) == 2

