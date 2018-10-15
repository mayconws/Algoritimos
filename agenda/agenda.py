from usuario import *
from contatos import *
import getpass

# Menu Principal Agenda ---

print("\n\033[47m\033[31mConectando no banco...\033[0;0m\n")
conexao = sqlite3.connect("banco.sqlite")

opcao = 0
while opcao != 2:
    print("""--- Menu Agenda ---

    1 - Entrar
    2 - Sair
""")

    opcao = int(input("Escolha uma das opções: "))
    if opcao == 1:
        print("\n--- Efetuar Login no Sistema ---\n")
        usuario = input("Por favor, informe o usuário: ")
        senha = getpass.getpass("Por favor, informe a senha: ")
        login(conexao, usuario, senha)
    elif opcao == 2:
        print("\nFechando o programa....\n")
        break

print("\n\033[47m\033[31mFechando conexão com o banco...\033[0;0m\n")
conexao.close()
