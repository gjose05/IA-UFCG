""" Implementa testes funcionais do arquivo astar.py  """

import networkx as nx

from astar                     import astar
from util.distancia_euclidiana import distancia_euclidiana
from util.calcular_custo       import calcular_custo

def test_caminho_simples():
    """
        Testa caminho simples entre dois nós diretamente conectados.
    """
    grafo = nx.DiGraph()
    grafo.add_edge('A', 'B', weight=1)
    path = astar(grafo, 'A', 'B', heuristica=lambda u, v: 0)
    assert path == ['A', 'B']

def test_caminho_com_multiplos_nos():
    """
        Testa caminho linear com múltiplos nós consecutivos.
    """
    grafo = nx.path_graph(['A', 'B', 'C', 'D'])
    nx.set_edge_attributes(grafo, 1, 'weight')
    path = astar(grafo, 'A', 'D', heuristica=lambda u, v: 0)
    assert path == ['A', 'B', 'C', 'D']

def test_caminho_com_multiplas_possibilidades_mesma_distancia():
    """
        Testa grafo com múltiplos caminhos possíveis de mesma distância.
    """
    grafo = nx.DiGraph()
    grafo.add_edge('A', 'B', weight=1)
    grafo.add_edge('B', 'D', weight=1)
    grafo.add_edge('A', 'C', weight=1)
    grafo.add_edge('C', 'D', weight=1)
    path = astar(grafo, 'A', 'D', heuristica=lambda u, v: 0)
    assert calcular_custo(grafo, path) == 2
    assert path[0] == 'A' and path[-1] == 'D'

def test_caminho_com_custo_diferente_nao_curto():
    """
        Testa grafo onde o caminho com maior custo não é o escolhido.
    """
    grafo = nx.DiGraph()
    grafo.add_edge('A', 'B', weight=1)
    grafo.add_edge('B', 'D', weight=1)
    grafo.add_edge('A', 'C', weight=2)
    grafo.add_edge('C', 'D', weight=2)
    path = astar(grafo, 'A', 'D', heuristica=lambda u, v: 0)
    assert path == ['A', 'B', 'D']

def test_caminho_mais_longo_mas_com_menor_custo():
    """
        Testa caminho mais longo em número de nós, porém com menor custo total.
    """
    grafo = nx.DiGraph()
    grafo.add_edge('A', 'B', weight=10)
    grafo.add_edge('B', 'D', weight=10)
    grafo.add_edge('A', 'C', weight=1)
    grafo.add_edge('C', 'E', weight=1)
    grafo.add_edge('E', 'D', weight=1)
    path = astar(grafo, 'A', 'D', heuristica=lambda u, v: 0)
    assert calcular_custo(grafo, path) == 3
    assert path == ['A', 'C', 'E', 'D']

def test_grafo_com_ciclos():
    """
        Testa grafo com ciclos para garantir que algoritmo não entre em loop.
    """
    grafo = nx.cycle_graph(['A', 'B', 'C', 'D'])
    nx.set_edge_attributes(grafo, 1, 'weight')
    path = astar(grafo, 'A', 'C', heuristica=lambda u, v: 0)
    assert calcular_custo(grafo, path) == 2
    assert path[0] == 'A' and path[-1] == 'C'

def test_grafo_com_pesos_iguais():
    """
        Testa grafo completo com todos os pesos iguais.
    """
    grafo = nx.complete_graph(5)
    nx.set_edge_attributes(grafo, 1, 'weight')
    path = astar(grafo, 0, 4, heuristica=lambda u, v: 0)
    assert path[0] == 0 and path[-1] == 4
    assert calcular_custo(grafo, path) == 1

def test_grafo_denso():
    """
        Testa grafo denso com vários nós e arestas.
    """
    grafo = nx.complete_graph(6)
    nx.set_edge_attributes(grafo, 1, 'weight')
    path = astar(grafo, 0, 5, heuristica=lambda u, v: 0)
    assert path[0] == 0 and path[-1] == 5
    assert calcular_custo(grafo, path) == 1

def test_grafo_esparso():
    """
        Testa grafo esparso (caminho linear).
    """
    grafo = nx.path_graph(6)
    nx.set_edge_attributes(grafo, 1, 'weight')
    path = astar(grafo, 0, 5, heuristica=lambda u, v: 0)
    assert path == [0, 1, 2, 3, 4, 5]
    assert calcular_custo(grafo, path) == 5

def test_caminho_com_heuristicaa_euclidiana():
    """
        Testa algoritmo com heurística de distância euclidiana.
    """
    grafo = nx.DiGraph()
    posicoes = {
        'A': (0, 0),
        'B': (1, 1),
        'C': (2, 0),
        'D': (3, 1),
    }
    for node, pos in posicoes.items():
        grafo.add_node(node, pos=pos)
    grafo.add_edge('A', 'B', weight=1.5)
    grafo.add_edge('B', 'D', weight=1.5)
    grafo.add_edge('A', 'C', weight=1)
    grafo.add_edge('C', 'D', weight=1)

    path = astar(grafo, 'A', 'D', heuristica=lambda u, v: distancia_euclidiana(u, v, grafo))
    assert path == ['A', 'C', 'D']
    assert calcular_custo(grafo, path) == 2
