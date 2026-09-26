from banco import conectar


def cadastrar_aluno():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO aluno
                (nome, cpf, data_nascimento, telefone, email)
            VALUES
                (%s, %s, %s, %s, %s)
        """, (
            nome,
            cpf,
            data_nascimento,
            telefone,
            email
        ))

        conexao.commit()

        print("Aluno cadastrado com sucesso!")

    except Exception as erro:
        conexao.rollback()
        print("Erro ao cadastrar aluno:", erro)

    finally:
        cursor.close()
        conexao.close()


def listar_alunos():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, nome, cpf, data_nascimento, telefone, email
            FROM aluno
            ORDER BY id
        """)

        alunos = cursor.fetchall()

        print("\n===== ALUNOS =====")

        for aluno in alunos:
            print(f"""
ID: {aluno[0]}
Nome: {aluno[1]}
CPF: {aluno[2]}
Nascimento: {aluno[3]}
Telefone: {aluno[4]}
Email: {aluno[5]}
------------------------
""")

    except Exception as erro:
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()


def buscar_aluno():
    id_aluno = input("Digite o ID do aluno: ")

    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, nome, cpf, data_nascimento, telefone, email
            FROM aluno
            WHERE id = %s
        """, (id_aluno,))

        aluno = cursor.fetchone()

        if aluno is None:
            print("Aluno não encontrado.")
        else:
            print(f"""
ID: {aluno[0]}
Nome: {aluno[1]}
CPF: {aluno[2]}
Nascimento: {aluno[3]}
Telefone: {aluno[4]}
Email: {aluno[5]}
""")

    except Exception as erro:
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()


def excluir_aluno():
    id_aluno = input("Digite o ID do aluno: ")

    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM aluno
            WHERE id = %s
        """, (id_aluno,))

        if cursor.rowcount == 0:
            print("Aluno não encontrado.")
        else:
            conexao.commit()
            print("Aluno excluído.")

    except Exception as erro:
        conexao.rollback()
        print("Não foi possível excluir:", erro)

    finally:
        cursor.close()
        conexao.close()
