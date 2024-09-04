from flask import Flask, jsonify, request, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hahahahaha'
app.config['MYSQL_DB'] = 'usuariosflask'
mysql = MySQL(app)

# Configuración de la clave secreta para sesiones
app.secret_key = 'mysecretkey'

# Ruta principal
@app.route('/')
def index():
    return 'Hola Mundo'

# Ruta para obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    data = cur.fetchall()
    usuarios = []
    for usuario in data:
        usuarios.append({
            'id': usuario[0],
            'nombre': usuario[1],
            'telefono': usuario[2],
            'email': usuario[3]
        })
    return jsonify(usuarios)

# Ruta para agregar un nuevo usuario
@app.route('/usuario', methods=['POST'])
def add_user():
    nombre = request.json['nombre']
    telefono = request.json['telefono']
    email = request.json['email']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO usuarios (nombre, telefono, email) VALUES (%s, %s, %s)', (nombre, telefono, email))
    mysql.connection.commit()
    return jsonify({'message': 'Usuario agregado satisfactoriamente'})

# Ruta para obtener un usuario específico por ID
@app.route('/usuario/<id>', methods=['GET'])
def get_user(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios WHERE id = %s', (id,))
    data = cur.fetchone()
    if data:
        usuario = {'id': data[0], 'nombre': data[1], 'telefono': data[2], 'email': data[3]}
        return jsonify(usuario)
    return jsonify({'message': 'Usuario no encontrado'})

# Ruta para actualizar un usuario
@app.route('/usuario/<id>', methods=['PUT'])
def update_user(id):
    nombre = request.json['nombre']
    telefono = request.json['telefono']
    email = request.json['email']
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE usuarios
        SET nombre = %s, telefono = %s, email = %s
        WHERE id = %s
    """, (nombre, telefono, email, id))
    mysql.connection.commit()
    return jsonify({'message': 'Usuario actualizado satisfactoriamente'})

# Ruta para eliminar un usuario
@app.route('/usuario/<id>', methods=['DELETE'])
def delete_user(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM usuarios WHERE id = %s', (id,))
    mysql.connection.commit()
    return jsonify({'message': 'Usuario eliminado satisfactoriamente'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
