# Crie um programa que solicite 10 números ao usuário, armazene-os em uma lista e depois exiba quantos desses números são pares.

# criando listas vazias
lista = []
pares = []
# laço for de 10 repetições
for x in range(10):
    # criando variavel num para armazenar em lista
    num = int(input(f"Digite o {x+1}º número: "))
    # armazenando num em lista
    lista.append(num)
    # cirando condição de número para através do resto da divisão por 2
    if num % 2 == 0:
        # adcinando num a lista pares caso num seja par
        pares.append(num)
# exibindo lista com len para informar quantidade de itens pares
print(f"Da lista: {lista} {len(pares)} são pares")
        
        