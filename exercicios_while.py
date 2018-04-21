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
n = int(input("Informe o valor para calcular a tabuada: "))
x = 1
while x <= 10:
     print(n, "x", x, "=", n*x)
     x = x + 1

# b) do X ao Y para um número informado pelo usuário (o usuário também deve informar os valores de X e Y).
