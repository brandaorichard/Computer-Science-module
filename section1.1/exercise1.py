def contains_duplicate(numbers):
    numbers.sort()
    previous_number = "not a number"
    for number in numbers:
        if previous_number == number:
            return True
        previous_number = number

    return False


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(contains_duplicate(numbers))
# Saída esperada: False, pois não há duplicatas

numbers_with_duplicate = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5]
print(contains_duplicate(numbers_with_duplicate))

""" O algoritmo ordena o array independente de qualquer coisa, então
o seu pior caso, melhor caso e caso médio são, no mínimo,
complexidade do algoritmo de ordenação do Python. Vendo a documentação,
vemos que tal algoritmo é O(n log n). Dado que, depois de ordenar, no pior
caso passamos pelo array inteiro uma vez só, isso seria O(n). Assim sendo,
a complexidade é O(n*log(n) + n) o que, simplificando, fica O(n log n)"""
