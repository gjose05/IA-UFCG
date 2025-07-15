"""
Testes para casos inválidos no algoritmo A*.
"""

import networkx as nx
from astar import astar

def test_grafo_none():
    """Testa comportamento quando o grafo é None."""
    path = astar(None, 'A', 'B', heuristica=lambda u, v: 0)
    assert path is None

def test_grafo_invalido():
    """Testa comportamento quando o grafo não é um objeto NetworkX válido."""
    path = astar("Não é no formato", 'A', 'B', heuristica=lambda u, v: 0)
    assert path is None

def test_grafo_vazio_1():
    """Testa comportamento para grafos vazios."""
    grafo = nx.DiGraph()
    path = astar(grafo, 'A', 'B', heuristica=lambda u, v: 0)
    assert path is None

def test_no_inicial_inexistente_1():
    """Testa quando o nó inicial não existe no grafo."""
    grafo = nx.DiGraph()
    grafo.add_edge('A', 'B')
    path = astar(grafo, 'C', 'B', heuristica=lambda u, v: 0)
    assert path is None

def test_no_destino_inexistente_1():
    """Testa quando o nó destino não existe no grafo."""
    grafo = nx.DiGraph()
    grafo.add_edge('A', 'B')
    path = astar(grafo, 'A', 'C', heuristica=lambda u, v: 0)
    assert path is None

def test_heuristica_none():
    """Testa comportamento quando a heurística retorna None."""
    grafo = nx.Graph()
    grafo.add_edge('A', 'B')
    path = astar(grafo, 'A', 'B', heuristica=lambda u, v: None)
    assert path is None

def test_heuristica_nao_chamavel():
    """Testa comportamento quando a heurística não é uma função."""
    grafo = nx.Graph()
    grafo.add_edge('A', 'B')
    path = astar(grafo, 'A', 'B', heuristica="não é uma função")
    assert path is None

def test_atributo_peso_inexistente():
    """Testa comportamento quando o atributo de peso não existe nas arestas."""
    grafo = nx.Graph()
    grafo.add_edge('A', 'B')
    path = astar(grafo, 'A', 'B', heuristica=lambda u, v: None)
    assert path is None

def test_coordenadas_invalido_1():
    """Testa comportamento para nó sem atributo 'pos'."""
    grafo = nx.Graph()
    grafo.add_node('A')
    grafo.add_node('B', pos=(0,0))
    path = astar(grafo, 'A', 'B', heuristica=lambda u, v: 0)
    assert path is None

def test_coordenadas_invalido_2():
    """Testa comportamento para nó com atributo 'pos' em formato errado."""
    grafo = nx.Graph()
    grafo.add_node('A', pos="0,0")
    grafo.add_node('B', pos=(0,0))
    path = astar(grafo, 'A', 'B', heuristica=lambda u, v: 0)
    assert path is None

def test_coordenadas_invalido_3():
    """Testa comportamento para nó com atributo 'pos' com dimensão incorreta."""
    grafo = nx.Graph()
    grafo.add_node('A', pos=(0,0,0))
    grafo.add_node('B', pos=(0,0))
    path = astar(grafo, 'A', 'B', heuristica=lambda u, v: 0)
    assert path is None

def test_coordenadas_invalido_4():
    """Testa comportamento para nó com atributo 'pos' None."""
    grafo = nx.Graph()
    grafo.add_node('A', pos=None)
    grafo.add_node('B', pos=(0,0))
    path = astar(grafo, 'A', 'B', heuristica=lambda u, v: 0)
    assert path is None

def test_caminho_inexistente_1():
    """Testa comportamento quando não existe caminho entre os nós."""
    grafo = nx.Graph()
    grafo.add_edge('A', 'B')
    grafo.add_edge('C', 'D')
    path = astar(grafo, 'A', 'D', heuristica=lambda u, v: 0)
    assert path is None

def test_caminho_inexistente_2():
    """Testa comportamento quando um nó está isolado."""
    grafo = nx.Graph()
    grafo.add_edge('A', 'B')
    grafo.add_node('C')
    path = astar(grafo, 'A', 'C', heuristica=lambda u, v: 0)
    assert path is None
