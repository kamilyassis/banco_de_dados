import mysql.connector
from flask import Flask, render_template


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
    cursor = conexao.cursor()
    print("Conexão com o banco de dados realizada com sucesso!")

    cursor.execute("SELECT * FROM livro")
    rows = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template('table.html', data=rows)

if __name__ == '__main__':
    app.run(debug=True)