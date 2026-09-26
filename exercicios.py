from banco import conectar


def cadastrar_exercicio():
    nome = input("Nome do exercício: ")
    grupo = input("Grupo muscular: ")
    descricao = input("Descrição: ")

    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO exercicio
                (nome, grupo_muscular, descricao)
            VALUES
                (%s, %s, %s)
        """, (
            nome,
            grupo,
            descricao
        ))

        conexao.commit()

        print("Exercício cadastrado!")

    except Exception as erro:
        conexao.rollback()
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()


def listar_exercicios():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, nome, grupo_muscular, descricao
            FROM exercicio
            ORDER BY id
        """)

        exercicios = cursor.fetchall()

        print("\n===== EXERCÍCIOS =====")

        for exercicio in exercicios:
            print(f"""
ID: {exercicio[0]}
Nome: {exercicio[1]}
Grupo muscular: {exercicio[2]}
Descrição: {exercicio[3]}
-------------------------
""")

    except Exception as erro:
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()
