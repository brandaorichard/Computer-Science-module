"""
Em um jogo de baralho, as cartas estão representadas por um array numérico.
Para iniciar o jogo, devemos embaralhar as cartas. Faremos isto dividindo uma
porção de cartas em 2 e depois mesclando as duas porções.
"""

#  análise de complexidade:
# O algoritmo realiza um for, portanto possui Complexidade de Tempo O(n)

"""
embora estejamos usando um laço while para iterar sobre as duas partes das
cartas, o número total de iterações não excede o tamanho total do array cards.
Mesmo que as partes possam ter diferentes tamanhos, ainda estamos percorrendo
todas as cartas uma vez para criar o array embaralhado.
"""


def shuffle_cards(cards, cards_per_part):
    mid_index = len(cards) // 2
    part1 = cards[:mid_index]
    part2 = cards[mid_index:]

    shuffled_cards = []
    index1 = 0
    index2 = 0

    while index1 < len(part1) or index2 < len(part2):
        if index1 < len(part1):
            shuffled_cards.append(part1[index1])
            index1 += 1

        if index2 < len(part2):
            shuffled_cards.append(part2[index2])
            index2 += 1

    return shuffled_cards


cards1 = [2, 6, 4, 5]
cards_per_part1 = 2
print(shuffle_cards(cards1, cards_per_part1))

cards2 = [1, 4, 4, 7, 6, 6]
cards_per_part2 = 3
print(shuffle_cards(cards2, cards_per_part2))
