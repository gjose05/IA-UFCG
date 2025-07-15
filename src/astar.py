"""Implementação do algoritmo A* para grafos ponderados com heurística."""


import heapq
import networkx as nx
from util.distancia_euclidiana import distancia_euclidiana


def astar(grafo: nx.Graph, inicio, objetivo, heuristica=None, weight='weight') -> list:
    """
    Implementação do algoritmo A*.
    """

    if grafo is None or not isinstance(grafo, nx.Graph) or len(grafo.nodes) == 0:
        return None

    if inicio not in grafo or objetivo not in grafo:
        return None

    if heuristica is None:
        heuristica = heuristica_padrao

    if not callable(heuristica):
        return None

    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, 0, [inicio]))
    visitados = {}

    while fila_prioridade:
        _, g_atual, caminho = heapq.heappop(fila_prioridade)
        atual = caminho[-1]

        if atual == objetivo:
            return caminho

        if atual in visitados and visitados[atual] <= g_atual:
            continue
        visitados[atual] = g_atual

        for vizinho in grafo.neighbors(atual):
            custo_aresta = grafo[atual][vizinho].get(weight, 1)
            if custo_aresta is None:
                continue

            novo_g = g_atual + custo_aresta

            h = heuristica(vizinho, objetivo)
            if h is None:
                continue

            f = novo_g + h
            heapq.heappush(fila_prioridade, (f, novo_g, caminho + [vizinho]))

    return None

def heuristica_padrao(u,v,grafo):
    """
    Implementação de uma heurista_padrao.
    """
    try:
        return distancia_euclidiana(u,v,grafo)
    except (KeyError, TypeError, ValueError):
        return None
