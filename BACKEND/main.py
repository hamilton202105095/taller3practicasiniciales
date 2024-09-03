from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.Admin_Routes import bp as Admin_Routes 
from routes.Usuario_Routes import bp as Usuario_Routes

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/') 
def holamundo():
    return 'Hola Mundo'


app.register_blueprint(Admin_Routes, url_prefix='/admin')
app.register_blueprint(Usuario_Routes, url_prefix='/usuario')

if __name__ == '__main__':
    app.run(debug=True) 