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

# 10.Construa um programa que mostre menu exatamente como o exemplo abaixo e implemente as funções necessárias:
# == Menu de Opções ==
# 1. Somar 2 números
# 2. Potência de um número
# 3. Raiz de grau N
# == Opção escolhida:
#
# print('''== Menu de Opções ==
# 1. Somar 2 números
# 2. Potência de um números
# 3. raiz de grau N''')
# opcao = int(input("== Opção Escolhida: "))
# if opcao == 1:
#     n1 = int(input("Digite o primeiro número: "))
#     n2 = int(input("Digite o segundo número: "))
#     soma = n1 + n2
#     print("A soma dos 2 numeros é: ", soma)
# if opcao == 2:
#     n1 = int(input("Digite um número: "))
#     potencia = n1**2
#     print("A potência é: ", potencia)
# if opcao == 3:
#     a = int(input("Digite um valor para A: "))
#     b = int(input("Digite um valor para B: "))
#     c = int(input("Digite um valor para C: "))
#     raiz = b**2-(4*a*c)/2
#     print("A raiz de grau N é: ", raiz)

# 11.Uma loja está com uma promoção de 10% desconto em todos os seus produtos. Faça um programa que receba um valor, calcule e imprima o valor do desconto (em reais) e o valor final do produto após aplicar o desconto.
#
# produto = float(input("Digite o valor do produto: "))
# desconto = (produto*10)/100
# print("O valor do desconto é: R$", desconto)
#
# totaldesconto = produto - desconto
# print("O valor final do do produto com desconto é: R$", totaldesconto)

# 12.Faça um programa que calcule o valor de imposto a ser pago a partir de um salário bruto. Se o salário for maior que R$3.000,00 deverá ser cobrado 15% de imposto e se for menor, 7,5%. Por fim, apresente o salário bruto (total), o valor de imposto e o salário líquido (o bruto menos o imposto).
#
# salario = float(input("Digite o seu salário bruto: R$ "))
# if salario < 3000:
#     imp7 = (salario*7.5)/100
#     total = salario-imp7
#     print("O seu salário bruto é de: {}".format(salario))
#     print("O valor descontado é de: {:.2f}".format(imp7))
#     print("O seu salário com desconto é de: R$ {:.2f}".format(total))
#
# elif salario > 3000:
#     imp15 = (salario*15)/100
#     total = salario-imp15
#     print("O seu salário bruto é de: {}".format(salario))
#     print("O valor descontado é de: {:.2f}".format(imp15))
#     print("O seu salário com desconto é de: R$ {:.2f}".format(total))

# 13.Construa um programa para receber 4 números e no final apresentar o maior e o menor deles.
#
# a = int(input("Digite um o primeiro número: "))
# b = int(input("Digite um o segundo número: "))
# c = int(input("Digite um o terceiro número: "))
# d = int(input("Digite um o quarto número: "))
# if a > b and a > c and a > d:
#     maior = a
# if b > a and b > c and b > d:
#     maior = b
# if c > a and c > b and c > d:
#     maior = c
# if d > a and d > b and d > c:
#     maior = d
#
# if a < b and a < c and a < d:
#     menor = a
# if b < a and b < c and b < d:
#     menor = b
# if c < a and c < b and c < d:
#     menor = c
# if d < a and d < b and d < c:
#     menor = d
# print("\033[32m""O Maior e o Menor são:""\033[0;0m")
# print("\033[32m", maior, "\033[1;0m")
# print("\033[32m", menor, "\033[1;0m")

# 14.Faça um Programa que receba o valor de x, calcule e imprima o valor de f(x) que será:
# f(x)= 12−x     se x<2
# f(x)= 1x−2     se x≥2
#
# x = int(input("Digite um valor para X: "))
# if x < 2:
#     fx1 = 1/(2-x)
#     print("O valor de f(x) é: ", fx1)
#
# elif x >= 2:
#     fx2 = 1/(x-2)
#     print("O valor de f(x) é: ", fx2)

# 15.Construa um programa para determinar se o indivíduo está com um peso favorável. Essa situação é determinada através do IMC (Índice de Massa Corporal), que é definida como sendo a relação entre o peso e o quadrado da altura do indivíduo. Ou seja: IMC = peso/altura² e a situação do peso é determinada pela tabela abaixo:
#
# peso = float(input("Digite seu peso: "))
# altura = float(input("Digite sua altura: "))
# imc = peso/(altura*altura)
# if imc < 18.5:
#     print("Seu IMC é de: {:.1f}".format(imc))
#     print(" === Peso Baixo ===")
#
# elif 18.5 <= imc < 24.9:
#     print("Seu IMC é de: {:.1f}".format(imc))
#     print("=== Peso Normal ===")
#
# elif 25 <= imc < 29.9:
#     print("Seu IMC é de: {:.1f}".format(imc))
#     print("=== Pré-Obesidade ===")
#
# elif 30 <= imc < 34.9:
#     print("Seu IMC é de: {:.1f}".format(imc))
#     print("=== Obesidade Grau I ===")
#
# elif 35 <= imc < 39.9:
#     print("Seu IMC é de: {:.1f}".format(imc))
#     print("=== Obesidade Grau II ===")
#
# elif imc >= 40:
#     print("Seu IMC é de: {:.1f}".format (imc))
#     print("=== Obesidade Grau III ===")

