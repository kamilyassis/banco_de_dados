import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='39*72p16lf'
)

cursor = conexao.cursor()

comando_bd = "CREATE DATABASE biblioteca"

# criar o banco de dados
cursor.execute(comando_bd)

cursor.close()
conexao.close()