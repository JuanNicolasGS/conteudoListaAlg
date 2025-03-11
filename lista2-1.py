# lista                         |
# for 10 números                |
#     armazenar na lista        |   PENSAMENTO INICIAL PARA FACILITAR CODE
# inverter lista                |
# imprimir lista                |

# criando lista
lista = []     
# laço for de 10 repetições com macete para formatação de input
for i in range(1, 10 +1):
    # criando variavel num para adicionar na lista usando "%d" para formatação de input
    num = int(input(f"Digite o {"%d" % i}º valor: " ))
    # adicionando numero na lista
    lista.append(num)
# invertendo lista
lista.reverse()
# imprimindo a lista
print(f"Invertemos a lista para você: {lista}")