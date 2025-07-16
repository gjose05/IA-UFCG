import time
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import statistics   
# Importa a sua implementação do A*
# Certifique-se que o arquivo astar.py está no mesmo diretório ou no PYTHONPATH
from astar import astar
from util.distancia_euclidiana import distancia_euclidiana

def gerar_grafo_grade(dimensao: int):
    """
    Gera um grafo do tipo grade (grid) com pesos e posições nos nós.

    Args:
        dimensao: A dimensão da grade (ex: 10 para uma grade 10x10).

    Returns:
        Um objeto nx.Graph configurado para o teste.
    """
    # Cria uma grade 2D
    G = nx.grid_2d_graph(dimensao, dimensao)

    # Adiciona o atributo de posição a cada nó para a heurística
    for node in G.nodes():
        G.nodes[node]['pos'] = node

    # Adiciona o atributo de peso (weight) em cada aresta
    for edge in G.edges():
        G.edges[edge]['weight'] = 1.0  # Peso uniforme

    return G

def executar_teste_de_carga():
    """
    Executa o teste de carga na função astar, medindo o tempo de execução
    para grafos de tamanhos crescentes.
    """
    # Define as dimensões dos grafos que serão testados
    dimensoes_teste = [10, 20, 30, 40, 50, 75, 100]
    resultados = []

    print("Iniciando teste de carga para o algoritmo A*...")
    print("-" * 50)
    print(f"{'Dimensão':>10} | {'Nós':>8} | {'Arestas':>10} | {'Tempo (s)':>12}")
    print("-" * 50)

    for dim in dimensoes_teste:
        # 1. Geração do Grafo
        grafo = gerar_grafo_grade(dim)
        num_nos = grafo.number_of_nodes()
        num_arestas = grafo.number_of_edges()

        # 2. Definição do início e objetivo
        inicio = (0, 0)
        objetivo = (dim - 1, dim - 1)

        # 3. Definição da heurística
        # A heurística é definida aqui usando uma função lambda para "capturar"
        # a variável 'grafo' do escopo atual, permitindo que a função
        # 'distancia_euclidiana' seja chamada com a assinatura correta (u, v, grafo)
        # sem modificar a sua função astar.
        heuristica_teste = lambda u, v: distancia_euclidiana(u, v, grafo)

        # 4. Medição do tempo
        start_time = time.perf_counter()
        caminho = astar(grafo, inicio, objetivo, heuristica=heuristica_teste)
        end_time = time.perf_counter()

        tempo_execucao = end_time - start_time

        # Validação simples do resultado
        if caminho is None:
            print(f"ATENÇÃO: Não foi encontrado um caminho para a dimensão {dim}x{dim}.")
            continue

        # 5. Armazenamento dos resultados
        resultados.append({
            'dimensao': f"{dim}x{dim}",
            'nos': num_nos,
            'arestas': num_arestas,
            'tempo_s': tempo_execucao
        })

        print(f"{f'{dim}x{dim}':>10} | {num_nos:>8} | {num_arestas:>10} | {tempo_execucao:>12.6f}")

    print("-" * 50)
    print("Teste de carga concluído.")
    return resultados

def plotar_resultados(resultados):
    """
    Plota os resultados do teste de carga usando Matplotlib e Pandas.
    """
    if not resultados:
        print("Nenhum resultado para plotar.")
        return

    df = pd.DataFrame(resultados)

    fig, ax1 = plt.subplots(figsize=(10, 6))

    color = 'tab:red'
    ax1.set_xlabel('Número de Nós no Grafo')
    ax1.set_ylabel('Tempo de Execução (s)', color=color)
    ax1.plot(df['nos'], df['tempo_s'], color=color, marker='o', label='Tempo de Execução')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True)

    fig.tight_layout()
    plt.title('Desempenho do Algoritmo A* vs. Tamanho do Grafo')
    plt.show()


if __name__ == '__main__':
    dados_do_teste = executar_teste_de_carga()
    plotar_resultados(dados_do_teste)