opcao = 0
while opcao != 3:
    print('''===== Menu =====
         1. Cadastrar Palavras
         2. Listar Palvaras
         3. Sair do programa
         =================''')

    opcao = int(input("Digite a opção selecionada: "))

    if opcao == 1:

        arq1 = open("arquivos/nomes.txt", "a")

        palavra  = input("Informe seu nome completo: ")

        arq1.write(palavra)
        arq1.write("\n")

        print(palavra)

        arq1.close()

    elif opcao == 2:

        arq1 = open("arquivos/nomes.txt", "r")

        conteudo = arq1.readlines()

        arq1.close()

        l = 0

        while l < len(conteudo) :
            print(conteudo[l])
            l+=1

    elif opcao == 3:
        print("Saindo do Pragrama...")
        break
