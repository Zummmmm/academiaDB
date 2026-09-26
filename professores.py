from banco import conectar


def cadastrar_professor():
    nome = input("Nome: ")
    cref = input("CREF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO professor
                (nome, cref, telefone, email)
            VALUES
                (%s, %s, %s, %s)
        """, (
            nome,
            cref,
            telefone,
            email
        ))

        conexao.commit()

        print("Professor cadastrado!")

    except Exception as erro:
        conexao.rollback()
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()


def listar_professores():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, nome, cref, telefone, email
            FROM professor
            ORDER BY id
        """)

        professores = cursor.fetchall()

        print("\n===== PROFESSORES =====")

        for professor in professores:
            print(
                f"ID: {professor[0]} | "
                f"Nome: {professor[1]} | "
                f"CREF: {professor[2]} | "
                f"Telefone: {professor[3]} | "
                f"Email: {professor[4]}"
            )

    except Exception as erro:
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()
