# lista pessoas                     |
# lista pessoa                      |
# for 5 informações                 |
#     nome                          |
#     idade                         |
#     altura                        |  PENSAMENTO INICIAL PARA FACILITAR CODE
#     adicionar a lista pessoa      |
#     adicionar a lista pessoas     |
# inverter ordem de pessoas         |
# imprimir pessoas invertidas       |

# criando lista de pessoas e pessoa
pessoas = []
pessoa = []
# criando um contador para um metodo diferente de formatação para enumeração de input
c = 1
# laço for de 5 repetiçoes
for i in range(5):
    # criando variaveis nome, idade e altura com outro macete de formatação de input
    nome = str(input(f"Digite o primeiro nome da pessoa {c}: "))
    idade = int(input(f"Digite a idade da pessoa {c}: "))
    altura = float(input(f"Digite a altura da pessoa {c}: "))
    # adicionando dados inseridos a pessoa
    pessoa.append(nome)
    pessoa.append(idade)
    pessoa.append(altura)
    # adicionando pessoa a lista pessoas
    pessoas.append(pessoa)
    # limpando a lista pessoa para nova entrada
    pessoa = []
    # adicionando 1 ao contador
    c += 1
# invertendo a lista
pessoas.reverse()
# imprimindo a lista de pessoas
print(f"Adicionamos o cadastro de cada pessoa à lista de pessoas e á invertemos: {pessoas}")