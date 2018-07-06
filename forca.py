from random import randint

lista_palavras = ["casa", "mercado", "palio", "palmeiras", "lakers", "lucas"]

print('''==============================
     JOGO DA FORCA - IFPR
==============================''')
print("\n")

print('''==============================
     Pronto para Começar...?
==============================''')
print("\n")

aceita = 1
n_aceita = 0

while True:
    inicio = int(input("Digite (1) para Inicar ou (0) para Sair: "))

    if inicio == aceita:

        pos= randint (0, len(lista_palavras)-1)
        palavra = lista_palavras[pos]
        riscos = [" _ "] * len(palavra)


        print("\n")
        print("Começando o jogo....FORCA - IFPR")

        erros = 0

        while erros < 7 :
            letra = input("Digite uma letra: ")

            #percorrer a palavra e ver se a letra está na palavra


        print(palavra)
        print(riscos)

    elif inicio == n_aceita:
        print("Saindo do jogo....")
        print("\n")
        print("Obrigado!")
        clear()
        break
