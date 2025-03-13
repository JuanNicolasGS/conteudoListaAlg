# criando lista
lista = []
# laço for de 2 repetições para adicionar numeros a lista
for i in range(2):
    num = int(input(f"Digite o {i + 1}° número: "))
    lista.append(num)
# recebendo número para entrar na segunda posição da lista
numPosicao = int(input("Digite o 3° número: "))
# usando insert para armazenar numPosicao na segunda posição da lista 
# | usei (2 - 1) para determinar a posição tendo conhecimento que o for começa a contagem em 0 quando não é determinado inicio
# | logo 2 seria o teceiro item da lista, para resolver isso podemos usar (2 - 1) ou determinar a posição de inicio no laço for
lista.insert((2 - 1), numPosicao)
# removendo o ultimo item da lista, usando -1 que é um macete para acessar o ultimo elemento de uma lista
lista.pop(-1)
# imprimindo a lista
print(f"Aqui está a lista: {lista}")