import mysql.connector
from mysql.connector import Error

# Função que retorna a conexão
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="inventario"
    )

try:
    # Obtendo a conexão
    conn = get_connection()

    if conn.is_connected():
        print('Conectado com sucesso ao banco de dados.')

        # Criando o cursor a partir da conexão
        cursor = conn.cursor()

        # Aqui você pode adicionar código para interagir com o banco de dados
        # Exemplo: cursor.execute('SEU COMANDO SQL AQUI')

except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")

finally:
    # Fechar o cursor e a conexão, independentemente de ocorrer erro ou não
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()
        print("Conexão com o banco de dados fechada.")
