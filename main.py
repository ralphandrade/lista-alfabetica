# lista
nomes = ['Alex', 'Fabio', 'Morgana', 'Tiago', 'Emanuelle','Joao', 'José', 'Maria', 'Francisco', 'Guilherme', 'Gustavo', 'Beatriz','Sofia', 'Yasmin','Rogério']

# usuario informa o nome que deseja pesquisar
nome = input('Digite o nome a ser pesquisado: ').capitalize()

#retorna o indice do nome pesquisado
# indice = nomes.index(nome)

# verifique se o nome está na lista ou não
try:
    indice = nomes.index(nome)
    print(f'Nomwe encontrado:{nome} no indice{indice}.')
except:
    print(f'{nome} não encotrado na lista. ')

   

