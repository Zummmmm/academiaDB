from banco import conectar


def cadastrar_plano():
    nome = input("Nome do plano: ")
    valor = input("Valor: ")
    duracao = input("Duração em dias: ")

    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO plano
                (nome, valor, duracao_dias)
            VALUES
                (%s, %s, %s)
        """, (
            nome,
            valor,
            duracao
        ))

        conexao.commit()

        print("Plano cadastrado!")

    except Exception as erro:
        conexao.rollback()
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()


def listar_planos():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, nome, valor, duracao_dias
            FROM plano
            ORDER BY id
        """)

        planos = cursor.fetchall()

        print("\n===== PLANOS =====")

        for plano in planos:
            print(
                f"ID: {plano[0]} | "
                f"Nome: {plano[1]} | "
                f"Valor: R$ {plano[2]} | "
                f"Duração: {plano[3]} dias"
            )

    except Exception as erro:
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()


def excluir_plano():
    id_plano = input("ID do plano: ")

    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM plano
            WHERE id = %s
        """, (id_plano,))

        if cursor.rowcount == 0:
            print("Plano não encontrado.")
        else:
            conexao.commit()
            print("Plano excluído.")

    except Exception as erro:
        conexao.rollback()
        print("Não foi possível excluir:", erro)

    finally:
        cursor.close()
        conexao.close()
