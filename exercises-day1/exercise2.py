# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
def media_aritmetica(values):
    soma = sum(values)
    media = soma / len(values)
    return media


values_list = [105, 150, 210]
result = media_aritmetica(values_list)
print("A média aritmética é: ", result)
