# criando lista
lista = []
# laço de 5 repetições para armazenar números na lista
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista.append(numero)
# ordenando a lista em ordem crescente
lista.sort()
# imprimindo lista e maior e menor item da lista
# | A função min() retorna o menor número na lista 
# | A função max() retorna o maior número na lista
print(f"Aqui está sua lista: {lista} \nO maior número da lista é: {max(lista)} \nO menor número da lista é: {min(lista)}" )