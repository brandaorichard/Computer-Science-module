"""
Você têm dois arrays de números inteiros que representam:

I - instantes de entrada e saídas em uma biblioteca II - um número que
represente um instante a ser buscado.

Retorne quantas pessoas estudantes estão na biblioteca naquele instante.
Considere que todo estudante entrou e saiu da biblioteca.
"""


def count_students_present(arrivals, departures, time_instant):
    students_present = 0
    for i in range(len(arrivals)):
        if arrivals[i] <= time_instant <= departures[i]:
            students_present += 1
    return students_present


arrivals = [1, 2, 3]
departures = [3, 2, 7]
time_instant = 4
print(count_students_present(arrivals, departures, time_instant))


"""
Resposta da análise de complexidade:
O algoritmo realiza um for, portanto possui Complexidade de Tempo O(n)
"""
