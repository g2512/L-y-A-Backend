from flask import Flask
from app.database import init_app
from app.views import *

#Crear una instancia de Flask
app = Flask(__name__)

init_app(app)

#asociacion de rutas con vistas
app.route('/',methods=['GET'])(index)
app.route('/api/productos/',methods=['GET'])(get_all_productos)

#Permite separa el codigo que se ejecuta cuando se corre el archivo
if __name__=='__main__':
    app.run(debug=True)