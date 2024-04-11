"""
Crie um algoritmo não recursivo para contar quantos números pares existem em
uma sequência numérica (1 a n).
"""


def count_even_num(n):
    count = 0
    for number in range(n + 1):
        if number % 2 == 0 and number != 0:
            count += 1
    return count


n = 10
print(n, count_even_num(n))
