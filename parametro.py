# def tabuada():
#     print("Calculando a Tabuada")
#
#     t = int(input("Digite um número para a tabuada: "))
#
#     x = 1
#
#     while x <= 10:
#          print(t, "x", x, "=", t*x)
#          x = x + 1
#
# tabuada()

# def exemplo2(t):
#
#     x = 1
#
#     while x <= 10:
#          print(t, "x", x, "=", t*x)
#          x = x + 1
#
# exemplo2(10)

# def exemplo3(a):
#
#     triplo = a * 3
#
#     return triplo

# def exemplo4(num):
#
#     if num % 2 == 0:
#
#         return num ** 2
#     else:
#         n = num ** 3
#         return n
#
# k = exemplo4(850)
# print("O numero é: {}".format(k))

# def soma(x,y):
#     total = x+y
#     print("O total da soma de x + y é: ", total)
#
# soma(10,50)

# def multiplicacao(a,b):
#
#     mult = a * b
#
#     print("A Multiplicação dos números: ", mult)
#
# multiplicacao(2,2)

# def teste(a):
#
#     usuario = int(input("Digite um numero: "))
#
#     mult = usuario ** 2
#
#     print("A multiplicação é: ", mult)
#
# teste(9)

# 1 - Faça uma função sem parâmetro que pede um número inteiro para o usuário e imprime o sucessor desse número na tela.
#
# def numero():
#
#     usuario = int(input("Digite um número: "))
#
#     sucessor = usuario + 1
#
#     print("O número sucessor é: {}".format(sucessor))
#
# numero()

# 2 - Faça uma função que recebe dois números inteiros por parâmetro e imprime somente o maior desses números na tela.

# def maior():
#
#     a = int(input("Digite um valor:"))
#     b = int(input("Digite outro valor: "))
#
#     if a > b:
#         return a
#
#     if b > a:
#         return b
#
# print("O maior número é: {}".format(maior()))

# def maior(a,b):
#
#     if a > b:
#         return a
#
#     if b > a:
#         return b
#
# resultado = maior(100,54)
#
# print("O maior núemro é: {}".format(resultado))

# 3 - Implemente o método solicitado conforme a responsabilidade a seguir:
#
# O método deve solicitar ao usuário o ano de seu nascimento e retornar sua idade atual (considerar apenas o ano atual e não o dia).
# O nome do método deve ser calcularIdade().

# def calcularIdade():
#
#     ano = int(input("Digite o ano de nascimento: "))
#
#     idade = 2018 - ano
#     return idade
#
# print("A sua idade é: {}".format(calcularIdade()))

# 4 - Crie uma função que recebe o nome do arquivo por parâmetro, leia o conteúdo do arquivo,
# calcule a soma dos números registrados e imprima-a na tela do programa somente a soma final.

arquivo = open("arquivos/numeros.txt", "r")

conteudo = arquivo.readlines()

arquivo.close()

l = 0

while l < len(conteudo) :
    print(conteudo[l])
    l+=1

l = 0
soma = 1

while l < len(conteudo) :
    soma = soma + l
    print("A soma dos números é: ", soma)
    l+=1


# Karen
#
# Questão - 1

# def raiz():
#
#     usuario = float(input("Digite um número para calcular a raiz quadrada: "))
#
#     num_raiz = usuario ** (1/2)
#
#     print("A raiz quadrada é: {:.2f}".format(num_raiz))
#
# raiz()

# Questão - 2

# def multiplicacao(a,b):
#
#     num = a * b
#     return num
#
# k = multiplicacao(9,2)
#
# print("A Multiplicação dos números: {}".format(k))

# def multiplicacao(a,b):
#
#     num = a * b
#     return num
#
# print("A multiplicação dos numeros é: {}".format(multiplicacao(9,2)))

# Questão - 3

# def somar():
#
#     num1 = int(input("Digite um número: "))
#     num2 = int(input("Digite outro número: "))
#
#     soma_num = num1 + num2
#     return soma_num
#
# print("A soma dos números é: {}".format(somar()))
