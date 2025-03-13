# Crie um programa que peça ao usuário para inserir 10 números e armazene-os em uma lista.
# Depois, remova os números duplicados e exiba a lista sem repetições.

lista = []
listaTotal = []
for x in range(10):
    numero = int(input(f"Digite o {x+1}º número: "))
    listaTotal.append(numero)
    if numero not in lista:
        lista.append(numero)

print(f"Sua lista sem números repetidos é: {lista}\nSua lista com numeros repetidos é: {listaTotal}")