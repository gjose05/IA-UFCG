from networkx import DiGraph

def calcular_custo(grafo: DiGraph, caminho: list, peso='weight') -> float:
    """
        retona a soma dos pesos do caminho passado.
    """
    return sum(grafo[u][v][peso] for u, v in zip(caminho[:-1], caminho[1:]))
