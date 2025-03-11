# 3 listas                                      |
#     numeros                                   |
#     pares                                     |
#     impares                                   |
# for 20 numeros                                |
#     numero                                    |    PENSAMENTO INICIAL PARA FACILITAR CODE
#     adicionar numero na lista numeros         |
#     condição par                              |
#         numero adicionado na lista par        |
#     condição impar                            |
#         numero adicionado na lista impar      |
# imprimir as tres listas                       |

# criando as listas numeros, pares e impares
numeros = []
pares = []
impares = []
# laço for de 20 repetições
for i in range(20):
    # criando variavel inteira número com formatação de enumeração de input
    numero = int(input(f"Digite o {i + 1}° número: "))
    # adicionando o número a lista de números
    numeros.append(numero)
    # verificando se é par ou ímpar e adicionando a lista correspondente
    if numero % 2 == 0:
        pares.append(numero)
        print(f"{numero} é par e foi adicionado a lista de números pares.")
    else:
        impares.append(numero)
        print(f"{numero} é ímpar e foi adicionado a lista de números ímpares.")
    # imprimindo linhas para separar números inseridos
    print("---" * 10)
# imprimindo listas de números, pares e impares, todos com um len para mostrar a quantidade de itens dentro da respectiva lista
print(f"\nListas: \n{len(numeros)} Números: {numeros} \n{len(pares)} Pares: {pares} \n{len(impares)} Impares: {impares}")