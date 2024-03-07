from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# init Flask app

app = Flask(__name__)

# Flask server

@app.route('/') # '/' is the home page

def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




