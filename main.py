from alunos import (
    cadastrar_aluno,
    listar_alunos,
    buscar_aluno,
    excluir_aluno
)

from planos import (
    cadastrar_plano,
    listar_planos,
    excluir_plano
)

from professores import (
    cadastrar_professor,
    listar_professores
)

from exercicios import (
    cadastrar_exercicio,
    listar_exercicios
)

from matriculas import (
    cadastrar_matricula,
    listar_matriculas,
    cancelar_matricula
)

from treinos import (
    criar_treino,
    adicionar_exercicio,
    consultar_treino
)


def menu():
    while True:

        print("""
=============================
       ACADEMIA
=============================

1  - Cadastrar aluno
2  - Listar alunos
3  - Buscar aluno
4  - Excluir aluno

5  - Cadastrar plano
6  - Listar planos
7  - Excluir plano

8  - Cadastrar professor
9  - Listar professores

10 - Cadastrar exercício
11 - Listar exercícios

12 - Criar matrícula
13 - Listar matrículas
14 - Cancelar matrícula

15 - Criar treino
16 - Adicionar exercício ao treino
17 - Consultar treino

0  - Sair

=============================
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            buscar_aluno()

        elif opcao == "4":
            excluir_aluno()

        elif opcao == "5":
            cadastrar_plano()

        elif opcao == "6":
            listar_planos()

        elif opcao == "7":
            excluir_plano()

        elif opcao == "8":
            cadastrar_professor()

        elif opcao == "9":
            listar_professores()

        elif opcao == "10":
            cadastrar_exercicio()

        elif opcao == "11":
            listar_exercicios()

        elif opcao == "12":
            cadastrar_matricula()

        elif opcao == "13":
            listar_matriculas()

        elif opcao == "14":
            cancelar_matricula()

        elif opcao == "15":
            criar_treino()

        elif opcao == "16":
            adicionar_exercicio()

        elif opcao == "17":
            consultar_treino()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


menu()
