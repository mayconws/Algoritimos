print('''====================
JOGO DA FORCA - IFPR
====================''')
print('')

print('''====================
Vamos Jogar?
====================''')
print('')

aceita = 1
n_aceita = 0

while True:
    inicio = int(input("Digite (1) para Inicar ou (0) para Sair: "))
    if inicio == aceita:
        print("Começando o jogo....FORCA - IFPR")
        break

    elif inicio == n_aceita:
        print("Saindo do jogo....Obrigado!")
        break

    else:
        print("Digite uma Opção Válida!")

palvaras = ["azul"]

print("Digite uma letra para a palavra abaixo....")
