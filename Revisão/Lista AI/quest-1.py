# Escreva um programa que peça ao usuário para inserir 5 números e armazene-os em uma lista. 
# Depois, calcule e exiba a soma de todos os números da lista.

# criando lista vazia
lista = []
# criando variavel soma para auxiliar a soma dos itens da lista
soma = 0
# laço for de 5 repetições
for x in range(5):
    # criando varivel num para armazenar na lista
    num = int(input(f"Digite o {x + 1}° número: "))
    # armazenando itens na lista
    lista.append(num)
# laço for que percorre a lista
for y in lista:
    # calculando soma de itens da lista
    soma += y
# exibindo soma de itens da lista
print(f"A soma de todos os números digitados e armazenados na lista é igual a: {soma}")