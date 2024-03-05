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

def create_livro(autor, titulo, num_copias_total, num_copias_disp, num_copias_alug): #precisa de num_copias_total
    comando = '''INSERT INTO livros(autor, titulo, num_copias_disp,
    num_copias_alug) VALUES (%s, %s,%s, %s, %s)'''
    executar_query(comando, (autor, titulo,num_copias_total, num_copias_disp, num_copias_alug))
    

def create_aluno(cpf,nome,curso):
    comando = 'INSERT INTO alunos(cpf,nome,curso) VALUES (%s, %s, %s)'
    executar_query(comando, (cpf,nome,curso))

def create_emprestimo(cpf_aluno, id_livro, data_inicio, data_fim):
    comando = 'INSERT INTO emprestimos(cpf_aluno, id_livro, data_inicio, data_fim) VALUES (%s, %s, %s, %s)'
    executar_query(comando, (cpf_aluno, id_livro, data_inicio, data_fim))

# READ
    
def read_table(table):
    comando = f'SELECT * FROM  {table}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado


# UPDATE
def update(table, at_change, val_at_change, at_ref, val_at_ref):
    comando = f'UPDATE {table} SET {at_change} = %s WHERE {at_ref} = %s'
    valores = (val_at_change, val_at_ref)
    executar_query(comando, valores)

# DELETE
    
def delete(tabela, at, val_at):
    comando = f'DELETE FROM {tabela} WHERE {at} = %s '
    executar_query(comando, val_at)  
