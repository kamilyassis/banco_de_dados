import conexao_mysql 

conexao = conexao_mysql.conexao()
cursor = conexao.cursor()


comando_bd = "CREATE DATABASE biblioteca"

# criar o banco de dados
cursor.execute(comando_bd)

cursor.close()
conexao.close()