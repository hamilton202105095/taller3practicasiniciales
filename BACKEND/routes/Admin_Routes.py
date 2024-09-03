import os
from flask import Blueprint, request, jsonify
from models.Usuario import Usuario
from models.Producto import Producto
from models.empleado import Empleado
from models.Compra import Compra
import xml.etree.ElementTree as ET


usuarios = []

bp = Blueprint('usuario', __name__, url_prefix='/usuario')


@bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.get_usuarios()
    return jsonify(usuarios)


@bp.route('/usuarios', methods=['POST'])
def post_usuarios():
    data = request.get_json()
    usuario = Usuario(data['nombre'], data['apellido'], data['email'], data['password'])
    usuario.save()
    return jsonify(usuario.serialize())