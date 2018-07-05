def clear():
    print("\n")

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
        print("\n")
        print("Começando o jogo....FORCA - IFPR")
        break

    elif inicio == n_aceita:
        print("Saindo do jogo....")
        print("\n")
        print("Obrigado!")
        clear()
        break

palavras = [
    "ifpr",
    "cachorro",
    "mundial",
    "testando",
    "palavra composta"
]

letras_digitas = []
erros = []
