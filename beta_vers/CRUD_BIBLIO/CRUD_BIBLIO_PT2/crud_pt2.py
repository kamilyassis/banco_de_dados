import CRUD_BIBLIO_PT2.conexao_mysql as conexao_mysql

conexao = conexao_mysql.conexao()
cursor = conexao.cursor()


# CRUD

# CREATE

def create_livro(id_livro, autor, titulo, num_copias_disp, num_copias_alug):
    comando = '''INSERT INTO livros(id_livro, autor, titulo, genero) VALUES (%s, %s, %s, %s)'''
    cursor.execute(comando, (id_livro, autor, titulo, num_copias_disp, num_copias_alug))
    conexao.commit()


def create_aluno(cpf, nome, curso):
    comando = 'INSERT INTO alunos(cpf,nome,curso) VALUES (%s, %s, %s)'
    cursor.execute(comando, (cpf, nome, curso))
    conexao.commit()


def create_emprestimo(cpf_aluno, id_livro, data_inicio, data_fim):
    comando = 'INSERT INTO emprestimos(cpf_aluno, id_livro, data_inicio, data_fim) VALUES (%s, %s, %s, %s)'
    cursor.execute(comando, (cpf_aluno, id_livro, data_inicio, data_fim))
    conexao.commit()


# READ

def read_table(conexao, table):
    comando = f'SELECT * FROM  {table}'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o bd
    print(resultado)


# UPDATE
def update(conexao, table, at_change, val_at_change, at_ref, val_at_ref):
    comando = f'UPDATE {table} SET {at_change} = %s WHERE {at_ref} = %s'
    valores = (val_at_change, val_at_ref)
    cursor.execute(comando, valores)
    conexao.commit()


# DELETE

def delete(conexao, at, val_at):
    comando = f'DELETE FROM usuarios WHERE {at} = %s '
    cursor.execute(comando, val_at)
    conexao.commit()


cursor.close()
conexao.close()
