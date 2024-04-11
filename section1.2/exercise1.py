# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
def retorna_maior_numero(a, b):
    if a > b:
        return a
    else:
        return b


num1 = 20
num2 = 30
result = retorna_maior_numero(num1, num2)

print("O maior numero eh: ", result)
