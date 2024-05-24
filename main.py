# lista
nomes = ['Alex', 'Fabio', 'Morgana', 'Tiago', 'Emanuelle']

# usuario informa o indice que deseja alterar
indice = int(input('Informe o indice que deseja alterar: '))
indice -= 1

# usuario informa o novo nome
nomes[indice] = input("Informe o nove nome: ")

# exibe a lista
for nome in nomes:
    print(nome)

   

