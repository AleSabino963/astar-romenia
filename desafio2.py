#Desafios do Arnaldo

# 1 - Calcule o custo de Arad → Timisoara → Lugoj → Mehadia → Drobeta → Craiova → Pitesti → Bucharest

from Mapa import mapa_romenia, heuristica_bucareste


def custo_da_estrada(origem, destino):
    """Devolve os km da estrada origem -> destino, ou None se ela não existe."""
    for vizinho, custo in mapa_romenia[origem]:
        if vizinho == destino:
            return custo
    return None

def custo_do_caminho(caminho):
    """Recebe uma lista de cidades e devolve a soma das estradas, em km."""
    total = 0
    for i in range(len(caminho) - 1):
        total = total + custo_da_estrada(caminho[i], caminho[i + 1])
    return total



cidades = ['Arad', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Pitesti', 'Bucharest']


print('\nCaminho pelas cidades:', ' -> '.join(cidades))
print('Custo =', custo_do_caminho(cidades), 'km')


#2 -  Chame mostrar_g_h_f para esse caminho. Em que cidade o f passa de 418?

def mostrar_g_h_f(caminho):
    """Para cada cidade do caminho imprime g (já andado), h (falta) e f = g + h."""
    print(f'  {"cidade":<15} {"g(n)":>5} {"h(n)":>5} {"f(n)":>5}')
    for i in range(len(caminho)):
        cidade = caminho[i]
        g = custo_do_caminho(caminho[:i + 1])
        h = heuristica_bucareste[cidade]
        f = g + h
        print(f'  {cidade:<15} {g:>5} {h:>5} {f:>5}')

