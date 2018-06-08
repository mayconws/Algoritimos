# 1. Crie um vetor e armazene os números de 1 a 100. Cada número deve ocupar uma posição do vetor (lista).
# a) Mostre na tela todos os números do vetor em ordem crescente (1 a 100).
# lista = [""]*100
# p = 0
# while p < len(lista):
#     lista[p] = p + 1
#     p = p + 1
#
# p = 0
# while p < len(lista):
#     print("Na posição", p, "Tem o valor", lista[p])
#     p = p + 1

# b) Mostre na tela todos os números do vetor em ordem decrescente (100 a 1).
# p = len(lista) - 1
#
# while p >= 0:
#     print("Na posição", p, "Tem o valor", lista[p])
#     p = p - 1

# c) Mostre na tela o dobro de todos os números.
# p = 0
# while p < len(lista):
#     print("Na posição", p, "Tem o valor", lista[p]*2)
#     p = p + 1

# d) Apresente na tela a soma de todos os números.
# soma = 0
# p = 0
#
# while p < len(lista):
#     soma = soma + p
#     p = p + 1
# print("A soma é : ", soma)

# e) Apresente na tela a média geral dos valores contidos na lista.
# soma = 0
# p = 0
#
# while p < len(lista):
#     soma = soma + p
#     p = p + 1
# print("A média é: ", soma/len(lista))

# f) Mostre na tela a quantidade de números pares.
# par = 0
# impar = 0
# p = 0
#
# while p < len(lista):
#     if p % 2 == 0:
#         par = par + 1
#     else:
#         impar = impar + 1
#     p = p + 1
#
# print("A quatidade de Par é: ", par)
# print("A quatidade de Impar é: ", impar)

# 2. Faça um programa para armazenar 6 números inteiros para uma loteria,
# permitindo que o usuário informe os números sorteados. Depois de preencher, informe uma mensagem e os números sorteados.
# lista = [""]*6
# numero = 0
#
# while numero < len(lista):
#     lista[numero] = int(input("Digite os números para sorteio: "))
#     numero = numero + 1
# print("Os números sorteados são: {}".format(lista))

# 3.Um professor precisa armazenar em uma lista os nomes dos alunos presentes em um minicurso.
# Faça um programa para armazenar 5 nomes e permitir que o professor digite o nome da cada um. Em seguida,
# apresente na tela todos os nomes informados.

# 4.Faça um programa que peça para o usuário informar o tamanho de um vetor. Em seguida,
# crie este vetor e preencha ele com números digitados pelo usuário. Por fim, apresente na tela os números digitados.
# t = int(input("Digite o tamanho da lista: "))
# lista = [""]*t
# p = 0
#
# while p < len(lista):
#     lista[p] = int(input("Digite os números:"))
#     p = p + 1
# print("Os núemros digitados são: {}".format(lista))

# 5.Para os exercícios abaixo, utilize o vetor criado no exercício anterior.
# a) Apresente os números do vetor em ordem inversa.
