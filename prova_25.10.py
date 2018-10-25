import sqlite3
import getpass

# --- Funções ----
def criar_tab_usua(conexao):

    cursor = conexao.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS usua(
    nome text,
    telefone text,
    senha text
    );"""

    cursor.execute(sql)
# ----------------------------------------------------------------------------
def inserir_usua(conexao, nome, telefone, senha):

    cursor = conexao.cursor()

    sql = """INSERT INTO usua VALUES(
    '{}',
    '{}',
    '{}'
    );
    """.format(nome, telefone, senha)

    cursor.execute(sql)

    conexao.commit()
# ----------------------------------------------------------------------------
def buscar_usua(conexao, nome):

    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM usua WHERE nome LIKE '%{}%';".format(nome)

    cursor.execute(sql)

    usua = cursor.fetchall()

    for u in usua:
        print("\n{}: {} - {}".format(u[0], u[1], u[2]))
# -----------------------------------------------------------------------------

def listar_usua(conexao):

    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM usua ORDER BY nome;"

    cursor.execute(sql)

    usua = cursor.fetchall()

    for u in usua:
        print("{}: {} - {}".format(u[0], u[1], u[2]))
# -----------------------------------------------------------------------------

print("\n--- Abrindo Conexão com o Banco ---\n")
conexao = sqlite3.connect("bd.prova")

opcao = 0
while opcao != 4:
    print(""" --- Menu ---

    1 - Inserir
    2 - Buscar
    3 - Listar
    4 - Sair

     """)

    opcao = int(input("Digite uma das opções: "))

    if opcao == 1:
        print("\n--- Inserir Usuários ---\n")

        n = input("Digite seu nome: ")
        t = input("Digite seu telefone: ")
        s = getpass.getpass("Digite sua senha: ")

        inserir_usua(conexao, n, t, s)
        print("\n--- Usuário Inserido com Sucesso ---\n")

    elif opcao == 2:
        print("\n--- Buscar Usuários ---\n")

        n = input("Digite seu nome: ")

        buscar_usua(conexao, n)
        print("\n--- Resultado da Busca ---\n")

    elif opcao == 3:

        print("\n--- Usuários Cadastrados ---\n")
        listar_usua(conexao)

    elif opcao == 4:
        print("\n--- Fechando o Programa ---")
        break

print("\n--- Fechando Conexão com o Banco ---")
conexao.close()
