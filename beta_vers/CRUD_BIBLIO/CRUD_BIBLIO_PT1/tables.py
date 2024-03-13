import mysql.connector
import conexao_mysql 

conexao = conexao_mysql.conexao()
cursor = conexao.cursor()

comando_tabela_livros = '''
CREATE TABLE livros (
    id_livro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    genero VARCHAR(100) NOT NULL
)

'''

def alterar_tabela(tabela, old_name, new_name, type):
    comando_alterar_coluna = f'''ALTER TABLE {tabela}
    CHANGE COLUMN {old_name} {new_name} {type}'''
    cursor.execute(comando_alterar_coluna)
    conexao.commit()

def criar_tabela(comando):
    try:
        cursor.execute(comando)
        conexao.commit()
        print("Tabela criada com sucesso!")
    except mysql.connector.Error as err: 
        if err.errno == mysql.connector.errorcode.ER_TABLE_EXISTS_ERROR:
            print('A tabela já existe')
        else:
            print(err.msg)

def dropar_tabela(nome_tabela):
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {nome_tabela}")
        conexao.commit()
        print(f"Tabela {nome_tabela} dropada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao dropar a tabela: {err}")
#testes
criar_tabela(comando_tabela_livros)
#dropar_tabela('livros')


cursor.close()
conexao.close()
