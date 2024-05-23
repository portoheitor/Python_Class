# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteráveis.
# print(list(range(10)))
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# # print(novos_produtos)
# print(novos_produtos)
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]

p(novos_produtos)

# lado esquerdo do for (antes) é usado para o mapeamento ... 
# lado direito do for (depois) é para o filtro que deseja aplicar 
#  duvidas consulta  https://youtu.be/1YbTDczvqco