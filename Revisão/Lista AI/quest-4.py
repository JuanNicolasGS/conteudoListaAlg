# Solicite ao usuário que informe quantos números quiser (encerre com um número negativo), 
# armazene-os em uma lista e calcule a média dos valores inseridos (desconsiderando o número negativo que encerra a entrada).

lista = []
soma = 0
while True:
    num = float(input("Informe um número (encerra com um número negativo): "))
    if num < 0:
        break
    else:
        lista.append(num)
        soma += num 
media = soma / len(lista) 
print(f"A media dos valores inseridos é: {media}")