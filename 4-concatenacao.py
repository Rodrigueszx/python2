#concatenação de valores

name = input("Digite o nome do filme:\n")
yearLaunch = int(input("Digite o ano de lançamento do filme:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))
#planIncluded = bool(input("O filme está incluso no plano? True or False:\n"))
text = "Nome do filme: {0}" "\nAno de lançamento do filme: {1}" "\nNota do filme: {2}".format(name, yearLaunch, noteMovie)

#Alternativa 1
# print("Dados do filme")
# print("====================================")
# print("Nome do filme: ",name)
# print("Ano de lançamento: ",yearLaunch)
# print("Nota do filme: ",noteMovie)

#Alternativa 2 
# print("Dados do filme")
# print("====================================")
# print("Nome do filme:", name, "\nAno de lançamento do filme:",yearLaunch, "\nNota do filme:", noteMovie)

#Alternativa 3
# print("Dados do filme")
# print("====================================")
# print(f'Nome do filme: {name} \nAno de lançamento do filme: {yearLaunch} \nNota do filme: {noteMovie}\n')

#Alternativa 4
print("Dados do filme")
print("====================================")
print(text)