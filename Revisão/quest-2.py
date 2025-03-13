# Criando lista com 5 nomes
lista = ["JUAN", "PAULO", "ARTUR", "ANA", "PERVERSO"]
# Recebendo nome como input, para ser verificado
# | Usando as funções strip() e upper() para formatar e facilitar o teste
nome = str(input("Digite um nome para ser verificado: ")).strip().upper()
# verificando se o nome digitado já existe na variavel lista
# | O operador In verifica se determinado item já existe na estrutura seguinte (lista e etc...)
if nome in lista:
    # imprimindo npme está na lista caso esteja
    print(f"Nome '{nome}' está na lista.")
else:
    # imprimindo npme não está na lista caso não esteja
    print(f"Nome '{nome}' não está na lista.")
    
