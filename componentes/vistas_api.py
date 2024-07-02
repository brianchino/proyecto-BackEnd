from flask import jsonify
from flask import render_template
from flask import request

from app import app
from componentes.modelos import Usuario
from componentes.modelos import Sucursal
from componentes.modelos import Cuenta


@app.route("/api-proyecto/sucursales", methods=['GET'])
def obtener_Sucursales():
    
    sucursales = Sucursal.obtener()
    datos = [sucursal.__dict__ for sucursal in sucursales]
    
    return jsonify(datos)


@app.route("/api-proyecto/cuenta", methods=['POST'])
def crear_cuenta():
    if request.method == 'POST':
        datos = request.get_json()
        print(f"Datos recibidos: {datos}")

        nuevaCuenta = Cuenta(datos['mail'],datos['clave'])
        nuevaCuenta.guardar_db()
        
    
    
    return jsonify(datos)


@app.route("/api-proyecto/ingreso", methods=['POST'])
def validar_cuenta():
    if request.method == 'POST':
        respuesta = {}
        datos = request.get_json()
        print(f"Datos recibidos: {datos}")

        ingreso = Cuenta(datos['mail'],datos['clave'])
        cuenta = Cuenta.obtener('mail', datos['mail'])
        if cuenta and ingreso.clave == cuenta.clave:
            usuario = Usuario.obtener('id_cuenta', cuenta.id)

            if not usuario:
                respuesta['perfil'] = 0
            else:
                respuesta['perfil'] = 1
                respuesta['nombre'] =usuario.nombre
                respuesta['apellido'] =usuario.apellido
                respuesta['dni'] =usuario.dni
                respuesta['fecha_de_nacimiento'] = usuario.fecha_de_nacimiento
            
            respuesta['mensaje'] = 'Ingreso exitoso!'
            respuesta['status'] = 200
        else:
            respuesta['mensaje'] = 'Verifique los datos enviados.'
            respuesta['status'] = 409

    return jsonify(respuesta) #devuelve un objeto
        
@app.route("/api-proyecto/guardar-perfil", methods=['POST'])
def crear_usuario():
    if request.method == 'POST':
        datos = request.get_json()
        print(f"Datos recibidos: {datos}")
        cuenta = Cuenta.obtener('mail',datos['mail'])
        nuevoUsuario = Usuario(cuenta.id,datos['nombre'],datos['apellido'],datos['dni'],datos['fecha_de_nacimiento'])
        nuevoUsuario.guardar_db()
    return jsonify(datos)

@app.route("/api-proyecto/modificar-perfil", methods=['POST'])
def modificar_usuario():
    if request.method == 'POST':    
        datos = request.get_json()
        print(f"Datos recibidos: {datos}")

        # Obtener cuenta por mail
        cuenta = Cuenta.obtener('mail', datos['mail'])
        if not cuenta:
            return jsonify({'error': 'Cuenta no encontrada'}), 404

        # Obtener usuario por id_cuenta
        usuario = Usuario.obtener('id_cuenta', cuenta.id)
        if not usuario:
            return jsonify({'error': 'Usuario no encontrado'}), 404

        # Eliminar 'mail' de los datos y agregar 'id' del usuario
        del datos['mail']
        datos['id'] = usuario.id

        resultado = Usuario.modificar(datos)
    return jsonify(datos)


    
@app.route("/api-proyecto/eliminar-cuenta", methods=['DELETE'])
def eliminar_cuenta():
   
    if request.method == 'DELETE':
        datos = request.get_json()
        cuenta = Cuenta.obtener('mail',datos['mail'])
        usuario = Usuario.obtener('id_cuenta',cuenta.id)
        eliminar_usuario = Usuario.eliminar(usuario.id)
        eliminar_cuenta = Cuenta.eliminar(cuenta.id)
        if eliminar_cuenta == eliminar_usuario:
            respuesta = {'mensaje': eliminar_usuario}
        else:
            respuesta = {'mensaje': 'Algo salió mal!'}
    else:
        respuesta ={'mensaje': 'no se recibieron datos.'}
    return jsonify(respuesta)
    



