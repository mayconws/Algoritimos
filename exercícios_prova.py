# Questinário - Tentativa 1

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
#     a = int(input("Digite um valor: "))
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

# def soma():
#     arquivo = open("arquivos/numeros.txt", "r")
#
#     conteudo = [ ]
#
#     conteudo = arquivo.readlines()
#
#     arquivo.close()
#
#     l = 0
#     soma = 0
#     while l < len(conteudo) :
#
#         numero = conteudo[l]
#         numero = int(numero)
#
#         soma = soma + numero
#
#         l+=1
#
#     print(soma)
#
# soma()

# Questionário - Karen
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

# Questionário - Tentativa 2

# 1 - Faça uma função sem parâmetro que pede um número inteiro para o usuário e imprime
# a metade desse número na tela.
#
# def num_metade():
#
#     valor = int(input("Digite um número inteiro: "))
#
#     metade = valor / 2
#
#     print("A metade do número é: {}".format(metade))
#
# num_metade()

# 2 - Faça uma função que recebe dois números inteiros por parâmetro
# e imprime somente o menor desses números na tela.

# def num_menor(num1,num2):
#
#     if num1 < num2:
#         return num1
#
#     else:
#         return num2
#
# numero = num_menor(12,9)
#
# print("O menor número: é {}".format(numero))

# 3 - O método deve solicitar ao usuário um número inteiro qualquer e retornar
# uma mensagem (String) informando se o número é par ou ímpar. O nome do método deve ser parOuImpar().

# def parOuImpar():
#
#     usuario = int(input("Digite um número inteiro: "))
#
#     if usuario % 2 == 0:
#         return ("O número é Par")
#
#     else:
#         return("O número é Impar")
#
# print(parOuImpar())

# 4 - Faça uma função que recebe por parâmetro o nome do arquivo, nome da pessoa e o ano de nascimento dela.
# A função deve abrir o arquivo informado e adicionar o nome e a idade da pessoa
# (considerando o ano atual que estamos) da seguinte forma:

def usuario(arquivo,nome,ano):

    usuario.write("João, 20")
    usuario.write("\n")

usuario("idade.txt","joão",20)
