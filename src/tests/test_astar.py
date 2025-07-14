import pytest
from astar import astar


def vizinhanca(no):
    grafo = {
        'A' : [('B', 1), ('C', 3)],
        'B' : [('D', 1)],
        'C' : [('D', 1)],
        'D' : []
    }
    return grafo.get(no, [])
