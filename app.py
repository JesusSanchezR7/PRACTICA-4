# Importa la clase Flask desde la librería flask
from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta (URL) para la página principal "/"
@app.route('/')
def hola_mundo():
    # Lo que se devuelve aquí se mostrará en el navegador
    return '¡Hola! Mi pipeline de DevOps funciona correctamente.'

# Verifica si este archivo es el programa principal que se está ejecutando
if __name__ == '__main__':
    # Inicia el servidor web
    app.run(host='0.0.0.0', port=5000)

