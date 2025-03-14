    # 1- Escreva um programa que lê dois nomes e retorne uma string formatada no formato "UltimoNome, PrimeiroNome".
    # 2- Iverta a ordem das palavras de uma string fornecida.
    # 3- Verifique se uma string é um palíndromo.
    # (Pode ser lida da mesma forma de trás para frente)
    
#EX01
# name = input("Digite o nome:")
# lastName = input("Digite o sobrenome:")
    
# print(f'{lastName}, {name}')

# #EX02
# text = "pyhton é muito interessante"
# palavras = text.split()
# textoInvertido = " ".join(palavras[::-1])

# print(textoInvertido)

#EX03
text1 = "arara"
text2 = "python"

#Removendo os espaços e deixa o nome em minúsculo
text1_format = text1.lower().replace(" ","")
text2_format = text2.lower().replace(" ","")

#verifica se a string é um palíndromo
paloindromo1 = text1_format == text1[::-1]
paloindromo2 = text2_format == text2[::-1]

print(paloindromo1)
print(paloindromo2)