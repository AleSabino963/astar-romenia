# -*- coding: utf-8 -*
# fase2_caminhos.py — Fase 2: funções, custo de um caminho e os valores g, h e f.
# Rode com:  python fase2_caminhos.py


# ----- PASSO 1: importar os dados ----
from Mapa import mapa_romenia, heuristica_bucareste


# ----- PASSO 2: função que devolve o custo de UMA estrada ----
def custo_da_estrada(origem, destino): #Cidade origem e cidade destino.
    """Devolve os km da estrada origem -> destino, ou None se ela não existe."""
    for vizinho, custo in mapa_romenia[origem]: #Pega o vizinho e o custo da cidade denominada Origem.
        if vizinho == destino: #Se o valor da variável vizinho for igual ao valor destino, retorna o custo do caminho.
            return custo
    return None


# ----- PASSO 3: função que soma o custo de um caminho inteiro ----
def custo_do_caminho(caminho): #Calcula o caminho de uma lista criada, por exemplo, a variável por_fagaras que lista as cidades do dicionário.
    """Recebe uma lista de cidades e devolve a soma das estradas, em km."""
    total = 0 # Para somar uma por uma, é necessário sempre resetar o valor da variável total
    for i in range(len(caminho) - 1): #Tira 1, pois são 4 cidades com 3 estradas ligando uma na outra.
        total = total + custo_da_estrada(caminho[i], caminho[i + 1]) # Soma o custo da estrada entre caminho[i] (Alguma Cidade) e caminho[i+1] (Próxima cidade). Alocando na variável total.
    return total


# ----- PASSO 4: testar as funções ----
print('Arad -> Sibiu custa', custo_da_estrada('Arad', 'Sibiu'), 'km')
print('Arad -> Bucharest custa', custo_da_estrada('Arad', 'Bucharest'), '(não existe estrada direta)')

por_fagaras = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest'] # Cria variável e aloca a lista de cidades para o caminho por Fagaras.
por_pitesti = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest'] # Cria variável e aloca a lista de cidades para o caminho por Pitesti.

print(f'\n Número do contador em len(por_fagaras) = {len(por_fagaras)}') # Testando se o Arnaldo é mentiroso ou não.

print('\nCaminho por Fagaras:', ' -> '.join(por_fagaras)) # Prática de formatação para não precisar digitar a seta para cada item. Lógica: note que "' -> '.join(por_fagaras" não foram separados por vírgula. .Join() é um comando para o texto seta.
print('   custo =', custo_do_caminho(por_fagaras), 'km')
print('Caminho por Pitesti:', ' -> '.join(por_pitesti))
print('   custo =', custo_do_caminho(por_pitesti), 'km')


# ----- PASSO 5: g(n), h(n) e f(n) ao longo de um caminho ----
def mostrar_g_h_f(caminho):
    """Para cada cidade do caminho imprime g (já andado), h (falta) e f = g + h."""
    print(f'  {"cidade":<15} {"g(n)":>5} {"h(n)":>5} {"f(n)":>5}')
    for i in range(len(caminho)):
        cidade = caminho[i] # Puxa cada cidade da lista a ser chamada, no caso a lista da variável 'por_fagaras', uma por vez.
        g = custo_do_caminho(caminho[:i + 1]) # Para passar para a próxima cidade, é necessário pegar o caminho de todas as cidades anteriores (:i) e somar com a próxima (i+1).
        h = heuristica_bucareste[cidade] # Puxa a heuristica da cidade atualmente sendo processada, até Bucareste.
        f = g + h
        print(f'  {cidade:<15} {g:>5} {h:>5} {f:>5}') # Alinhamento de cada item, < esquerda, > direita, :n caracteres reservados, preenchendo com espaços quando vazio, para manter alinhado.



print('\nValores ao longo do caminho por Fagaras:')
mostrar_g_h_f(por_fagaras)

print('\nValores ao longo do caminho por Pitesti:')
mostrar_g_h_f(por_pitesti)