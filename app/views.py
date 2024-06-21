from flask import jsonify
from app.models import Producto

def index():
    response = {'message':'Hola mundo API FLASK 🐍'}
    return jsonify(response)

#funcion que busca todo el listado de las peliculas
def get_all_productos():
    productos = Producto.get_all()
    list_productos = [producto.serialize() for producto in productos]
    return jsonify(list_productos)

#funcion que busca una pelicula
def get_movie():
    pass

def create_movie():
    pass

def update_movie():
    pass

def delete_movie():
    pass