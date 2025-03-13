# lista                         |
# enquanto                      |
#     nota                      |
#     nota na lista             |    PENSAMENTO INICIAL PARA FACILITAR CODE
#     opção condicionada        |
#         ? pass : break        |
# saida notas                   |
# saida lista ordenada          |

# criando lista
lista = []
# criando contador para enumeração de input
c = 1
# criando variavel float nota e adicionando a lista
nota = float(input(f"Digite a {c}º nota: "))
lista.append(nota)
# estrutura de repetição while | while True é um tipo de loop infinito
while True:
    # imprimindo frase para ajuda na compreensão do programa
    print("Digite S para continnuar e N para sair")
    # criando variavel string opção com tratamento de erro caso seja digitados espaços vaios e letras minúsculas
    opcao = str(input("Quer continuar? ")).strip().upper()
    # condição de opção | N para o laço | S continua o laço | se for algo diferente disso imprimo opçãp invalida e faço tentar denovo
    if opcao == "N":
        break
    elif opcao == "S":
        c += 1
        nota = float(input(f"Digite a {c}º nota: "))
        lista.append(nota)
    else:
        print("Opção inválida, tente novamente!")
# ordenando a lista
lista.sort()
# imprimindo a lista ordenada com número de notas digitadas
print(f"Foram digitados {len(lista)} notas \nE a mesma ordenada é: {lista}")

        