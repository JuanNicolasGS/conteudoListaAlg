# Crie um programa que peça ao usuário para inserir 5 números em uma lista.
# Depois, solicite ao usuário um número a ser substituído e outro número para substituí-lo.
# Atualize a lista e exiba o resultado.

lista = []

for x in range(5):
    num = int(input(f"Digite o {x + 1}° número: "))
    lista.append(num)
posicao = int(input(f"{lista}\nEscolha uma posição para substituir: "))
numNovo = int(input("Digite um número para substituir: "))
lista.pop(posicao - 1)
lista.insert(posicao - 1, numNovo)
print(lista)