# criando lista com 6 valores numèricos
numeros = [1, 2, 3, 4, 5, 6]
# imprindo lista para o usuário escolher qual irá remover
print(numeros)
# criando variavel escolha como input para o usuário escolher qual irá remover
escolha = int(input("Escolha um número da lista para remover: "))
if escolha in numeros:
    # fazendo remoção do número escolhido pelo usuário
    numeros.remove(escolha)
    print("Número removido com sucesso")
    # imprimindo lista atualizada
    print(numeros)
else:
    print("Número não encontrado na lista")


















































































    