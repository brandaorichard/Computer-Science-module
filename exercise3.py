# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n.
# Por exemplo:


def print_square(n):
    for row in range(n):
        print(n * "*")


# tamanho_quadrado = int(input("Digite o tamanho do lado do quadrado: "))

square_size = 5
print_square(square_size)
