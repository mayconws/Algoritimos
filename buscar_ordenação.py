# def buscar(lista, n):
#
#     for i in lista:
#         print(i)
#
#         if i == num:
#
#             return True
#
#     return False
#
# lista = [1,2,3,4,5]
#
# num = 3
#
# print(buscar(lista, num))

# def buscar(lista, n):
#
#     cont = 0
#
#     for i in lista:
#         print(i)
#
#         if i == num:
#             cont = cont + 1
#
#         if i > num and cont > 0:
#             break
#
#     return cont
#
# lista = [1,2,3,3,3,3,4,5,3,6,7,8,9,10]
#
# num = 3
#
# print("A quantidade de numeros repetidos é", buscar(lista, num))

def fatR(n):
    ''' (int) -> int '''
    if n == 0:
        return 1
    else:
        return n * fatR(n-1)

# testes
print("Fatorial de 0: ", fatR(0))
print("Fatorial de 1: ", fatR(1))
print("Fatorial de 2: ", fatR(2))
print("Fatorial de 3: ", fatR(3))
print("Fatorial de 5: ", fatR(5))
