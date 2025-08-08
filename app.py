# Importação
from flask import Flask

app = Flask(__name__)

# Definir uma rota raiz (página inicial) e a fnção que será executada ao requisitar
@app.route('/')
def hello_word():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)
    
