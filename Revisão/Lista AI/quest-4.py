# Solicite ao usuário que informe quantos números quiser (encerre com um número negativo), 
# armazene-os em uma lista e calcule a média dos valores inseridos (desconsiderando o número negativo que encerra a entrada).

# cirando lista vazia
lista = []
# criando variavel auxiliar soma
soma = 0
# criando estrutura de reptição while True (loop infinito)
while True:
    # recebendo para armazenar na lisa se ele for maior igual a 0
    num = float(input("Informe um número (encerra com um número negativo): "))
    # criando estrutura de condição para parar o loop caso resposta de num seja menor que 0
    if num < 0:
        # quebrando estrutura de repetição
        break
    # adicionando o número ao final da lista se ele for maior/igual a 0
    else:
        lista.append(num)
        # fazendo soma de cada objeto na lista
        soma += num 
# calculando a média dos valores inseridos
media = soma / len(lista)
# exibindo a média dos valores inseridos na lista 
print(f"A media dos valores inseridos é: {media}")