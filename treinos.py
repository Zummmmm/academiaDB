from banco import conectar


def criar_treino():
    matricula_id = input("ID da matrícula: ")
    professor_id = input("ID do professor: ")
    nome = input("Nome do treino: ")
    objetivo = input("Objetivo: ")

    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO treino
                (matricula_id, professor_id, nome, objetivo)
            VALUES
                (%s, %s, %s, %s)
            RETURNING id
        """, (
            matricula_id,
            professor_id,
            nome,
            objetivo
        ))

        treino_id = cursor.fetchone()[0]

        conexao.commit()

        print(f"Treino criado! ID: {treino_id}")

    except Exception as erro:
        conexao.rollback()
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()

def adicionar_exercicio():
    treino_id = input("ID do treino: ")
    exercicio_id = input("ID do exercício: ")

    series = input("Séries: ")
    repeticoes = input("Repetições: ")
    carga = input("Carga: ")
    descanso = input("Descanso em segundos: ")

    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO treino_exercicio
                (
                    treino_id,
                    exercicio_id,
                    series,
                    repeticoes,
                    carga,
                    descanso_segundos
                )
            VALUES
                (%s, %s, %s, %s, %s, %s)
        """, (
            treino_id,
            exercicio_id,
            series,
            repeticoes,
            carga,
            descanso
        ))

        conexao.commit()

        print("Exercício adicionado ao treino!")

    except Exception as erro:
        conexao.rollback()
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()

def consultar_treino():
    treino_id = input("ID do treino: ")

    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                t.nome,
                t.objetivo,
                p.nome,
                e.nome,
                e.grupo_muscular,
                te.series,
                te.repeticoes,
                te.carga,
                te.descanso_segundos
            FROM treino t
            JOIN professor p
                ON p.id = t.professor_id
            JOIN treino_exercicio te
                ON te.treino_id = t.id
            JOIN exercicio e
                ON e.id = te.exercicio_id
            WHERE t.id = %s
        """, (treino_id,))

        resultados = cursor.fetchall()

        if not resultados:
            print("Treino não encontrado.")
            return

        primeiro = resultados[0]

        print(f"""
===== TREINO =====

Nome: {primeiro[0]}
Objetivo: {primeiro[1]}
Professor: {primeiro[2]}

===== EXERCÍCIOS =====
""")

        for resultado in resultados:
            print(
                f"Exercício: {resultado[3]}\n"
                f"Grupo: {resultado[4]}\n"
                f"Séries: {resultado[5]}\n"
                f"Repetições: {resultado[6]}\n"
                f"Carga: {resultado[7]}\n"
                f"Descanso: {resultado[8]} segundos\n"
                f"---------------------"
            )

    except Exception as erro:
        print("Erro:", erro)

    finally:
        cursor.close()
        conexao.close()
