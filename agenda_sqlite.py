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

    for usr in usuarios:
        print( "{}: {} ({})".format(usr[0], usr[1], usr[2]) )
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
def buscar_usuario(conexao):

    cursor = conexao.cursor()

    sql = ""

    cursor.execute(sql)
# -----------------------------------------------------------------

# --- Menu Principal do Programa ---

print("Conectando no banco...\n")
conexao = sqlite3.connect("agenda.sqlite")

opcao = 0
while opcao != 6:
    print("""
Em relação aos usuários do sistema, você deseja...

    1 - Inserir
    2 - Buscar
    3 - Listar
    4 - Alterar
    5 - Excluir
    6 - Sair
""")

    opcao = int(input("Opção desejada: "))

    if opcao == 1:
        print("\n--- Digite os dados do usuário ---\n")

        n = input("Nome: ")
        l = input("Login: ")
        s = input("Senha: ")

        if n == "":
            print("Espaço vazio! Digite um nome...")

        if l == "":
            print("Espaço vazio! Digite um login...")

        if s == "":
            print("Espaço vazio! Digite um senha...")

        criar_tabela_usuario(conexao)
        inserir_usuario(conexao, n, l, s)

    elif opcao == 2:
        print("\n--- Buscar registro ---\n")

        # Exemplo de sql para consultar tudo que contenah o nome digitado
        # "SELECT ...... WHERE nome LIKE '%{}%';".format(nome)

    elif opcao == 3:
        print("\n--- Listagem registros ---\n")
        listar_usuarios(conexao)

    elif opcao == 4:
        print("\n--- Alteração de registros ---\n")

    elif opcao == 5:
        print("\n--- Exclusão de registro ---")

    elif opcao == 6:
        print("\n--- Saindo ----\n")
        break
# Fechando a conexão (ligação) com o banco
print("\n\nFechando conexão com o banco...")
conexao.close()
