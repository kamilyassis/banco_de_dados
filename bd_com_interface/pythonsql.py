import mysql.connector
from flask import Flask, render_template, jsonify, request




app = Flask(__name__)

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senharoot!26',
    db='banco_p1'
    # database='banco_p1;'
)

@app.route('/')


def exibir():
    cursor = conexao.cursor(dictionary=True)
    print("Conexão com o banco de dados realizada com sucesso!")
    cursor.execute("SELECT * FROM livro")
    rows = cursor.fetchall()
    
    return render_template('table.html', data=rows)
        
@app.route('/api/search', methods=['GET'])

def search():
    try:
        nome_livro = request.args.get('nome_livro')
        cursor = conexao.cursor(dictionary=True)
        cursor.execute('SELECT * FROM livro WHERE titulo = %s', (nome_livro,))
        livro = cursor.fetchall()

        if livro:
            return render_template('search.html', data=livro)
        else:
            print(f"Livro '{nome_livro}' não encontrado.")
    except mysql.connector.Error as err:
        print(f"Erro ao buscar o livro: {err}")





if __name__ == '__main__':
    app.run(debug=True)


    