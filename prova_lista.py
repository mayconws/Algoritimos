# Questão 1 : Faça um programa que, utilizando um laço de repetição, receba a idade de 10 pessoas,
# calcule e mostre a quantidade de pessoas em cada faixa etária de acordo com a legenda:
#
# Menor de idade - 0 a 17 anos
# Jovem - 18 a 65 anos
# Meia idade - 66 a 79 anos
# Idoso - 80 a 99 anos
# Idoso de vida longa - 100 ou mais

# menor = jovem = meia_idade = idoso = vida_longa = 0
#
# # repete 10 vezes:
# for n in range(10):
#     idade = int(input("Digite a sua idade:"))
#
# # apos digitar cada idade, classifica a pessoa e incrementa a variavel certa:
#     if idade <= 17:
#         menor = menor + 1
#     elif 17 < idade <= 65:
#         jovem = jovem + 1
#     elif 65 < idade <= 79:
#         meia_idade = meia_idade + 1
#     elif 79 < idade <= 99:
#         idoso = idoso + 1
#     else:
#         vida_longa = vida_longa + 1
#
# # Após processar as 10 pessoas, imprime o resultado
#
# print("Menores de idade: ", menor)
# print("Jovens: ", jovem)
# print("Pessoas de meia idade: ", meia_idade)
# print("Idosos: ", idoso)
# print("Idosos de vida longa: ", vida_longa)

# 1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

# num = [""] * 10
#
# i = 0
# soma = 0
#
# while i < len(num):
#     num[i] = int(input("Digite os números: "))
#     soma = soma + num[i]
#     i = i + 1
# print(f"Os núemros digitados são: {num}")
# print(f"A soma dos núemros informados são: {soma}")

# 2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

# num = [""] * 3
#
# i = 0
#
# while i < len(num):
#     num[i] = int(input("Digite os numeros: "))
#     i = i + 1
# num.reverse()
# print(num)
#
# i = len(num) - 1
#
# while i >= 0:
#     print(f"Os números na ordem inversa são: {num[i]}")
#     i = i - 1

# 3 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela

# notas = [""] * 4
#
# i = 0
# soma = 0
#
# while i < len(notas):
#     notas[i] = int(input("Digite a sua nota: "))
#     soma = soma + notas[i]
#     i = i + 1
# print(f"As suas notas foram: \nNotas 1: {notas[0]}\n \nNota 2: {notas[1]}\n \nNota 3: {notas[2]}\n \nNota 4: {notas[3]}\n")
# print(f"A sua média final é: {soma/4}")

# 4 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

# letras = []
# vogais = ['A', 'E', 'I', 'O', 'U']
#
# for i in range(0, 10):
#     letras.append(input('Informe um caracter: ').upper())
#
# totConsoantes = 0
# consoantes = []
# for i in range(0, 10):
#     if letras[i] not in vogais:
#         consoantes.append(letras[i])
#         totConsoantes += 1
# print(consoantes)

 # Karen - O método deve receber um vetor de números inteiros por parâmetro e retornar somente a quantidade de números ímpares do vetor.
 # O nome do método deve ser quantosImpares().
# def quantosImpares():
#
#     lista = [""] * 5
#
#     impar = 0
#     i = 0
#
#     while i < len(lista):
#         lista[i] = int(input("Digite um número: "))
#         i = i + 1
#
#         if i % 2 != 0:
#             impar = impar + 1
#     print(f"A quantidade de Numeros Ímpares é: {impar}")
#
# quantosImpares()

# 5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

# num = []
# impar = []
# par = []
#
# for i in range(0,5):
#     numero = int(input("Digite um número: "))
#     num.append(numero)
#
#     if numero % 2 == 0:
#         par.append(numero)
#
#     else:
#         impar.append(numero)
#
# print(f"Os números digitados são: {num}")
# print(f"Os números pares são: {par}")
# print(f"Os números impares são: {impar}")

def num(numeros):

    num = [1,8,9,0,5]

    i = 0
    soma = 0

    while i < len(num):
        soma = soma + num[i]
        i = i + 1

    print(fnum)
    print(soma)
