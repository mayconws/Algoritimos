# 1.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
#
# valor = int(input("Digite um valor: "))
# if valor > 0:
#     print("O valor é positivo!")
# else:
#     print("O valor é negativo!")

# 2.Faça um Programa que peça dois números e imprima o maior deles.
#
# n1 = int(input("Digite um número:"))
# n2 = int(input("Digite o segundo número:"))
# if n1 >= n2:
#     print("O primeiro núemro é o maior: ")
# else:
#     print("O segundo núemro é o maior: ")

# 3.Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
#
# valor1 = int(input("Digite um valor para A: "))
# valor2 = int(input("Digite um valor para B: "))
# valor3 = int(input("Digite um valor para C: "))
# soma = valor1 + valor2
# if soma <= valor3:
#     print("A soma de A+B é menor que C")
# else:
#     print("A soma de A+B é maior que C")

# 4.Faça um Programa que verifique o sexo de uma pessoa. O usuário deve informar ‘F’ ou ‘M’ e o programa deve escrever “Feminino” ou “Masculino”, conforme a letra digitada.
#
# sexo = input("Digite f ou m: ")
# if sexo == "m":
#     print("Sexo Masculino")
# elif sexo == "f":
#     print("Sexo Feminino")
# else:
#     print("Sexo indefinido")

# 5.Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo (resto da divisão).
#
# divisao = int(input("Digite um número inteiro: "))
# if (divisao % 2 == 0):
#     print("O número é par!")
# else:
#     print("O número é impar!")

# 6.Faça um algoritmo que peça um número e se ele for par some 5, se não, some 8.
#
# numero = int(input("Digite um número: "))
# if (numero % 2 == 0):
#     print (numero + 5)
# else:
#     print (numero + 8)

# 7.Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100). Se a média aritmética das notas for maior ou igual a 60, escreva “Aprovado”, se não, “Reprovado”.
#
# trabalho = int(input("Digite a nota do trabalho: "))
# prova = int(input("Digite a nota da prova: "))
# media = (trabalho+prova)/2
# if media >= 60:
#     print("Aprovado!")
# elif media <= 60:
#     print("Reprovado!")

# 8.Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela somente o maior deles.
#
# a = int(input("Digite um valor para A:"))
# b = int(input("Digite um valor para B:"))
# c = int(input("Digite um valor para C:"))
# if a > b and c:
#     print("O valor A é o maior")
# elif b > a and c:
#     print("O valor B é o maior")
# elif c > b and c:
#     print("O valor C é o maoior")

# 9.Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela os números em ordem crescente.
#
# a = int(input("Digite um valor para A: "))
# b = int(input("Digite um valor para B: "))
# c = int(input("Digite um valor para C: "))
# if a > b and a > c:
#     maior = a
# if b > a and b > c:
#     maior = b
# if c > a and c > b:
#     maior = c
#
# if a < b and a > c:
#     meio = a
# if b < a and b > c:
#     meio = b
# if c < a and c > b:
#     meio = c
#
# if a < b and a < c:
#     menor = a
# if b < a and b < c:
#     menor = b
# if c < a and c < b:
#     menor = c
# print("A ordem Crescente é ", menor, meio, maior)

# # 10.Construa um programa que mostre menu exatamente como o exemplo abaixo e implemente as funções necessárias:
#     == Menu de Opções ==
#     1. Somar 2 números
#     2. Potência de um número
#     3. Raiz de grau N
#     == Opção escolhida:

print('''== Menu de Opções ==
1. Somar 2 números
2. Potência de um números
3. raiz de grau N''')
opcao = int(input("== Opção Escolhida: "))
if opcao == 1:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    soma = n1 + n2
    print("A soma dos 2 numeros é: ", soma)
if opcao == 2:
    n1 = int(input("Digite um número: "))
    potencia = n1**2
    print("A potência é: ", potencia)
if opcao == 3:
    a = int(input("Digite um valor para A: "))
    b = int(input("Digite um valor para B: "))
    c = int(input("Digite um valor para C: "))
    raiz = b**2-(4*a*c)/2
    print("A raiz de grau N é: ", raiz)
else:
    print("Opção inválida...Tente Novamete!")
