from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL 

app = Flask(__name__)

#conexxion de mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Corrige el nombre de la clave a 'MYSQL_USER'
app.config['MYSQL_PASSWORD'] = 'hahahahaha'
app.config['MYSQL_DB'] = 'usuariosflask'
mysql = MySQL(app)

#configuracion de sesion
app.secret_key = 'mysecretkey'

@app.route('/') 
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    data = cur.fetchall()
    print(data)
    return render_template('index.html', usuarios = data)


@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        print(nombre)
        print(telefono)
        print(email)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (nombre, telefono, email) VALUES (%s, %s, %s)', (nombre, telefono, email))
        mysql.connection.commit()
        flash('Usuario agregado satisfactoriamente')
        return redirect(url_for('Index'))

@app.route('/edit/<id>')
def get_contact(id):
    cur =mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('edit-user.html', usuario = data[0])

@app.route('/update/<id>',methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE usuarios
            SET nombre = %s,
                telefono = %s,
                email = %s
            WHERE id = %s
        """, (nombre, telefono, email, id))
        mysql.connection.commit()
        flash('Usuario actualizado satisfactoriamente')
        return redirect(url_for('Index'))

            


@app.route('/delete/<string:id>')
def delete_user(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM usuarios WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Usuario eliminado satisfactoriamente')
    return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
