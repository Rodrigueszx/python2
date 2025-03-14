# operadores aritmeticos

num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

# operadores

sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
mod = num1 % num2
exp = num1 ** num2

print('=========================')
print(sum)
print(sub)
print(mult)
print(div)
print(div)
print(exp)

print(f'Potencia do numero {num1} por {num2} é {exp}')
print(f'Resto da divisão de {num1} por {num2} é: {mod}')

#comparação

bigger = num1 > num2
smaller = num1 < num2 
equal = num1 == num2
different = num1 != num2 
biggerEqual = num1 >= num2
smallerEqual = num1 <= num2

print(f'Os números {num1} e {num2} são iguais? {equal}')
print(f'O número {num1} é maior ou igual a {num2}? {biggerEqual}')


#atribuição

num1 += 1 #num1 + 1
num1 -= 1 #num1 - 1
num1 *= 1 #num1 * 1
num1 /= 1 #num1 / 1