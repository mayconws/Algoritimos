# 1. Faça algoritmos em Python, utilizando o while, que:
# a) Apresente na tela os números de 1 a 100.
# b) Faça a soma dos números de 1 a 100 e apresente somente o resultado.
# c) Apresente na tela somente os números pares entre 1 e 100.
# d) Apresente na tela somente a soma dos números pares entre 1 e 100.
# e) Apresente na tela os números de X a Y (peça para o usuário informar os valores de X e de Y).
# f) Faça a soma dos números de X a Y e apresente somente o resultado (peça para o usuário informar os valores de X e de Y).
# g) Apresente na tela somente os números ímpares entre X e Y (peça para o usuário informar os valores de X e de Y).

# # a)
# n = 1
# while n < 100:
#     print(n)
#     n = n + 1


# b)
# n = 1
# soma = 0
# while n <= 100:
#     soma = soma + n
#     n = n + 1
# print("A soma é", soma)

# c)
# i = 1
# while i < 100:
#     if i % 2 == 0:
#         print(i)
#     i = i + 1

# d)
# i = 1
# soma = 0
# while i <= 100:
#     if i % 2 == 0:
#         soma = soma + i
#     i = i + 1
# print("A soma é: ", soma)

# e)
# x = int(input("Informe um valor x: "))
# y = int(input("Informe um valor y: "))
# while x <= y:
#     print(x)
#     x = x + 1

# x = 1
# y = 0
# while x >= y:
#     x = int(input("Informe um valor x: "))
#     y = int(input("Informe um valor y: "))
#
# while x <= y:
#     print(x)
#     x = x + 1

# f)
# x = int(input("Informe um valor x: "))
# y = int(input("Informe um valor y: "))
# soma = 0
# while x <= y:
#     soma = soma + x
#     x = x + 1
# print("A soma é", soma)

# g)
# x = int(input("Informe um valor x: "))
# y = int(input("Informe um valor y: "))
#
# while x <= y:
#     if x % 2 == 1:
#         print(x)
#     x = x + 1

# 2.Faça um programa para calcular a tabuada:
# a) do 1 ao 10 para um número informado pelo usuário.
# n = int(input("Informe o valor para calcular a tabuada: "))
# x = 1
# while x <= 10:
#      print(n, "x", x, "=", n*x)
#      x = x + 1

# b) do X ao Y para um número informado pelo usuário (o usuário também deve informar os valores de X e Y).
# x = int(input("Digite um número para a tabuada: "))
# y = int(input("Digite um número final para tabuada: "))
# soma = 1
# while x <= y:
#     print(x, "x", y, "=", x*y)
#     x = x + 1
#     soma = soma + x

# 3.Na matemática, o fatorial de um número natural n, representado por n!, é o produto de todos
# os inteiros positivos menores ou iguais a n. Por exemplo: o fatorial de 5 é representado por 5!
# que é igual a 5 x 4 x 3 x 2 x 1. Faça um programa que peça um número para o usuário e apresente na tela seu fatorial.
# numero = int(input("Digite um numero para calcular o seu fatorial: "))
# numero_calc = numero
# fatorial = 1
# while numero_calc > 0:
#     fatorial = fatorial*numero_calc
#     numero_calc = numero_calc - 1
# print("O Fatorial de {}!" " = {}".format(numero, fatorial))

# 4.Faça um programa que mostre o menu a seguir, receba a opção do usuário e os dados necessários para executar cada operação.
 # O programa será executado repetidamente até que o usuário passe o número informado para sair do programa (opção).
# ====== Menu Principal ======
# 1. Par ou ímpar?
# 2. Potência XY
# 3. Raiz quadrada
# 4. Sair
print('''===== Menu =====
1. Par ou Impar?
2. Potência X e Y
3. Raiz quadrada
4. Sair
=================''')
numero = int(input("Digite uma opção: "))
opcao = int(input("Informe o valor para ser calculado: "))
while opcao != 4:


# 5.Faça um programa que mostre o menu a seguir, receba a opção do usuário e os dados necessários para executar cada operação. O programa será executado repetidamente até que o usuário passe o número informado para sair do programa (opção).
# ====== Menu Principal ======
# 1. Fazer a tabuada do 1 ao 10 para um número X
# 2. Apresentar os múltiplos de X entre 1 e 100
# 3. Apresentar a soma dos números de 1 a 100
# 4. Sair do programa
