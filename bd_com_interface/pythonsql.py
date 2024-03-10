import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)



conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senharoot!26',
    db='banco_p1'
    # database='banco_p1;'
)

@app.route('/')

@app.route('/search')
def search():
    q = request.args.get('q')
    print(q)

    if q:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM livro WHERE nome LIKE %s", (f'%{q}%',))
        results = cursor.fetchall()
        return render_template('search.html', data=results)
        
# @app.route('/search', methods=['GET', 'POST'])

# def exibir_por_nome():

#     cursor = conexao.cursor(dictionary=True)
#     output = cursor.execute("SELECT  FROM livro ORDER BY nome")

def exibir():
    cursor = conexao.cursor(dictionary=True)
    print("Conexão com o banco de dados realizada com sucesso!")
    cursor.execute("SELECT * FROM livro")
    rows = cursor.fetchall()
    
    return render_template('table.html', data=rows)


if __name__ == '__main__':
    app.run(debug=True)


    