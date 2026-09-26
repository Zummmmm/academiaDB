from banco import conectar


def cadastrar_matricula():
    aluno_id = input("ID do aluno: ")
    plano_id = input("ID do plano: ")
    data_inicio = input("Data de início (AAAA-MM-DD): ")
    data_fim = input("Data de fim (AAAA-MM-DD ou vazio): ")

    if data_fim == "":
        data_fim = None

    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO matricula
                (aluno_id, plano_id, data_inicio, data_fim)
            VALUES
                (%s, %s, %s, %s)
        """, (
            aluno_id,
            plano_id,
            data_inicio,
            data_fim
        ))

        conexao.commit()

        print("Matrícula criada!")

    except Exception as erro:
        conexao.rollback()
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()


def listar_matriculas():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                m.id,
                a.nome,
                p.nome,
                m.data_inicio,
                m.data_fim,
                m.status
            FROM matricula m
            JOIN aluno a
                ON a.id = m.aluno_id
            JOIN plano p
                ON p.id = m.plano_id
            ORDER BY m.id
        """)

        matriculas = cursor.fetchall()

        print("\n===== MATRÍCULAS =====")

        for matricula in matriculas:
            print(
                f"ID: {matricula[0]} | "
                f"Aluno: {matricula[1]} | "
                f"Plano: {matricula[2]} | "
                f"Início: {matricula[3]} | "
                f"Fim: {matricula[4]} | "
                f"Status: {matricula[5]}"
            )

    except Exception as erro:
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()


def cancelar_matricula():
    id_matricula = input("ID da matrícula: ")

    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE matricula
            SET status = 'CANCELADA'
            WHERE id = %s
        """, (id_matricula,))

        if cursor.rowcount == 0:
            print("Matrícula não encontrada.")
        else:
            conexao.commit()
            print("Matrícula cancelada.")

    except Exception as erro:
        conexao.rollback()
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()
