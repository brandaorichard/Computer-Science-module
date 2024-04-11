"""
foi lhe dado a demanda de analisar um array de números inteiros que representam
os produtos dessa empresa. Verifique quantos produtos formam boas combinações,
ou seja, quando um produto é igual ao outro e seu índice é maior que o anterior
Esta combinação pode ser utilizada para modificar os produtos de uma página.
"""


def count_good_pairs(products):
    count = 0
    n = len(products)
    for i in range(n):
        for j in range(i + 1, n):
            if products[i] == products[j] and i < j:
                count += 1
    return count


products1 = [1, 3, 1, 1, 2, 3]
print(count_good_pairs(products1))

products2 = [1, 1, 2, 3]
print(count_good_pairs(products2))


"""
Resposta da análise de complexidade:
O algoritmo realiza um for dentro de outro e possui Complexidade de Tempo O(n²)
"""
