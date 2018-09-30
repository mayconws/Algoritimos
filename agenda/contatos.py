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

    print("\033[36mId Nome    Telefone     E-mail\n\033[0;0m")
    print("\033[36m== ======= ===========  ================\n\033[0;0m")
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

    print("\033[36mId Nome    Telefone  E-mail\n\033[0;0m")
    print("\033[36m== ======= ========  ================\n\033[0;0m")
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

print("\033[41m\033[37mConectando no banco...\n\033[0;0m")
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

    opcao = int(input("\033[33mInforme a opção desejada: \033[0;0m"))

    if opcao == 1:
        print("\033[44m\033[37m\n--- Digite os dados do contato ---\n\033[0;0m")

        n = input("Nome: ")
        t = input("Telefone: ")
        e = input("E-mail: ")
        i = int(input("Id: "))

        if n == "":
            print("\033[44m\033[37m\nEspaço vazio! Digite um nome...\033[0;0m")

        if t == "":
            print("\033[44m\033[37m\nEspaço vazio! Digite um login...\033[0;0m")

        if e == "":
            print("\033[44m\033[37m\nEspaço vazio! Digite um senha...\033[0;0m")

        print("\033[44m\033[37m\n--- Contato inserido com sucesso ---\n\033[0;0m")

        inserir_contato(conexao, n, t, e, i)

    elif opcao == 2:
        print("\033[44m\033[37m\n--- Buscar Registro ---\n\033[0;0m")

        nome = input("Digite o nome do contato: ")
        print("\033[44m\033[37m\n--- Registros Encontrados ---\n\033[0;0m")
        buscar_contato(conexao, nome)


    elif opcao == 3:
        print("\033[44m\033[37m\n--- Lista de contatos cadastrados ---\n\033[0;0m")
        listar_contato(conexao)

    elif opcao == 4:
        print("\033[44m\033[37m\n--- Alteraçao de Contatos ---\n\033[0;0m")

        n = input("Nome: ")
        t = input("Telefone: ")
        e = input("Email: ")
        i = int(input("Id: "))
        alterar_contato(conexao, n, t, e, i)
        print("\033[44m\033[37m\n--- Alteração realizada com sucesso ---\n\033[0;0m")

    elif opcao == 5:
        print("\033[44m\033[37m\n--- Exclusão de Registro ---\n\033[0;0m")

        id = input("Digite o ID para do contato para excluir: ")
        excluir_contato(conexao, id)
        print("\033[44m\033[37m\n--- Contato excluido com sucesso ---\033[0;0m")

    elif opcao == 6:
        print("\033[44m\033[37m\n--- Voltando ----\n\033[0;0m")
        menuUsuario()

print("\033[41m\033[37m\nFechando conexão com o banco...\033[0;0m")
conexao.close()
