import mysql.connector

# Função para conectar ao banco de dados
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_usuario"
    )

# Cadastrar usuário
def create_user():
    nome = input("Nome: ")
    email = input("Email: ")
    endereco = input("Endereço: ")

    # Validar campos
    if nome == "" or email == "" or endereco == "":
        print("Preencha todos os campos!")
        return

    conn = None
    cursor = None

    try:
        # Abre conexão e cursor
        conn = conectar()
        cursor = conn.cursor()

        # Comando SQL de inserção
        sql = "INSERT INTO usuarios (nome, email, endereco) VALUES (%s, %s, %s)"
        valores = (nome, email, endereco)

        cursor.execute(sql, valores)
        conn.commit()

        print("Usuário cadastrado!")

    except Exception as e:
        # Tratar erros
        print("Erro:", e)

    finally:
        # Fecha conexão
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# READ - Listar usuários
def read_users():
    conn = None
    cursor = None

    try:
        # Conecta ao banco
        conn = conectar()
        cursor = conn.cursor()

        # Consulta SQL
        cursor.execute("SELECT * FROM usuarios")
        dados = cursor.fetchall()

        print("\nLista de usuários:")
        for u in dados:
            print(f"ID: {u[0]} | Nome: {u[1]} | Email: {u[2]} | Endereço: {u[3]}")

    except Exception as e:
        print("Erro:", e)

    finally:
        # Fecha conexão
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# UPDATE - Atualizar usuário
def update_user():
    user_id = input("ID do usuário: ")
    nome = input("Novo nome: ")
    email = input("Novo email: ")
    endereco = input("Novo endereço: ")

    # Validação
    if user_id == "" or nome == "" or email == "" or endereco == "":
        print("Preencha todos os campos!")
        return

    conn = None
    cursor = None

    try:
        # Conecta ao banco
        conn = conectar()
        cursor = conn.cursor()

        # Comando SQL de atualização
        sql = "UPDATE usuarios SET nome=%s, email=%s, endereco=%s WHERE id=%s"
        valores = (nome, email, endereco, user_id)

        cursor.execute(sql, valores)
        conn.commit()

        print("Usuário atualizado!")

    except Exception as e:
        print("Erro:", e)

    finally:
        # Fecha conexão
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# DELETE - Remover usuário
def delete_user():
    user_id = input("ID para excluir: ")

    # Validação
    if user_id == "":
        print("Informe o ID!")
        return

    conn = None
    cursor = None

    try:
        # Conecta ao banco
        conn = conectar()
        cursor = conn.cursor()

        # Comando SQL de exclusão
        sql = "DELETE FROM usuarios WHERE id=%s"
        cursor.execute(sql, (user_id,))
        conn.commit()

        print("Usuário excluído!")

    except Exception as e:
        print("Erro:", e)

    finally:
        # Fecha conexão
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# MENU - Interface no terminal
def menu():
    while True:
        print("\n===== CRUD USUÁRIOS =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Sair")

        op = input("Escolha: ")

        # Direciona para cada função
        if op == "1":
            create_user()
        elif op == "2":
            read_users()
        elif op == "3":
            update_user()
        elif op == "4":
            delete_user()
        elif op == "0":
            print("Encerrado.")
            break
        else:
            print("Opção inválida!")


# EXECUÇÃO do sistema
menu()