# Peça ao usuário que insira 5 números em uma lista e depois exiba essa lista na ordem inversa.

lista = []
for x in range(5):
    num = int(input(f"Digite o {x + 1}° número: "))
    lista.append(num)
lista.reverse()
print(f"lista invertida: {lista}")