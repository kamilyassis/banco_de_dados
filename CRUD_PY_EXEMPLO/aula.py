import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='39*72p16lf',
    database='teste_1_crud',
)

#executar comandos da conexao
cursor = conexao.cursor()

# CRUD

# CREATE

'''nome = "jup"
email = "jup@email.com"
date = "1999-05-01"'''

#date = datetime.strptime("01-05-2002", "%d-%m-%Y").strftime("%Y-%m-%d")  # Formatar a data corretamente

#(%s) -> placeholder
'''comando = 'INSERT INTO usuarios(nome,email,date) VALUES (%s, %s, %s)'
cursor.execute(comando, (nome,email,date))
conexao.commit() #edita o bd
'''
# READ

def read_db(conexao):
    comando = f'SELECT * FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall() #ler o bd
    print(resultado)

# UPDATE
nome = "jup"
email = "jup@25.com"

def update_db(conexao):
    comando = f'UPDATE usuarios SET email = "{email}" WHERE nome = "{nome}" '
    cursor.execute(comando) 
    conexao.commit() 

def delete_empty_rows(conexao):
    comando = f'DELETE FROM usuarios WHERE nome = "" '
    cursor.execute(comando) 
    conexao.commit() 


# Fechar o cursor e a conexão
cursor.close()
conexao.close()