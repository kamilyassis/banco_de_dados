import mysql.connector
import conexao_mysql 

conexao = conexao_mysql.conexao()
cursor = conexao.cursor()


def executar_query(query, valores=None):
    try:
        if valores:
            cursor.execute(query, valores)
        else:
            cursor.execute(query)
        conexao.commit()
    finally:
        cursor.close()
        conexao.close()

# CRUD

# CREATE

def create_livro(titulo,autor, genero): #precisa de num_copias_total
    comando = '''INSERT INTO livros(titulo, autor,genero) VALUES (%s, %s,%s)'''
    executar_query(comando, (titulo,autor, genero))

# READ
    
def read_table(table):
    try:
        cursor = conexao.cursor()
        comando = f'SELECT * FROM biblioteca.{table}'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        return resultado
    finally:
        cursor.close()


def buscar_livro(titulo):

    busca = f'SELECT * FROM livros WHERE titulo = %s'
    cursor.execute(busca, (titulo,))

    #retornar apenas o referente ao id digitado
    resultado = cursor.fetchone()

    if resultado: #verificando se não esta vazio
        print ("O livro está disponível.")
    else:
        print("O livro não está disponível.")

#gerar relatorio
def relatorio_livros():
    comando = ''' SELECT * FROM livros '''
    cursor.execute(comando)

    #retornar todos os elementos
    resultado = cursor.fetchall()

    for linha in resultado:
        print(f'ID: {linha[0]}, Autor: {linha[1]}, Título: {linha[2]}, Gênero: {linha[3]}')

def exibir_livro_por_nome(nome_livro):
    try:
        query = f"SELECT * FROM livros WHERE titulo = '{nome_livro}'"
        cursor.execute(query)
        livro = cursor.fetchone()
        
        if livro:
            print(f"Detalhes do livro '{nome_livro}':")
            print(f"Título: {livro[1]}")
            print(f"Autor: {livro[2]}")
            print(f"Gênero: {livro[4]}")
        else:
            print(f"Livro '{nome_livro}' não encontrado.")
    except mysql.connector.Error as err:
        print(f"Erro ao buscar o livro: {err}")


# UPDATE
def update(table, at_change, val_at_change, at_ref, val_at_ref):
    comando = f'UPDATE {table} SET {at_change} = %s WHERE {at_ref} = %s'
    valores = (val_at_change, val_at_ref)
    executar_query(comando, valores)

# DELETE
    
def delete(tabela, at, val_at):
    comando = f'DELETE FROM {tabela} WHERE {at} = %s '
    executar_query(comando, val_at)  

buscar_livro('Carolina')