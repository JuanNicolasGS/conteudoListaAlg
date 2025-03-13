# Peça ao usuário para inserir 10 números e armazene-os em uma lista. Depois, determine e exiba o maior e o menor número da lista.

# criando lista
lista = []
# laço for de 10 repetições
for x in range(10):
    # criando variavel num para armazenar na lista
    num = float(input(f"Digite o {x+1}º número: "))
    # armazenando na lista
    lista.append(num)
# criando variaveis maior e menor para receber os valores retornados das funções min() e max()
# | A função min() retorna o menor número dentro da lista passada como parametro para a função
# | A função max() retorna o menor número dentro da lista passada como parametro para a função
maior = max(lista)
menor = min(lista)
# exibindo maior e menor número da lista
print(f"O maior valor de sua lista: {maior} \nO menor valor de sua lista: {menor}" )