from random import shuffle
from counter import Counter


def selection_sort(array):
    for i in range(len(array)):
        minimum = i

        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        array[minimum], array[i] = array[i], array[minimum]

    return array


def insertion_sort(array):
    for i in range(len(array)):
        current_value = array[i]
        cur_pos = i

        while cur_pos > 0 and array[cur_pos - 1] > current_value:
            array[cur_pos] = array[cur_pos - 1]
            cur_pos -= 1

        array[cur_pos] = current_value

    return array


algorithms = [selection_sort, insertion_sort]

for algorithm in (insertion_sort, selection_sort):
    algorithm_name = algorithm.__name__

    for input in (10_000, 100_000, 1_000_000):

        sorted_numbers = list(range(input))
        reversed_sorted_numbers = list(reversed(sorted_numbers))
        random_numbers = sorted_numbers[:]  # copia dos ordenados
        shuffle(random_numbers)  # embaralha eles

        with Counter(f"{algorithm_name} c/ entrada" + f"ord {input} nums"):
            algorithm(sorted_numbers)

        with Counter(
            f"{algorithm_name} com entrada"
            + f"inversamente ordenada de {input} números"
        ):
            algorithm(reversed_sorted_numbers)

        with Counter(f"{algorithm_name} c/ entrada" + f"random {input} nums"):
            algorithm(random_numbers)

        print("*" * 50)
