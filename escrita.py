arq = open("arquivos/nomes.txt", "w")

nome  = input("Informe seu nome completo: ")

arq.write(nome)
arq.write("\n")

print(nome)

print("Fechando o arquivo...")


arq.close()
