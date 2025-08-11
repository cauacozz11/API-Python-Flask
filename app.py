# Importação
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

# Modelagem

class Produto(db.Model):
    id = db.Column(db.Integer, )

# Definir uma rota raiz (página inicial) e a fnção que será executada ao requisitar
@app.route('/teste')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)
    
