import CRUD_BIBLIO_PT1.conexao_mysql as conexao_mysql

conexao = conexao_mysql.conexao()
cursor = conexao.cursor()

comando_tabela_livros = '''
CREATE TABLE livros (
    id_livro INT AUTO_INCREMENT PRIMARY KEY,
    autor VARCHAR(100) NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    num_copias_total INT NOT NULL,
    num_copias_disp INT NOT NULL,
    num_copias_alug INT NOT NULL
)

'''

comando_tabela_alunos = '''
CREATE TABLE alunos (
    cpf INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    curso VARCHAR(100) NOT NULL
)

'''

comando_tabela_emprestimos = '''
CREATE TABLE emprestimos (
    cpf_aluno INT,
    id_livro INT,
    FOREIGN KEY (id_livro) REFERENCES livros(id_livro),
    FOREIGN KEY (cpf_aluno) REFERENCES alunos(cpf),
    data_inicio DATETIME NOT NULL,
    data_fim DATETIME NOT NULL
)'''

def alterar_tabela(tabela, old_name, new_name, type):
    comando_alterar_coluna = f'''ALTER TABLE {tabela}
    CHANGE COLUMN {old_name} {new_name} {type}'''
    cursor.execute(comando_alterar_coluna)
    conexao.commit()

def criar_tabela(comando):
    cursor.execute(comando)
    conexao.commit()

#criar_tabela(comando_tabela_livros)
#criar_tabela(comando_tabela_alunos)
#criar_tabela(comando_tabela_emprestimos)

cursor.close()
conexao.close()