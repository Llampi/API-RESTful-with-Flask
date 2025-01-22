from flask import Blueprint, jsonify, request

usuarios_blueprint = Blueprint('usuarios', __name__)

usuarios = [
    {'id': 1, 'nombre': 'Juan', 'apellido': 'Pérez'},
    {'id': 2, 'nombre': 'María', 'apellido': 'García'}
]

@usuarios_blueprint.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({'usuarios': usuarios})



@usuarios_blueprint.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = [usuario for usuario in usuarios if usuario['id'] == id]
    if len(usuario) == 0:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404
    return jsonify({'usuario': usuario[0]})

@usuarios_blueprint.route('/usuarios', methods=['POST'])
def crear_usuario():
    nuevo_usuario = request.get_json()
    usuarios.append(nuevo_usuario)
    return jsonify({'mensaje': 'Usuario creado correctamente'}), 201

@usuarios_blueprint.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario_a_actualizar = [usuario for usuario in usuarios if usuario['id'] == id]
    if len(usuario_a_actualizar) == 0:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404
    usuario_a_actualizar[0].update(request.get_json())
    return jsonify({'mensaje': 'Usuario actualizado correctamente'})

@usuarios_blueprint.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario_a_eliminar = [usuario for usuario in usuarios if usuario['id'] == id]
    if len(usuario_a_eliminar) == 0:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404
    usuarios.remove(usuario_a_eliminar[0])
    return jsonify({'mensaje': 'Usuario eliminado correctamente'})
