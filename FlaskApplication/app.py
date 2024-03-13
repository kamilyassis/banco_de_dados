from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #association between URL and function

def index():
    return render_template('index.html')

#run server

if __name__ == "__main__":
    app.run(debug=True)