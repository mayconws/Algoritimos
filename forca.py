print('''====================
JOGO DA FORCA - IFPR
====================''')
print('')

print('''====================
Pronto para Começar...?
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

palavras = [
    "ifpr",
    "cachorro",
    "caminhão",
    "corinthians",
    "paralelepipido",
]

dicas = [
    "É uma instituição de ensino",
    "É um animal",
    "É um veículo",
    "maior time do Brasil",
    "Uma forma geometrica"
]
