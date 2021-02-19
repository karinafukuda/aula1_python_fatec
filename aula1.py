#Aula 1 - Variável

#int - converte string do input em int
base = int(input("Digite a base:  "))
altura = int(input("Digite a altura:  "))
area = base * altura
print(area)

#soma de 2 números reais
a = float(input("Digite um valor real para A:  "))
b = float(input("Digite um valor real para B:  "))
soma = a + b
print(soma)

#operadores matemáticos

a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
print ("Soma = ", a + b)
print ("Subtração = ", a - b)
print ("Multiplicação = ", a * b)
print ("Divisão Real = ", a / b)
print ("Divisão Inteira = ", a // b)
print ("Resto = ", a % b)
print ("Potência = ", a ** b)

#exemplo em uma expressão aritmética

a = 17
b = 3
c = 5

resultado = (3 * a + 2 *( b + c)) / ( a - b ** 2)
print ("O resultado da conta é:" , resultado)





