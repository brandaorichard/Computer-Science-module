# Exercício 4: Crie uma função que receba uma lista de nomes e retorne
# o nome com a maior quantidade de caracteres.


def find_biggest_name(names):
    biggest_name = names[0]
    for name in names:
        if len(name) > len(biggest_name):
            biggest_name = name
    return biggest_name


print(find_biggest_name(["ric", "xin", "bibi"]))
