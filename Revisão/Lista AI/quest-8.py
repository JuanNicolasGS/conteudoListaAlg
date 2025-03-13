# Peça ao usuário para inserir 10 nomes em uma lista. Depois, pergunte um nome e verifique se ele está na lista. 
# Informe ao usuário se o nome foi encontrado ou não.

lista = []
for x in range(10):
    nome = str(input(f"Digite o {x + 1}° nome: ")).strip().upper()
    lista.append(nome)
nomeVerificado = str(input(f"Digite o nome para ser verificado: ")).strip().upper()
if nomeVerificado in lista:
    print(f"O nome {nomeVerificado} está na lista")
else:
    print(f"O nome {nomeVerificado} não está na lista")