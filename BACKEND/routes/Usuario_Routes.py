from flask import Blueprint, request, jsonify
from models.Usuario import Usuario
from routes.Admin_Routes import bp as Admin_Routes
import xml.etree.ElementTree as ET
bp = Blueprint('user_routes', __name__, url_prefix='/user')
from models.Producto import Producto
import os


userLogged = {
    'id': '',
    'password': '',
    'nombre': '',
    'apellido': '',
}


@bp.route('/login', methods=['POST'])
def login():
    global userLogged
    usuarios = Usuario.get_usuarios()
    if request.method == 'POST':
        # ver si el usuario existe
        id = request.json['id']
        password = request.json['password']

        if id == '' or password == '':
            return jsonify({'message': 'empty fields'}),
    
        if id == 'ADMIN' and password == '12345':
            userLogged = {
                'id': 'admin',
                'password': '1234',
                'nombre': 'admin',
                'apellido': 'admin',
            }
            return jsonify({
                    "message": "success",
                    "role": "admin"
                })
        for usuario in usuarios:
            if usuario.id == id and usuario.password == password:
                userLogged = usuario.__dict__()
                return jsonify({
                        "message": "success",
                        "role": "user" 
                    })        
        
        return jsonify({'message': 'el id o la contraseña son incorrectos'}), 404
    
@bp.route('/userLogged', methods=['GET'])
def getUserLogged():
    return jsonify(userLogged)

@bp.route('/logout', methods=['GET'])
def logout():
    global userLogged
    userLogged = {
        'id': '',
        'password': '',
        'nombre': '',
        'apellido': ''
    }
    return jsonify({'message': 'success'})


@bp.route('/comprar', methods=['POST'])
def comprar():
    global userLogged
    if request.method == 'POST':
        data = request.json
        userLogged['carrito'] = data
        return jsonify({'message': 'success'})
    return jsonify({'message': 'error'})
