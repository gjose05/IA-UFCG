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

    def heuristica(u, v):
        return distancia_euclidiana(u, v, grafo)

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

    def heuristica(u, v):
        return distancia_euclidiana(u, v, grafo)

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

    def heuristica(u, v):
        return distancia_euclidiana(u, v, grafo)

    path = astar(grafo,"Cajazeiras","Natal", heuristica= heuristica)
    assert path == ["Cajazeiras", "São Bento", "Santa Cruz", "Natal"]

def test_cg_recife():
    """
    Teste com dois caminhos diferentes para um percurso de Campina Grande até Recife
    """
    coordenadas = {
        'Campina Grande': (-7.22, -35.89),
        'João Pessoa': (-7.12, -34.86),
        'Recife': (-8.05, -34.88),
        'Caruaru': (-8.28, -35.97),
        'Vitória de Santo Antão': (-8.12, -35.30),
        'Goiana': (-7.56, -35.00),
    }

    grafo = nx.DiGraph()

    for cidade, pos in coordenadas.items():
        grafo.add_node(cidade, pos=pos)

    grafo.add_edge("Campina Grande", "João Pessoa", weight=125)
    grafo.add_edge("João Pessoa", "Recife", weight=120)
    grafo.add_edge("Campina Grande", "Caruaru", weight=130)
    grafo.add_edge("Caruaru", "Vitória de Santo Antão", weight=52)
    grafo.add_edge("Vitória de Santo Antão", "Recife", weight=50)
    grafo.add_edge("João Pessoa", "Goiana", weight=66)
    grafo.add_edge("Goiana", "Recife", weight=75)

    def heuristica(u, v):
        return distancia_euclidiana(u, v, grafo)

    path = astar(grafo, "Campina Grande", "Recife", heuristica=heuristica)
    assert path == ["Campina Grande", "Caruaru", "Vitória de Santo Antão", "Recife"]


def test_cg_arapiraca_4rotas():
    """
    Teste com quatro caminhos diferentes entre Campina Grande e Arapiraca.
    """
    coordenadas = {
        'Campina Grande': (-7.22, -35.89),
        'Caruaru': (-8.28, -35.97),
        'Garanhuns': (-8.89, -36.50),
        'Palmeira dos Índios': (-9.41, -36.63),
        'Arapiraca': (-9.75, -36.66),
        'Recife': (-8.05, -34.88),
        'Palmares': (-8.68, -35.59),
    }

    grafo = nx.DiGraph()

    for cidade, pos in coordenadas.items():
        grafo.add_node(cidade, pos=pos)

    grafo.add_edge("Campina Grande", "Recife", weight=125)
    grafo.add_edge("Recife", "Palmares", weight=90)
    grafo.add_edge("Palmares", "Garanhuns", weight=100)
    grafo.add_edge("Garanhuns", "Arapiraca", weight=90)
    grafo.add_edge("Campina Grande", "Caruaru", weight=130)
    grafo.add_edge("Caruaru", "Garanhuns", weight=95)
    grafo.add_edge("Caruaru", "Palmeira dos Índios", weight=100)
    grafo.add_edge("Palmeira dos Índios", "Arapiraca", weight=35)
    grafo.add_edge("Palmares", "Palmeira dos Índios", weight=110)

    def heuristica(u, v):
        return distancia_euclidiana(u, v, grafo)

    path = astar(grafo, "Campina Grande", "Arapiraca", heuristica=heuristica)
    assert path == ["Campina Grande", "Caruaru", "Palmeira dos Índios", "Arapiraca"]