# 16.As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e o contrataram para desenvolver o programa que vai calcular os reajustes. Faça um programa que recebe o salário de um colaborador e calcule o reajuste segundo o seguinte critério baseado no salário atual:
# até R$ 710,00 (incluindo): aumento de 20%
# entre R$ 710,00 e R$ 1.000,00: aumento de 15%
# entre R$ 1.000,00 e R$ 2.500,00: aumento de 10%
# de R$ 2.500,00 em diante: aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
#
# print()
# print('''=== Reajuste Salárial ===''')
# print()
# salario = float(input("Digite o salário do colaborador: RS "))
# print()
# if salario <= 710:
#     aumento20 = (salario*20)/100
#     total = salario+aumento20
#     print("O salário antes do reajuste é de: {:.2f}".format(salario))
#     print()
#     print("O percentual de aumento aplicado é de: 20%")
#     print()
#     print("O valor do aumento é de: {:.2f}".format(aumento20))
#     print()
#     print("O novo salário após o aumento é de: {:.2f}".format (total))
#
# if 710 <= salario < 1000:
#     aumento15 = (salario*15)/100
#     total = salario+aumento15
#     print("O salário antes do reajuste é de: {:.2f}".format(salario))
#     print()
#     print("O percentual de aumento aplicado é de: 15%")
#     print()
#     print("O valor do aumento aplicado é de: {:.2f}".format(aumento15))
#     print()
#     print("O novo salário após o aumento é de: {:.2f}".format(total))
#
# if 1000 <= salario < 2500:
#     aumento10 = (salario*10)/100
#     total = salario+aumento10
#     print("O salário antes do reajuste é de: {:.2f}".format(salario))
#     print()
#     print("O percentual de aumento aplicado é de: 10%")
#     print()
#     print("O valor do aumento aplicado é de: {:.2f}".format(aumento10))
#     print()
#     print("O novo salário após o aumento é de: {:.2f}".format(total))
#
# if salario >= 2500:
#     aumento5 = (salario*5)/100
#     total = salario+aumento5
#     print("O salário antes do reajuste é de: {:.2f}".format(salario))
#     print()
#     print("O percentual de aumento aplicado é de: 5%")
#     print()
#     print("O valor do aumento aplicado é de: {:.2f}".format(aumento5))
#     print()
#     print("O novo salário após o aumento é de: {:.2f}".format(total))

# 17.Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# Até 5 Kg        Acima de 5 Kg
# Morango       R$ 8,90 por Kg     R$ 7,90 por Kg
# Maçã         R$ 3,90 por Kg          R$ 3,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$25,00, receberá ainda um desconto de 7% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs adquiridas e calcule o valor a ser pago pelo cliente.
#
# morango = int(input("Digite a quantidade de morango (Kg): "))
# maca = int(input("Digite a quantidade de maça (Kg): "))
# if morango <= 5 or maca <= 5:
#     morango_5 = morango*8.90
#     maca_5 = maca*3.90
#     total = morango_5+maca_5
#
# if morango > 5 or maca > 5:
#     morango_maior = morango*7.90
#     maca_maior = maca*3.50
#     total = morango_maior+maca_maior
#
# if total > 25:
#         desconto = (total*7)/100
#         vfinal = total-desconto
#         print("O valor a ser pago é: {:.2f}".format(total))
#         print("O valor do desconto é de: {:.2f}".format(desconto))
#         print("O valor do desconto é de: {:.2f}".format(vfinal))

# 18.Faça um Programa para calcular a quantidade de notas de um troco. O programa deverá
# perguntar ao usuário o valor do troco (inteiro) e depois informar quantas notas (considere
# R$1 como nota, pois temos moeda) de cada valor serão fornecidas. As notas disponíveis
# serão as de 1, 2, 5, 10, 50 e 100 reais.
# Exemplo 1​: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
# uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2​: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma
# nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

print("==="*10)
dinheiro = int(input("Digite o valor para saque: R$ " ))
total = dinheiro
cedula = 100
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print("Total de Notas: ", total_cedula)
            print("Cedulas de R$: ", cedula)
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        elif cedula == 1:
            cedula = 1
            total_cedula = 0
        if total == 0:
            break

print("==="*10)
print("Obrigado! Volte sempre!")
