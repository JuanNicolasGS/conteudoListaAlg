# Solicite ao usuário 10 números e armazene-os em uma lista. Em seguida, 
# crie uma nova lista contendo apenas os números ímpares e exiba-a.

lista = []
impares = []
for x in range(10):
    num = int(input(f"Digite o {x+1}º número: "))
    lista.append(num)
    if num % 2!= 0:
        impares.append(num)
print(f"Números ímpares: {impares}")
