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
            
            respuesta['mensaje'] = 'Ingreso exitoso!'
            respuesta['status'] = 200
        else:
            respuesta['mensaje'] = 'Verifique los datos enviados.'
            respuesta['status'] = 409
        #cuentas = Cuenta.obtener()  
        #cuentas = [cuenta.__dict__ for cuenta in cuentas]
        
         
        #print(cuentas)
        # if cuenta and ingreso.clave == cuenta.clave :
        #     usuario = Usuario('id_cuenta',cuenta.id)
        #     if not usuario:
        #    respuesta['perfil'] = 0        
        #     else:
        #         respuesta['perfil'] = 1

    return jsonify(respuesta) #devuelve un objeto
        
@app.route("/api-proyecto/guardar-perfil", methods=['POST'])
def crear_usuario():
    
    datos = request.get_json()
    print(f"Datos recibidos: {datos}")
    cuenta = Cuenta.obtener('mail',datos['mail'])
    nuevoUsuario = Usuario(cuenta.id,datos['nombre'],datos['apellido'],datos['dni'],datos['fecha_de_nacimiento'])
    nuevoUsuario.guardar_db()
        
    
    
    return jsonify(datos)

@app.route("/api-proyecto/modificar-perfil", methods=['POST'])
def modificar_usuario():    
    datos = request.get_json()
    print(f"Datos recibidos: {datos}")
    cuenta = Cuenta.obtener('mail',datos['mail'])
    usuario = Usuario.obtener('id_cuenta',cuenta.id)
    del datos['mail']
    #datos['id'] = cuenta.id
    Usuario.modificar(datos)
    return jsonify(datos)

    
    



