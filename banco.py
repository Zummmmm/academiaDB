import psycopg


def conectar():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="academia",
        user="postgres",
        password="chtnd"
    )