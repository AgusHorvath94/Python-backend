from flask import jsonify, request
from app.models import Usuario

def index():
    response = {'message':'Hola Mundo API-REST Flask 🐍'}
    return jsonify(response)

def get_all_usuarios():
    usuarios = Usuario.get_all()
    usuarios_serializados = [usuario.serialize() for usuario in usuarios]
    return jsonify(usuarios_serializados)


def get_usuario(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    if not usuario:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    return jsonify(usuario.serialize())

def create_usuario():
    #Obtengo los datos enviados en formato json - convierte en un diccionaro python
    data = request.json
    #PROCESO DE VALIDACION
    #if(data['title']==''):
    #    return jsonify({'message':'El campo titulo es obligatorio'}) 
    new_usuario = Usuario(None,data["nombre"],data["apellido"],data["email"],data["contraseña"],data["nacimiento"])
    new_usuario.save()
    response = {'message':'Usuario creado con exito'}
    return jsonify(response), 201

def update_usuario(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    if not usuario:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    data = request.json
    usuario.nombre = data['nombre']
    usuario.apellido = data['apellido']
    usuario.email = data['email']
    usuario.contraseña = data['contraseña']
    usuario.nacimiento = data['nacimiento']
    usuario.save()
    return jsonify({'message': 'Usuario actualizado con exito'})

def delete_usuario(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    if not usuario:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    usuario.delete()
    return jsonify({'message': 'Usuario eliminado con exito'})

