import sqlite3

# ---  Funções do Programa ---

# --- Função 1: Criação da Tabela ---
def criar_tabela_usuario(conexao):

    cursor = conexao.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS usuario(
            nome text,
            login text,
            senha text
        );
    """

    cursor.execute(sql)
# ---------------------------------------------------

# --- Função 2: Inserir Usuário ---
def inserir_usuario(conexao, nome, login, senha):

    cursor = conexao.cursor()

    sql = """
        INSERT INTO usuario VALUES(
            '{}',
            '{}',
            '{}'
        );
    """.format(nome, login, senha)

    cursor.execute(sql)

    conexao.commit()
# ---------------------------------------------------

# --- Função 3: Listar Usuários ---
def listar_usuarios(conexao):

    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM usuario ORDER BY nome;"

    cursor.execute(sql)

    usuarios = cursor.fetchall()

    print("\033[36mId Nome    Login\n\033[0;0m")
    print("\033[36m== ======= =========\n\033[0;0m")
    for usr in usuarios:
        print( "{}: {} - ({})".format(usr[0], usr[1], usr[2]) )
# ---------------------------------------------------------------

# --- Função 4: Excluir Usuários ---
def excluir_usuario(conexao, id):

    cursor = conexao.cursor()

    sql = """
        DELETE FROM usuario
        WHERE rowid = {};
    """.format(id)

    cursor.execute(sql)

    conexao.commit()
# ---------------------------------------------------------------

# --- Função 5: Buscar Usuários ---
def buscar_usuario(conexao, nome ):

    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM usuario WHERE nome LIKE '%{}%';".format(nome)

    cursor.execute(sql)

    usuario = cursor.fetchall()

    print("\033[36mId Nome    Login\n\033[0;0m")
    print("\033[36m== ======= ========\n\033[0;0m")
    for usr in usuario:
        print( "{}: {} - ({})".format(usr[0], usr[1], usr[2]))
# -----------------------------------------------------------------

# --- Função 6: Alterar Contatos --
def alterar_usuario(conexao, nome, login, senha, id):

    cursor = conexao.cursor()

    sql = "UPDATE usuario SET nome = '{}', login = '{}', senha = '{}' WHERE rowid = {}".format(nome, login, senha, id)

    cursor.execute(sql)

    conexao.commit()
# ----------------------------------------------------------------------------------------------------------------

# --- Menu Principal do Programa ---

def menuUsuario():
    print("\033[41m\033[37mConectando no banco...\n\033[0;0m")
    conexao = sqlite3.connect("banco.sqlite")

    opcao = 0
    while opcao != 6:
        print("""\033[32m
Em relação aos usuários do sistema, você deseja...

        1 - Inserir
        2 - Buscar
        3 - Listar
        4 - Alterar
        5 - Excluir
        6 - Voltar
\033[0;0m""")

        opcao = int(input("\033[33mOpção desejada: \033[0;0m"))

        if opcao == 1:
            print("\033[47m\033[31m\n\n--- Digite os dados do usuário ---\n\n\033[0;0m")

            n = input("Nome: ")
            l = input("Login: ")
            s = input("Senha: ")

            if n == "":
                print("\n\033[47m\033[31mEspaço vazio! Digite um nome...\n\033[0;0m")

            if l == "":
                print("\n\033[47m\033[31mEspaço vazio! Digite um login...\n\033[0;0m")

            if s == "":
                print("\n\033[47m\033[31mEspaço vazio! Digite um senha...\n\033[0;0m")
            print("\033[47m\033[31m\n--- Contato inserido com sucesso ---\n\033[0;0m")

            inserir_usuario(conexao, n, l, s)

        elif opcao == 2:
            print("\033[47m\033[31m\n--- Buscar registro ---\n\n\033[0;0m")

            nome = input("Digite o nome do usuário para a busca: ")
            print("\033[47m\033[31m\n--- Registros Encontrados ---\n\033[0;0m")
            buscar_usuario(conexao, nome)

        elif opcao == 3:
            print("\033[47m\033[31m\n--- Lista de usuário cadastrados ---\n\033[0;0m")
            listar_usuarios(conexao)

        elif opcao == 4:
            print("\033[47m\033[31m\n--- Alteração de Usuários ---\n\033[0;0m")

            n = input("Nome: ")
            l = input("Login: ")
            s = input("Senha: ")
            i = input("Id: ")
            alterar_usuario(conexao, n, l, s, i)
            print("\033[47m\033[31m\n--- Alteração realizada com sucesso ---\n\033[0;0m")

        elif opcao == 5:
            print("\033[47m\033[31m\n--- Exclusão de registro ---\n\n\033[0;0m")

            id = input("Digite o ID para do contato para excluir: ")
            excluir_usuario(conexao, id)
            print("\033[47m\033[31m\n--- Usuário excluido com sucesso ---\033[0;0m")

        elif opcao == 6:
            print("\033[47m\033[31m\n--- Voltando ----\n\n\033[0;0m")
            break
    # Fechando a conexão (ligação) com o banco
    print("\033[41m\033[37m\nFechando conexão com o banco...\033[0;0m")
    conexao.close()
