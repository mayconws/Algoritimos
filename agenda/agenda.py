from usuario import *
from contatos import *


# Menu Principal Agenda ---

print("""\n--- Informe o Usuário e o Login para acessar o sistema: \n""")

print("--- Login ---")

usuario = input("Informe o usuário: ")

senha = input("Informe a senha: ")

u = login(conexao, nome, senha)
