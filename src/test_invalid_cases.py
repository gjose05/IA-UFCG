import networkx as nx
import pytest

from astar import astar

# Teste pra grafo None
def test_grafo_none():
    path = astar(None, 'A', 'B', heuristica=lambda u, v: 0)
    assert path is None

# Teste para entrada do grafo invalida (nao eh no modelo networkx)
def test_grafo_invalido():
    path = astar("Não é no formato", 'A', 'B', heuristica=lambda u, v: 0)
    assert path is None

# Testes para grafos vazios
def test_grafo_vazio_1():
    G = nx.DiGraph()  
    path = astar(G, 'A', 'B', heuristica=lambda u, v: 0)
    assert path is None

# Teste para nós de inicio invalidos
def test_no_inicial_inexistente_1():
    G = nx.DiGraph()
    G.add_edge('A', 'B')
    path = astar(G, 'C', 'B', heuristica=lambda u, v: 0)
    assert path is None

# Teste para nós de destino invalidos
def test_no_destino_inexistente_1():
    G = nx.DiGraph()
    G.add_edge('A', 'B')
    path = astar(G, 'A', 'C', heuristica=lambda u, v: 0)
    assert path is None

# Testa quando a heuristica é invalida
def test_heuristica_none():
    G = nx.Graph()
    G.add_edge('A', 'B')
    path = astar(G, 'A', 'B', heuristica=lambda u, v: None)
    assert path is None

def test_heuristica_nao_chamavel():
    G = nx.Graph()
    G.add_edge('A', 'B')
    path = astar(G, 'A', 'B', heuristica="não é uma função")
    assert path is None

# Teste de peso invalido
def test_atributo_peso_inexistente():
    G = nx.Graph()
    G.add_edge('A', 'B')
    path = astar(G, 'A', 'B', heuristica=lambda u, v: None)
    assert path is None

#Teste para cooddernadas erradas
def test_coordenadas_invalido_1():
    G = nx.Graph()
    G.add_node('A')  
    G.add_node('B', pos=(0,0))
    path = astar(G, 'A', 'B', heuristica=lambda u, v: 0)
    assert path is None

def test_coordenadas_invalido_2():
    G = nx.Graph()
    G.add_node('A', pos = "0,0")  
    G.add_node('B', pos=(0,0))
    path = astar(G, 'A', 'B', heuristica=lambda u, v: 0)
    assert path is None

def test_coordenadas_invalido_3():
    G = nx.Graph()
    G.add_node('A', pos=(0,0,0))  
    G.add_node('B', pos=(0,0))
    path = astar(G, 'A', 'B', heuristica=lambda u, v: 0)
    assert path is None

def test_coordenadas_invalido_4():
    G = nx.Graph()
    G.add_node('A', pos=None)  
    G.add_node('B', pos=(0,0))
    path = astar(G, 'A', 'B', heuristica=lambda u, v: 0)
    assert path is None

#Teste pra caminho que nao existe
def test_caminho_inexistente_1():
    G = nx.Graph()
    G.add_edge('A', 'B')
    G.add_edge('C', 'D')
    path = astar(G, 'A', 'D', heuristica=lambda u, v: 0)
    assert path is None

def test_caminho_inexistente_2():
    G = nx.Graph()
    G.add_edge('A', 'B')
    G.add_node('C')
    path = astar(G, 'A', 'C', heuristica=lambda u, v: 0)
    assert path is None




