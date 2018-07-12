from random import randint

# Deesenhos dos erros da Forca..... Com a função (def).
def erro1():
    print("""
|─|─────────────────|
| |               (--)
| |
| |
| |
| |
| |
| |
|_|______________________
você tem 6 tentativas
─────────────────────────
""")
def erro2():
    print("""
|─|─────────────────|
| |               (oo)
| |                ||
| |                ||
| |                ||
| |
| |
| |
|_|______________________
você tem 5 tentativas
─────────────────────────
""")
def erro3():
    print("""
|─|─────────────────|
| |               (oo)
| |                ||_
| |                || \\
| |                ||  \\
| |
| |
| |
|_|______________________
você tem 4 tentativas
─────────────────────────
""")
def erro4():
    print("""
|─|─────────────────|
| |               (oo)
| |               _||_
| |              / || \\
| |             /  ||  \\
| |
| |
| |
|_|______________________
você tem 3 tentativas
─────────────────────────
""")
def erro5():
    print("""
|─|─────────────────|
| |               (oo)
| |               _||_
| |              / || \\
| |             /  ||  \\
| |                /
| |              _/
| |
|_|______________________
você tem 2 tentativas
─────────────────────────
""")
def erro6():
    print("""
|─|─────────────────|
| |               (oo)
| |               _||_
| |              / || \\
| |             /  ||  \\
| |                /\\
| |              _/  \\_
| |
|_|_______________________
você só tem 1 tentativa!!!
──────────────────────────
""")
def ganhou():
    print(''' =-=-=-=-=- PARABÉNS VOCÊ GANHOU !!!! =-=-=-=-=-''')
def erro7():
    print(''' ========== VOCÊ PERDEU !!! ==========''')

# menu do Jogo da Forca.
print('''==============================
     JOGO DA FORCA - IFPR
==============================''')
print("\n")

print('''==============================
     Pronto para Começar...?
==============================''')
print("\n")

# Opções para inicar o jogo com a condição de While Verdadeiro.
aceita = 1
n_aceita = 0

while True:
    inicio = int(input("Digite (1) para Inicar ou (0) para Sair: "))

    if inicio == aceita:
        print("\n")
        print("Começando o jogo....FORCA - IFPR")

    elif inicio == n_aceita:
        print("Saindo do jogo....")
        print("\n")
        print("Obrigado!")
        break

    listaPalavras = ["casa", "shopping", "palio", "palmeiras", "lakers", "lucas", "acdc", "dinossauro"]
    listaDicas = ["DICA: Local de descanso...", "DICA: Ir as compras...", "DICA: Carro popular", "DICA: Time sem mundial...", "DICA: Time da NBA...", "DICA: Companheiro de sala conhecido como Nethoes...", "DICA: Banda de Rock...", "DICA: Animal Pré Histórico..."]

    # Escolha uma palavra no vetor da lista.
    x = randint(0,len(listaPalavras) - 1) # O -1 porque a lista começa em 0, se não tiver o -1 vai passar a quantidade de posições.
    escolhida = listaPalavras[x] # o "X" refere-se a posição escolhida, no caso escolhe uma palavra da lista.

    # listas vazias para armazenar dados
    descobertas = []
    digitadas = []

    for c in range(0,len(escolhida)): # Esse for percorre cada letra da palavra escolhida aleatoriamente, uma palavra pode ser uma lista.
        descobertas.append("_") # Coloca traço em todas as letras de descobertas.

    print(" _" * len(escolhida)) # Esse é apenas o print Inicial, antes do laço de repetição
    print(listaDicas[x])

    acertou = False
    erros = 0

    while acertou == False:
        acertos = 0
        print(" ")
        letra = input(str("Dígite uma letra: ")).lower() # Altera para letra minuscula.

        if letra in digitadas:
            print("Você já tentou essa letra !!") # Verifica se a letra ja foi digitada.
        else:
            digitadas.append(letra) # a letra vai para a lista de digitadas, para evitar repetições
            print(listaDicas[x])

            for c in range(0, len(escolhida)):
                if letra == escolhida[c]: #se alguma letra é igual a palavra da lista"escolhida"
                    descobertas[c] = letra #substitui o tracinho de descoberta pela letra
                    acertos+=1

                print(descobertas[c], end=' ')

            if acertos == 0:  # Contador de erros, se não tiver nenhum acerto na rodada, soma mais um erro
                erros+=1

            if erros == 1:
                erro1() # Função relacionada ao def inicial do desenho da forca.
            elif erros == 2:
                erro2()
            elif erros == 3:
                erro3()
            elif erros == 4:
                erro4()
            elif erros == 5:
                erro5()
            elif erros == 6:
                erro6()
            if erros == 7:
                erro7()
                break # Para o laço de repetição para finalizar o jogo.

            acertou = True # Se chegou até aqui acertou fica TRUE
            for z in range(0, len(descobertas)):
                if descobertas[z] == "_":
                    acertou = False # Volta se tiver algum tracinho ainda...

    if erros < 7: # Se o erro for < 7 Parabéns você Ganhou!!!
        print(" ")
        ganhou()
