# Peça ao usuário 10 números e armazene-os em uma lista.
# Depois, exiba a lista ordenada em ordem crescente e em ordem decrescente.

lista = []
for x in range(10):
    num = int(input(f"Digite o {x + 1}° número: "))
    lista.append(num)
lista.sort()
print(f"Lista ordem crescente: {lista} ")
lista.sort(reverse=True)
print(f"Lista ordem decrescente: {lista}")