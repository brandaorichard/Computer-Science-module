def selection_sort(numbers):
    n = len(numbers)  # Quantidade de elementos da lista

    for index in range(n - 1):  # Precisamos ordenar N-1 elementos
        min_element_index = index
        # Definimos a variável para buscar o menor elemento

        for search_index in range(index + 1, n):
            # Início da busca pelo menor elemento
            if numbers[search_index] < numbers[min_element_index]:
                min_element_index = (
                    search_index  # Atualiza o índice atual do menor elemento
                )

        # Troca os elementos de posição
        current_element = numbers[index]
        numbers[index] = numbers[min_element_index]
        numbers[min_element_index] = current_element

    return numbers


numbers = [7, 5, 9, 2, 6, 8]
print(f"Lista inicial: {numbers}")
ordered_numbers = selection_sort(numbers)
print(f"Lista final: {ordered_numbers}")


# Outra maneira de implementar o Selection Sort (com mais recursos Pythônicos):
def search(numbers, start, end):
    min_element = numbers[start]
    min_element_index = start

    for i in range(start + 1, end):  # Busca pelo menor elemento
        if numbers[i] < min_element:
            min_element = numbers[i]
            min_element_index = i

    return min_element_index  # Retorna a posição do menor elemento


def selection_sort(numbers):
    n = len(numbers)

    for index in range(n - 1):  # Início da iteração para ordenar os N-1 elems
        min_element_index = search(numbers, index, n)
        numbers[index], numbers[min_element_index] = (
            numbers[min_element_index],
            numbers[index],
        )  # Trocando os elementos utilizando desempacotamento.

    return numbers


"""
Analisando a complexidade deste algoritmo, vemos que independente de todos os
elementos estarem ordenados (ou não), ou parcialmente ordenados, sempre teremos
que percorrer o array completamente e também n - 1 elementos a cada iteração.
Isto nos leva a uma complexidade O(n²) para todos os casos
(pior, médio, melhor).
"""
