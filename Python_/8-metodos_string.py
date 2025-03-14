movieName = "top gun"
movieDescription = '''Top Gun' is a 1986 American action drama film directed by Tony Scott, and produced by Don Simpson and Jerry Bruckheimer, in association with Paramount Pictures. The screenplay was written by Jim Cash and Jack Epps Jr., and was inspired by an article titled "Top Guns" published in California magazine three years earlier.'''

print(movieName.upper()) #retorna a string em maiúscula
print(movieName.lower()) #retorna a string em minúscula
print(movieName.capitalize()) #retorna a string com a primeira letra em maiúscula
print(movieName.title()) #retorna a string com a primeira letra de cada palavra em maiúscula
print(movieName.center(10, '-')) #retorna string centralizada com caractere de preenchimento
print(movieName.find("u")) #retorna o índice da primeira ocorrência de uma substring
print(movieName.find("o")) #retorna a contagem de ocorrências de uma substring
print(movieName.replace("top","matrix")) #substitui uma substring por outra
print(movieDescription.split(',')) #divide a string em uma lista de substrings