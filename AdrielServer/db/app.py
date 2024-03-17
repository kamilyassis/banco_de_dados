from flask import Flask, render_template, request, redirect, url_for,jsonify
import pymysql
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '39*72p16lf'
app.config['MYSQL_DB'] = 'biblioteca'


conexao = pymysql.connect(host=app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'],
                password=app.config['MYSQL_PASSWORD'], db=app.config['MYSQL_DB'])
cursor = conexao.cursor()

@app.route('/')


def exibir():
    cursor = conexao.cursor()
    print("Conexão com o banco de dados realizada com sucesso!")
    cursor.execute("SELECT * FROM livros")
    rows = cursor.fetchall()
    
    return render_template('table.html', data=rows)
        
@app.route('/api/search', methods=['GET'])

def search():
    try:
        nome_livro = request.args.get('nome_livro')
        cursor = conexao.cursor(dictionary=True)
        cursor.execute('SELECT * FROM livros WHERE titulo = %s', (nome_livro,))
        livro = cursor.fetchall()

        if livro:
            return render_template('search.html', data=livro)
        else:
            print(f"Livro '{nome_livro}' não encontrado.")
    except pymysql.connect.Error as err:
        print(f"Erro ao buscar o livro: {err}")

@app.route('/api/delete', methods=['POST'])

def delete():
    try:
        data = request.json
        id_deletado = data['id_deletado']
        cursor = conexao.cursor() 
        cursor.execute('DELETE FROM livros WHERE id_livro = %s', (id_deletado,))
        conexao.commit()
        return jsonify(success=True)
    except pymysql.connect.Error as err:
        print(f"Erro ao deletar o livro: {err}")
        return jsonify(success=False, error=str(err))

@app.route('/api/update/<int:id_livro>', methods=['POST'])
def update_livro(id_livro):
    autor = request.form['autor']
    titulo = request.form['titulo']
    genero = request.form['genero']
    
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute(
            "UPDATE livros SET autor = %s, titulo = %s, genero = %s WHERE id_livro = %s",
            (autor, titulo, genero, id_livro)
        )
        conexao.commit()
        cursor.close()
        conexao.close()
        
        # Retornar uma resposta de sucesso
        return jsonify({'success': True, 'message': 'Livro atualizado com sucesso'})
    except pymysql.connect.Error as err:
        print(f"Erro ao atualizar o livro: {err}")
        cursor.close()
        # Retornar uma resposta de erro
        return jsonify({'success': False, 'message': 'Erro ao atualizar o livro'})

if __name__ == '__main__':
    app.run(debug=True)
