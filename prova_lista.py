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


# Questão - 2 O método deve receber um vetor de números inteiros por parâmetro e retornar um
# vetor com os valores elevados ao quadrado se o índice (posição) do respectivo número
# for par e ao cubo se o índice for ímpar. Atenção com o tipo do retorno!
