"""
precisamos saber o tempo máximo que um software permaneceu sem instabilidades.
Para isto, a cada hora é feito uma requisição ao sistema para verificamos se
está tudo bem. Supondo um array que contenha os estados coletados por nosso
software, calcule quanto tempo máximo que o servidor permaneceu sem
instabilidades.

Faça a análise de complexidade da sua solução.
"""

# 1 - OK
# 0 - Instabilidades


def max_time_without_instabilities(collected_values):
    max_time = 0
    current_time = 0

    for value in collected_values:
        if value == 1:
            current_time += 1
        else:
            current_time = 0

        if current_time >= max_time:
            max_time = current_time

    return max_time


collected_values1 = [0, 1, 1, 1, 0, 0, 1, 1]
print(max_time_without_instabilities(collected_values1))

collected_values2 = [1, 1, 1, 1, 0, 0, 1, 1]
print(max_time_without_instabilities(collected_values2))
