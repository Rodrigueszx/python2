movieName = "top gun"

#string[start:end:step] ou [inicio:fim] - indice inicia em 0 | indice final -1

#1 - buscar toda string apartir da primeira posição
print(movieName[0:])

#2 - buscar toda string até a ultima posição, sempre levando em consideração que o indice final é -1

print(movieName[:7])

#3-buscar toda string da 3º posição até a ultima posição
print(movieName[2:])

"""#string[start:end:step] ou [inicio:fim:passo] - indice inicia em 0 | indice final -1, passo determina o incremento, por padrão é 1"""

#4 - buscar toda string incrementando de 2 em 2
print(movieName[::2])

#5-buscar toda string nos índices ímpares
print(movieName[1::2])

#6-Inverter a string de trás para frente
print(movieName[::-1])