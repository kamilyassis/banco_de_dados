import mysql.connector

def conexao():
    conexao = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '39*72p16lf',
    database = 'biblioteca'
)
    return conexao
