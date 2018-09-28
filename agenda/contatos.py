import sqlite3

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

    for cont in contato:
        print( "{}: {} ({})".format(cont[0], cont[1], cont[2]) )
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

    for cont in contato:
        print( "{}: {} ({})".format(cont[0], cont[1], cont[2]) )
# ----------------------------------------------------------------

def alterar_contato(conexao, nome):

    cursor = conexao.cursor()

    sql = "UPDATE contato SET nome = '{}', fone = '{}', email = '{}' WHERE rowid = {}".format

    cursor.execute(sql)
# -----------------------------------------------------------------------

# ========== Menu Principal ==========

print("Conectando no banco...\n")
conexao = sqlite3.connect("banco.sqlite")

opcao = 0
while opcao != 6:
    print("""
Em relação aos contatos do sistema, você deseja...

    1 - Inserir
    2 - Buscar
    3 - Listar
    4 - Alterar
    5 - Excluir
    6 - Voltar
""")

    opcao = int(input("Opção desejada: "))

    if opcao == 1:
        print("\n--- Digite os dados do contatos ---\n")

        n = input("Nome: ")
        t = input("Telefone: ")
        e = input("Email: ")
        i = int(input("Id: "))

        if n == "":
            print("Espaço vazio! Digite um nome...")

        if t == "":
            print("Espaço vazio! Digite um login...")

        if e == "":
            print("Espaço vazio! Digite um senha...")

        inserir_contato(conexao, n, t, e, i)

    elif opcao == 2:
        print("\n--- Buscar registro ---\n")

        nome = input("Digite o nome do contato: ")
        buscar_contato(conexao, nome)

    elif opcao == 3:
        print("\n--- Listando Contatos ---\n")
        listar_contato(conexao)

    elif opcao == 4:
        print("\n--- Alterando Contatos ---\n")

        nome = input("Digite o nome do contato: ")
        alterar_contato(conexao, nome)

    elif opcao == 5:
        print("\n--- Exclusão de registro ---")

    elif opcao == 6:
        print("\n--- Saindo ----\n")
        break

print("\n\nFechando conexão com o banco...")
conexao.close()
