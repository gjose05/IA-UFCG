"""Testes utilizando dados reais"""

import networkx as nx
from astar import astar
from util.distancia_euclidiana import distancia_euclidiana

def test_jp_natal():
    """
    Teste simples
    """

    coordenadas = {
    'João Pessoa': (-7.12, -34.86),
    'Campina Grande': (-7.22, -35.89),
    'Recife': (-8.05, -34.88),
    'Natal': (-5.79, -35.21),
    }

    grafo = nx.DiGraph()

    for cidade,pos in coordenadas.items():
        grafo.add_node(cidade, pos=pos)

    grafo.add_edge("João Pessoa","Recife", weight= 116)
    grafo.add_edge("João Pessoa","Natal", weight= 181)
    grafo.add_edge("João Pessoa","Campina Grande", weight= 127)
    grafo.add_edge("Campina Grande","Natal", weight= 286)
    grafo.add_edge("Recife","Natal", weight= 287)

    heuristica = lambda u,v: distancia_euclidiana(u,v,grafo)

    path = astar(grafo,"João Pessoa","Natal", heuristica= heuristica)
    assert path == ["João Pessoa", "Natal"]

def test_patos_campina():
    """
    Teste com dois caminhos diferentes para um percurso de Patos até Campina Grande
    """
    coordenadas = {
    'Patos': (-7.03, -37.28),
    'Campina Grande': (-7.22, -35.89),
    'Santa Luzia': (-6.87, -36.92),
    'Juazeirinho': (-7.07, -36.58),
    'Soledade': (-7.06, -36.37),
    'Areia de Baraúnas': (-7.12, -36.95),
    }

    grafo = nx.DiGraph()

    for cidade,pos in coordenadas.items():
        grafo.add_node(cidade, pos=pos)

    grafo.add_edge("Patos","Santa Luzia", weight= 44)
    grafo.add_edge("Santa Luzia","Juazeirinho", weight= 50)
    grafo.add_edge("Juazeirinho","Soledade", weight= 25)
    grafo.add_edge("Soledade","Campina Grande", weight= 58)
    grafo.add_edge("Areia de Baraúnas","Juazeirinho", weight= 44)
    grafo.add_edge("Patos","Areia de Baraúnas", weight= 48)

    heuristica = lambda u,v: distancia_euclidiana(u,v,grafo)

    path = astar(grafo,"Patos","Campina Grande", heuristica= heuristica)
    assert path == ["Patos","Areia de Baraúnas","Juazeirinho","Soledade","Campina Grande"]

def test_cajazeiras_natal():
    """
    Teste com três caminhos diferentes para um percurso de Cajazeiras até Natal
    """
    coordenadas = {
    'Patos': (-7.03, -37.28),
    'Campina Grande': (-7.22, -35.89),
    'Cajazeiras': (-6.89, -38.46),
    'João Pessoa': (-7.12, -34.86),
    'Natal': (-5.79, -35.21),
    'São Bento': (-6.49, -37.37),
    'Santa Cruz': (-6.22, -35.90),  # Santa Cruz no RN
    'Catolé do Rocha': (-6.34, -37.69),
    'Mossoró': (-5.20, -37.24),
    }

    grafo = nx.DiGraph()

    for cidade,pos in coordenadas.items():
        grafo.add_node(cidade, pos=pos)

    grafo.add_edge("Cajazeiras","Patos", weight= 170)
    grafo.add_edge("Patos","Campina Grande", weight= 177)
    grafo.add_edge("Campina Grande","João Pessoa", weight= 126)
    grafo.add_edge("João Pessoa","Natal", weight= 181)
    grafo.add_edge("Cajazeiras","São Bento", weight= 160)
    grafo.add_edge("São Bento","Santa Cruz", weight= 212)
    grafo.add_edge("Santa Cruz","Natal", weight= 122)
    grafo.add_edge("Cajazeiras","Catolé do Rocha", weight= 138)
    grafo.add_edge("Catolé do Rocha","Mossoró", weight= 152)
    grafo.add_edge("Mossoró","Natal", weight= 280)

    heuristica = lambda u,v: distancia_euclidiana(u,v,grafo)
    path = astar(grafo,"Cajazeiras","Natal", heuristica= heuristica)
    assert path == ["Cajazeiras", "São Bento", "Santa Cruz", "Natal"]
