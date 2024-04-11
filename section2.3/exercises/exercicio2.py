# iterative
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encontrar o ponto médio do array
        left_half = arr[:mid]  # Dividir o array na metade esquerda
        right_half = arr[mid:]  # Dividir o array na metade direita

        # Chamadas recursivas para ordenar as duas metades
        merge_sort(left_half)
        merge_sort(right_half)

        # Inicialização dos índices para mesclar
        i = j = k = 0

        # Mesclar as duas metades ordenadamente
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verificar se há elementos restantes na metade esquerda
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Verificar se há elementos restantes na metade direita
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


arr = [7, 3, 5, 4, 6, 8, 2, 1]
print("Array original:", arr)
merge_sort(arr)
print("Array ordenado:", arr)
