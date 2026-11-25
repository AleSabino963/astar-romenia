#Desafios do Arnaldo

#1 - Imprima as cidades que têm exatamente 1 estrada
from Mapa import mapa_romenia, heuristica_bucareste

print('Cidades com apenas uma estrada:')
for cidade in mapa_romenia:
    quantidade = len(mapa_romenia[cidade])
    if quantidade == 1:
        print(f'  {cidade:<15}')


#2 - Imprima as cidades com h(n) menor que 200 km.
print('Cidades com heurística menor que 200 km:')
for cidade in heuristica_bucareste:
    if heuristica_bucareste[cidade] < 200:
        print(f'  {cidade:<15} h(n) = {heuristica_bucareste[cidade]} km')


#3 - Descubra qual é a estrada mais longa do mapa
maisDistante = 0
cidadeOrigem = ''
cidadeDestino = ''

for cidade, vizinhos in mapa_romenia.items():
    for vizinho, distancia in vizinhos:
        if distancia > maisDistante:
            maisDistante = distancia
            cidadeOrigem = cidade
            cidadeDestino = vizinho

print(f'\nA estrada mais longa é de {cidadeOrigem}->{cidadeDestino} com {maisDistante} km de distância\n')