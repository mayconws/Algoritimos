opcao = 0
while opcao != 4:
    print('''===== Menu - Forca =====

1. Iniciar o Jogo
2. Cadastrar Palavras
3. Cadastrar Dicas
4. Sair do jogo

========================''')

    opcao = int(input("Digite a opção selecionada: "))

    if opcao == 2:

        arq1 = open("arquivos/palavra.txt", "a")

        palavra  = input("Informe a palavra: ")

        arq1.write(palavra)
        arq1.write("\n")

        arq1.close()

        arq1 = open("arquivos/palavra.txt", "r")

        conteudo = arq1.readlines()

        arq1.close()

    elif opcao == 3:

        arq2 = open("arquivos/dica.txt", "a")

        dica  = input("Informe a 'DICA' para a palavra: ")

        arq2.write(dica)
        arq2.write("\n")

        arq2 = open("arquivos/dica.txt", "r")

        conteudo = arq2.readlines()

        arq2.close()

    elif opcao == 4:
        print("Saindo do Pragrama...")
        break
