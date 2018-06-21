# 1. Crie um vetor e armazene os números de 1 a 100. Cada número deve ocupar uma posição do vetor (lista).
# # a) Mostre na tela todos os números do vetor em ordem crescente (1 a 100).
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
lista = [""]*6
numero = 0

while numero < len(lista):
    lista[numero] = int(input("Digite os números para sorteio: "))
    numero = numero + 1
print("Os números sorteados são: {}".format(lista))

# 3.Um professor precisa armazenar em uma lista os nomes dos alunos presentes em um minicurso.
# Faça um programa para armazenar 5 nomes e permitir que o professor digite o nome da cada um. Em seguida,
# apresente na tela todos os nomes informados.
# print('''====================
# Curso de Python
# Instituto Federal do Paraná
# ====================''')
# lista = [""]*5
# nomes = 0
#
# while nomes < len(lista):
#      lista[nomes] = input("Digite os nomes para cadastro: ")
#      nomes = nomes + 1
# print("Os números sorteados são: {}".format(lista))

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
# p = len(lista) - 1
# while p < len(lista):
#     print(lista[p])
#     p = p - 1

# b) Apresente a soma de todos os elementos.
# soma = 0
# p = 0
#
# while p <= len(lista):
#     soma = soma + p
#     p = p + 1
# print("A soma dos númetos: {}".format(soma))

# c) Calcule a média aritmética dos valores.
# soma = 0
# p = 0
#
# while p < len(lista):
#     soma = soma + p
#     p = p + 1
# print("A média Aritmetica: {}".format(soma/len(lista)))

# d) Determinar um segmento informado pelo usuário (posição inicial e final) para apresentar os números na tela.
# Por exemplo: na sequência 5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1 o usuário teria que informar 4 e 8 (posição inicial e final,
# respectivamente) para mostrar na tela somente os valores destacados.
# p = int(input("Digite a posição inicial: "))
# f = int(input("Digite a posição final: "))
#
# while p < f:
#     print("O número Inicial é: {} e o Número Final é: {}".format(p, f))
#     p = p + 1

# e) Determinar um segmento informado pelo usuário (posição inicial e final) para apresentar a soma daquele intervalo.
# Exemplo: Na sequência 5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1 , a soma do segmento destacado é 33.
# i = int(input("Digite a posição inicial: "))
# f = int(input("Digite a posição final: "))
# p = 0
# soma = 0
#
# while i < f:
#     soma = soma + p
#     p = p + 1
# print("A soma dos números selecionados é: {}".format(soma))

# f) Encontre qual é o maior e o menor número desta lista.

# g) Encontre qual é o maior e o menor número desta lista. Além disso, informe quais são os índices (posições) deles.

# h) Informe quantos números pares e ímpares foram digitados (apenas a quantidade de cada).

# 6. Crie um vetor para armazenar alguns números que serão utilizados no cálculo da tabuada.
# a) Apresente todos os números informados e seu respectivo dobro.
#
# b) Para cada número presente no vetor, faça a tabuada do 1 ao 10 (utilizando laço de repetição).
