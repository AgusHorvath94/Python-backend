from flask import Flask
from app.views import *
from app.database import init_app
from flask_cors import CORS

#inicializacion de aplicacion con flask 

app = Flask (__name__)

init_app(app)
#permitir solicitudes desde cualquier origen
CORS(app)

#registrar la ruta asociada a una vista 

app.route('/',methods=['GET'])(index)
app.route('/api/usuarios/',methods=['GET'])(get_all_usuarios)
app.route('/api/usuarios/',methods=['POST'])(create_usuario)
app.route('/api/usuarios/<int:usuario_id>', methods=['GET'])(get_usuario)
app.route('/api/usuarios/<int:usuario_id>', methods=['PUT'])(update_usuario)
app.route('/api/usuarios/<int:usuario_id>', methods=['DELETE'])(delete_usuario)

if __name__ == "__main__":
    #levanta el servidor de desarrollo flask
    app.run(debug=True)