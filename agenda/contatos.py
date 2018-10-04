from usuario import *

# --- Função para criar a tabela ----
def criar_tabela_contato(conexao):

    cursor = conexao.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS contato (
            nome text,
            fone text,
            email text,
            usuario integer
        );
    """

    cursor.execute(sql)

    conexao.commit()
# --------------------------------------------

#  --- Função para inserir o contato ---
def inserir_contato(conexao, nome, telefone, email, id):

    cursor = conexao.cursor()

    sql = """
        INSERT INTO contato VALUES(
            '{}',
            '{}',
            '{}',
             {}
        );
    """.format(nome, telefone, email, id)

    cursor.execute(sql)

    conexao.commit()
# --------------------------------------------

# --- Função para listar contatos ---
def listar_contato(conexao):

    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM contato ORDER BY nome;"

    cursor.execute(sql)

    contato = cursor.fetchall()

    print("\033[32mId Nome    Telefone     E-mail\033[0;0m\n")
    print("\033[32m== ======= ===========  ================\033[0;0m\n")
    for cont in contato:
        print("{}: {} - ({}) -".format(cont[0], cont[1], cont[2]), cont[3] )
# -----------------------------------------------------------

# --- Função para excluir contatos ---
def excluir_contato(conexao, id):

    cursor = conexao.cursor()

    sql = """
        DELETE FROM contato
        WHERE rowid = {};
    """.format(id)

    cursor.execute(sql)

    conexao.commit()
# ---------------------------------------------------------------

# --- Função para buscar contatos ---
def buscar_contato(conexao, nome):

    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM contato WHERE nome LIKE '%{}%';".format(nome)

    cursor.execute(sql)

    contato = cursor.fetchall()

    print("\033[32mId Nome    Telefone  E-mail\033[0;0m\n")
    print("\033[32m== ======= ========  ================\033[0;0m\n")
    for cont in contato:
        print( "{}: {} - ({}) -".format(cont[0], cont[1], cont[2]), cont[3] )
# ----------------------------------------------------------------

# --- Função para alterar contatos ---
def alterar_contato(conexao, nome, telefone, email, id):

    cursor = conexao.cursor()

    sql = "UPDATE contato SET nome = '{}', fone = '{}', email = '{}' WHERE rowid = {}".format(nome, telefone, email, id)

    cursor.execute(sql)

    conexao.commit()
# -----------------------------------------------------------------------------------------------------------------------

# ========== Menu Principal ==========

print("\n\033[47m\033[31mConectando no banco...\033[0;0m\n")
conexao = sqlite3.connect("banco.sqlite")

opcao = 0
while opcao != 6:
    print("""\033[32m
Em relação aos contatos do sistema, você deseja...

    1 - Inserir
    2 - Buscar
    3 - Listar
    4 - Alterar
    5 - Excluir
    6 - Voltar
\033[0;0m""")

    opcao = int(input("\033[32mInforme a opção desejada: \033[0;0m"))

    if opcao == 1:
        print("\n\033[47m\033[30m--- Digite os dados do contato ---\033[0;0m\n")

        n = input("Nome: ")
        t = input("Telefone: ")
        e = input("E-mail: ")
        i = int(input("Id: "))

        if n == "":
            print("\n\033[47m\033[30mEspaço vazio! Digite um nome...\033[0;0m")

        if t == "":
            print("\n\033[47m\033[30mEspaço vazio! Digite um login...\033[0;0m")

        if e == "":
            print("\n\033[47m\033[30mEspaço vazio! Digite um senha...\033[0;0m")

        print("\n\033[47m\033[30m--- Contato inserido com sucesso ---\033[0;0m\n")

        inserir_contato(conexao, n, t, e, i)

    elif opcao == 2:
        print("\n\033[47m\033[30m--- Buscar Registro ---\033[0;0m\n")

        nome = input("Digite o nome do contato: ")
        print("\n\033[47m\033[30m--- Registros Encontrados ---\033[0;0m\n")
        buscar_contato(conexao, nome)


    elif opcao == 3:
        print("\n\033[47m\033[30m--- Lista de contatos cadastrados ---\033[0;0m\n")
        listar_contato(conexao)

    elif opcao == 4:
        print("\n\033[47m\033[30m--- Alteraçao de Contatos ---\033[0;0m\n")

        n = input("Nome: ")
        t = input("Telefone: ")
        e = input("Email: ")
        i = int(input("Id: "))
        alterar_contato(conexao, n, t, e, i)
        print("\n\033[47m\033[30m--- Alteração realizada com sucesso ---\033[0;0m\n")

    elif opcao == 5:
        print("\n\033[47m\033[30m--- Exclusão de Registro ---\033[0;0m\n")

        id = input("Digite o ID para do contato para excluir: ")
        excluir_contato(conexao, id)
        print("\n\033[47m\033[30m--- Contato excluido com sucesso ---\033[0;0m")

    elif opcao == 6:
        print("\n\033[47m\033[30m--- Voltando ----\033[0;0m\n")
        menuUsuario()

print("\n\033[47m\033[31mFechando conexão com o banco...\033[0;0m\n")
conexao.close()
