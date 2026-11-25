# -*- coding: utf-8 -*-
# fase1_explorar.py — Fase 1: navegar nos dados, sem nenhuma busca ainda.
# Rode com: python fase1_explorar.py

# ----- PASSO 1: trazer os dados do arquivo mapa.py -----
from Mapa import mapa_romenia, heuristica_bucareste


# ----- PASSO 2: quantas cidades existem? -----
print('Quantidade de cidades no mapa:', len(mapa_romenia)) #Mostra número de itens no dicionário, 20.
print('Quantidade de valores de h(n):', len(heuristica_bucareste)) #Mostra número de itens no dicionário, 20.


# ----- PASSO 3: olhar o valor guardado em uma chave -----
vizinhos_arad = mapa_romenia['Arad'] #Coloca todo o conteúdo de Arad do dicionário, para a variável vizinhos_arad.
print() #Pular linha.
print('Vizinhos de Arad:', vizinhos_arad) #Mostra o conteúdo da variável vizinhos_arad, que são os nomes e distâncias dos vizinhos de Arad, registrado no Mapa.py.
print('Tipo do valor:', type(vizinhos_arad)) #Mostra qual o tipo da variável vizinhos_arad, que é uma lista.
print('Tipo do valor:', type(mapa_romenia)) #Mostra qual o tipo da variável mapa_romenia, que é um dicionário.


# ----- PASSO 4: pegar uma tupla e as partes dela -----
primeira = vizinhos_arad[0] #Acopla a primeira tupla da lista vizinhos_arad, que é ('Zerind', 75), para a variável primeira.
print() #Pular linha.
print('Primeira estrada que sai de Arad:', primeira) #Mostra o conteúdo da variável primeira, que é ('Zerind', 75).
print('posição [0] -> cidade vizinha:', primeira[0]) #Mostra o conteúdo da posição 0 da tupla primeira, que é 'Zerind'.
print('posição [1] -> custo em km :', primeira[1]) #Mostra o conteúdo da posição 1 da tupla primeira, que é 75.


# ----- PASSO 5: percorrer a lista com for e desempacotar -----
print() #Pular linha.
print('Estradas que saem de Arad:')
for vizinho, custo in mapa_romenia['Arad']: #Laço de repetição que percorre a lista de tuplas vizinhos_arad, desempacotando cada tupla em duas variáveis respectivamente: vizinho(nome 0) e custo(distancia 1).
    print(' Arad ->', vizinho, '=', custo, 'km') #Lista cada resultado do laço de repetição.


# ----- PASSO 6: percorrer o mapa inteiro ----
print() #Pular linha.
print('Número de estradas de cada cidade:')
for cidade in mapa_romenia: #Laço de repetição que percorre o dicionário mapa_romenia inteiro.
    quantidade = len(mapa_romenia[cidade]) #Calcula o número de estradas para cada cidade.
    print(f'  {cidade:<15} {quantidade} estrada(s)') #Lista cada resultado do laço de repetição, alinhando tudo à esquerda.


# ----- PASSO 7: consultar a heurística ----
print() #Pular linha.
print('h(Arad) =', heuristica_bucareste['Arad'], 'km em linha reta até Bucareste') #Mostra o valor da heurística de Arad até Bucareste.
print('Para cada vizinho de Arad: custo da estrada e h(vizinho)') #Mostra o título da lista.
for vizinho, custo in mapa_romenia['Arad']: #Laço de repetição que percorre a lista de tuplas vizinhos_arad, desempacotando cada tupla em duas variáveis respectivamente: vizinho(nome 0) e custo(distancia 1).
    h = heuristica_bucareste[vizinho] #Adiciona o valor da heurística de cada vizinho para a variável h.
    print(f'  {vizinho:<10} estrada = {custo:>3} km   h = {h:>3} km') #Lista cada resultado do laço de repetição, organizando o texto para exibição.


