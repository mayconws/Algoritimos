fileh = open("arquivos/numeros.txt", "r")

conteudo = fileh.readlines()

fileh.close()

l = 0

while l < len(conteudo) :
    print(conteudo[l])
    l+=1
