"""
    Função para calcular a distância euclidiana entre dois nós em um grafo.
"""
from networkx import DiGraph

def distancia_euclidiana(n1, n2, grafo: DiGraph) -> float:
    """
        Retorna a distância em linha reta entre dois nós de um grafo.
    """
    x1, y1 = grafo.nodes[n1]['pos']
    x2, y2 = grafo.nodes[n2]['pos']
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