def test_cg_fortaleza():
    """
    Teste com cinco caminhos diferentes entre Campina Grande e Fortaleza.
    """
    coordenadas = {
        'Campina Grande': (-7.22, -35.89),
        'João Pessoa': (-7.12, -34.86),
        'Recife': (-8.05, -34.88),
        'Natal': (-5.79, -35.21),
        'Mossoró': (-5.20, -37.33),
        'Cajazeiras': (-6.89, -38.56),
        'Juazeiro do Norte': (-7.21, -39.32),
        'Iguatu': (-6.36, -39.30),
        'Sobral': (-3.68, -40.35),
        'Fortaleza': (-3.73, -38.54),
    }

    grafo = nx.DiGraph()

    for cidade, pos in coordenadas.items():
        grafo.add_node(cidade, pos=pos)

    grafo.add_edge("Campina Grande", "João Pessoa", weight=125)
    grafo.add_edge("João Pessoa", "Natal", weight=180)
    grafo.add_edge("Natal", "Mossoró", weight=280)
    grafo.add_edge("Mossoró", "Fortaleza", weight=420)
    grafo.add_edge("Campina Grande", "Recife", weight=125)
    grafo.add_edge("Recife", "Natal", weight=290)
    grafo.add_edge("Campina Grande", "Cajazeiras", weight=190)
    grafo.add_edge("Cajazeiras", "Juazeiro do Norte", weight=140)
    grafo.add_edge("Juazeiro do Norte", "Iguatu", weight=90)
    grafo.add_edge("Iguatu", "Fortaleza", weight=390)
    grafo.add_edge("Juazeiro do Norte", "Sobral", weight=390)
    grafo.add_edge("Sobral", "Fortaleza", weight=240)
    grafo.add_edge("Campina Grande", "Juazeiro do Norte", weight=370)
    grafo.add_edge("Juazeiro do Norte", "Fortaleza", weight=490)

    def heuristica(u, v):
        return distancia_euclidiana(u, v, grafo)

    path = astar(grafo, "Campina Grande", "Fortaleza", heuristica=heuristica)
    assert path == ["Campina Grande", "Cajazeiras", "Juazeiro do Norte", "Iguatu", "Fortaleza"]


def test_sp_bh():
    """
    Teste com seis caminhos diferentes entre São Paulo e Belo Horizonte.
    """
    coordenadas = {
        'São Paulo': (-23.55, -46.63),
        'Campinas': (-22.90, -47.06),
        'Ribeirão Preto': (-21.17, -47.81),
        'Franca': (-20.54, -47.40),
        'São José dos Campos': (-23.19, -45.88),
        'Taubaté': (-23.02, -45.55),
        'Volta Redonda': (-22.52, -44.10),
        'Resende': (-22.47, -44.45),
        'Juiz de Fora': (-21.76, -43.35),
        'Barbacena': (-21.23, -43.77),
        'Lavras': (-21.25, -45.00),
        'Varginha': (-21.55, -45.43),
        'Belo Horizonte': (-19.92, -43.94),
    }

    grafo = nx.DiGraph()

    for cidade, pos in coordenadas.items():
        grafo.add_node(cidade, pos=pos)

    grafo.add_edge("São Paulo", "Campinas", weight=100)
    grafo.add_edge("Campinas", "Ribeirão Preto", weight=240)
    grafo.add_edge("Ribeirão Preto", "Franca", weight=90)
    grafo.add_edge("Franca", "Belo Horizonte", weight=420)
    grafo.add_edge("Campinas", "Varginha", weight=280)
    grafo.add_edge("Varginha", "Belo Horizonte", weight=300)
    grafo.add_edge("Campinas", "Lavras", weight=270)
    grafo.add_edge("Lavras", "Belo Horizonte", weight=230)
    grafo.add_edge("São Paulo", "São José dos Campos", weight=100)
    grafo.add_edge("São José dos Campos", "Volta Redonda", weight=160)
    grafo.add_edge("Volta Redonda", "Juiz de Fora", weight=190)
    grafo.add_edge("Juiz de Fora", "Belo Horizonte", weight=270)
    grafo.add_edge("São Paulo", "Taubaté", weight=110)
    grafo.add_edge("Taubaté", "Resende", weight=90)
    grafo.add_edge("Resende", "Juiz de Fora", weight=180)
    grafo.add_edge("Juiz de Fora", "Barbacena", weight=90)
    grafo.add_edge("Barbacena", "Belo Horizonte", weight=170)
    grafo.add_edge("Campinas", "Juiz de Fora", weight=300)

    def heuristica(u, v):
        return distancia_euclidiana(u, v, grafo)

    path = astar(grafo, "São Paulo", "Belo Horizonte", heuristica=heuristica)
    assert path == ["São Paulo", "Campinas", "Lavras", "Belo Horizonte"]
