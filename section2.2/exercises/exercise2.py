# transformando o algoritmo do exercise 1 em recursivo


def count_even_num_recursive(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 1 + count_even_num_recursive(n - 1)
    else:
        return count_even_num_recursive(n - 1)


n = 10
print(n, count_even_num_recursive(n))
