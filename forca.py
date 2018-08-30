from random import randint

def tentativa1():

    print('''
    |─|─────────────────|
    | |               (o.o)
    | |
    | |
    | |
    | |
    | |
    | |
    |_|=====================
    você tem 6 tentativas
    ========================
    ''')
def tentativa2():
    print('''
    |─|─────────────────|
    | |               (o.o)
    | |                ||
    | |                ||
    | |                ||
    | |
    | |
    | |
    |_|=====================
    você tem 5 tentativas
    ========================
    ''')
def tentativa3():
    print('''
    |─|─────────────────|
    | |               (o.o)
    | |                ||_
    | |                || \\
    | |                ||  \\
    | |
    | |
    | |
    |_|=====================
    você tem 4 tentativas
    ========================
    ''')
def tentativa4():
    print('''
    |─|─────────────────|
    | |               (o.o)
    | |               _||_
    | |              / || \\
    | |             /  ||  \\
    | |
    | |
    | |
    |_|=====================
    você tem 3 tentativas
    ========================
    ''')
def tentativa5():
    print('''
    |─|─────────────────|
    | |               (o.o)
    | |               _||_
    | |              / || \\
    | |             /  ||  \\
    | |                /
    | |              _/
    | |
    |_|=====================
    você tem 2 tentativas
    ========================
    ''')
def tentativa6():
    print('''
    |─|─────────────────|
    | |               (o.o)
    | |               _||_
    | |              / || \\
    | |             /  ||  \\
    | |                /\\
    | |              _/  \\_
    | |
    |_|================================
    Última Chance !!! Tome cuidado !!!
    ===================================
    ''')
def campeao():
    print(''' =-=-=-=-=- PARABÉNS VOCÊ GANHOU !!!! =-=-=-=-=-''')
def final():
    print(''' ========== VOCÊ PERDEU !!! ==========''')

lista_palavras = ["casa", "shopping", "palio", "palmeiras", "lakers", "lucas", "acdc", "dinossauro"]
lista_dicas = ["DICA: Local de descanso...", "DICA: Ir as compras...", "DICA: Carro popular", "DICA: Time sem mundial...", "DICA: Time da NBA...", "DICA: Companheiro de sala conhecido como Nethoes...", "DICA: Banda de Rock...", "DICA: Animal Pré Histórico..."]

print('''====================================
   JOGO DA FORCA - IFPR
====================================''')
print("\n")

print('''====================================
Pronto para Começar...?
====================================''')
print("\n")

pos = randint (0, len(lista_palavras)-1)
palavra = lista_palavras[pos]
riscos = ["_"] * len(palavra)
letras_digitadas = []

print("\n")
print("Começando o jogo....FORCA - IFPR")

print("\n")
print(lista_dicas[pos])
print("\n")
print(riscos)
print("\n")

erros = 0

while erros < 7 :
    letra = input("Digite uma letra: ").lower()

# Esquema para conferir se a letra está presente na palavra,
# estando presente, ela substitui a posição equivalente dela na string palavra na lista
# de riscos, senão o número de erros aumenta em 1.

    if letra in palavra:
        pos = palavra.find(letra)
        for i in range(pos, len(palavra)):
            if letra == palavra[i]:
                riscos[i] = letra

    else:
        erros = erros + 1

    if erros == 1:
        tentativa1()
    elif erros == 2:
        tentativa2()
    elif erros == 3:
        tentativa3()
    elif erros == 4:
            tentativa4()
    elif erros == 5:
            tentativa5()
    elif erros == 6:
            tentativa6()
    if erros == 7:
        print("\n")
        final()
        print("\n")
    break

# Coloquei a impressão dos riscos dentro do loop do While para que seja possível
# ver as letras acertadas enquanto se digita novas.

    print(' '.join(riscos))

        # Condição para verifcar se a letra já foi digitada.

    if letra in letras_digitadas:
        print("Você já tentou essa Letra. Digite Novamente !!!")

    else:
        letras_digitadas.append(letra)

    # Se a palvara for igual a quantidade de riscos, acertou a palavra e ganhou
    # o jogo!

    if palavra == ''.join(riscos):
        campeao()
        break

    else:
        print("Saindo do jogo....")
        print("\n")
        print("Obrigado!")
        break
