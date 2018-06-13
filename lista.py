# t = int(input("Tamanho da lista: "))
# lista = [""]*t

# p = 0
# while p < len(lista):
#     lista[p] = int(input("Numero: "))
#     p = p + 1

#Fazendo a soma de valores
# soma = 0
# p = 0
# while p < len(lista):
#     lista[p] = int(input("Numero: "))
#     soma = soma + lista[p]
#     p = p + 1
# print("A soma é : ", soma)
# print("A média é: ", soma/len(lista))
#
# soma = 0
# pesos = 0
# p = 0
# while p < len(lista):
#     soma = soma + lista[p]*p
#     pesos = pesos + p
#     p = p + 1
#

# medpon = soma / pesos
# print("A média POnderada é: ", medpon)

t = int(input("Tamanho da lista: "))
lista = [""]*t

p = 0
while p < len(lista):
    lista[p] = int(input("Numero: "))
    p = p + 1

par = 0
impar = 0
p = 0
while p < len(lista):
    if lista[p] % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    p = p + 1

print("A quatidade de Par é: ", par)
print("A quatidade de Impar é: ", impar)
