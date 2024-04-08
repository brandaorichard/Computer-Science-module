def insertion_sort(numbers):
    n = len(numbers)  # Quantidade de elementos na lista

    for index in range(1, n):  # Começaremos a ordenar pelo segundo elemento
        key = numbers[index]
        # Pegamos o segundo elemento e o definimos como chave

        new_position = index - 1
        # Tomamos a posição anterior para iniciar a comparação

        while (
            new_position >= 0 and numbers[new_position] > key
        ):  # Enquanto a chave for menor, remaneja o elemento para frente
            numbers[new_position + 1] = numbers[new_position]
            # Remaneja o elemento
            new_position = new_position - 1

        numbers[new_position + 1] = key  # Insere a chave na posição correta

    return numbers


numbers = [7, 5, 9, 2, 6, 8]
print(insertion_sort(numbers))

"""
Como precisamos percorrer cada um dos elementos e depois percorrer comparando
os elementos à esquerda do mesmo, em um pior caso, onde a lista esteja
inversamente ordenada, teremos uma complexidade de O(n²). Isto se repete
também em média, para listas parcialmente ordenadas. Porém, se inicialmente a
lista estiver ordenada, este algoritmo terá complexidade O(n), pois só fará a
iteração de todos os elementos, e não precisará ficar remanejando os
elementos.
"""
