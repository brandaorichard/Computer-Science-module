import random


def generate_array(n, m):
    array = []
    for _ in range(100):
        numbers = [random.random() for _ in range(n)]
        array.append(sum(numbers) / n)
    return array


n = 10
array = generate_array(n, 100)
print(array)

""" Mesmo que, para o exemplo dado, o valor de `n` seja muito menor que o valor da constante `100`, para valores de `n` grandes o valor da constante se torna desprezível. Esse problema, então, é `O(n)`. Pelo mesmo motivo, a complexidade de espaço é constante, ou seja, `O(1)`"""
