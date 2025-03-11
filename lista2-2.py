# lista de numeros                          |
# for 5 numeros                             |
#     adicionar numero inteiro na lista     | PENSAMENTO INICIAL PARA FACILITAR CODE
# imprimir lista de numeros                 |

# criando lista de numeros
numbers = []
# laço for de 5 repetições
for i in range(5):
    # criando variavel inteira num com difetente macete de formatação
    num = int(input(f'Digite o {i+1}º número: '))
    # adicionando número a lista de numeros
    numbers.append(num)
# imprimindo a lista
print(f"Adicionamos os números digitados à lista: {numbers}")