def find_max_recursive(list):
    if not list:
        return None

    if len(list) == 1:
        return list[0]

    max_rest = find_max_recursive(list[1:])
    return list[0] if list[0] > max_rest else max_rest


array = [1, 3, 9, 5, 8, 7]
print(find_max_recursive(array))

# exemplo da plataforma:
# def maiorinteiro_aux(lista, tamanho):
#     if tamanho == 1:
#         return lista[0]
#     else:
#         maior_do_resto_da_lista = maiorinteiro_aux(lista, tamanho-1)
#         if maior_do_resto_da_lista > lista[tamanho-1]:
#             return maior_do_resto_da_lista
#         else:
#             return lista[tamanho-1]


# def maiorinteiro(lista):
#     tamanho = len(lista)
#     return maiorinteiro_aux(lista, tamanho)


# print(maiorinteiro([1, 21, 300, 4, 57]))
