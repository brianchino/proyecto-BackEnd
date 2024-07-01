from flask import jsonify
#from flask import render_template
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
        datos = request.json["datos"]
        print(f"Datos recibidos: {datos}")

        ingreso = Cuenta(datos['mail'],datos['clave'])
        cuentas = Cuenta.obtener()  
        cuentas = [cuenta.__dict__ for cuenta in cuentas]
        
         
        print(cuentas)
        # if cuenta and ingreso.clave == cuenta.clave :
        #     usuario = Usuario('id_cuenta',cuenta.id)
        #     if not usuario:
        #         respuesta['perfil'] = 0        
        #     else:
        #         respuesta['perfil'] = 1

    return jsonify(respuesta) #devuelve un objeto
        
    
    
    



