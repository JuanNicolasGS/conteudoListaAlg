# Crie um programa que solicite 10 números ao usuário, armazene-os em uma lista e depois exiba quantos desses números são pares.

lista = []
pares = []
for x in range(10):
    num = int(input(f"Digite o {x+1}º número: "))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
print(f"Da lista: {lista} {len(pares)} são pares")
        
        