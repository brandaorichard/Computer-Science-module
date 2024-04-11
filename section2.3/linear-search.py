def linear_search(numbers, target):
    n = len(numbers)  # N será a quantidade de elementos da lista
    for index in range(0, n):  # vamos iterar a lista completa
        if numbers[index] == target:
            # se encontrar o elemento alvo, retorne a posição
            return index

    return -1  # Não encontrou? Retorne -1


print(linear_search([1, 2, 3], 2))  # saída: 1
print(linear_search([1, 2, 3], 4))  # saída: -1

"""
A busca linear pode ser simples, mas não necessariamente será a solução mais
rápida, já que ela faz uma verificação de todos os elementos para encontrar
qual é o correspondente.
"""

"""
O algoritmo linear_search, no pior caso (se o elemento estiver na última
posição ou não existir), precisará percorrer toda a estrutura para encontrar o
elemento. Diante disso, sua complexidade é O(n). No entanto, o algoritmo de
linear_search não necessita que a coleção esteja ordenada.
"""
