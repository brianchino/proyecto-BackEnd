from flask import jsonify
#from flask import render_template
#from flask import request

from app import app
from componentes.modelos import Usuario
from componentes.modelos import Sucursal

from componentes.modelos import Cuenta

#ruta de acceso para consultar sucursales
@app.route("/api-proyecto/sucursales", methods=['GET'])
def obtener_Sucursales():
    
    sucursales = Sucursal.obtener()
    datos = [sucursal.__dict__ for sucursal in sucursales]
    
    return jsonify(datos)

# ruta de acceso para consultar cuentas

@app.route("/api-proyecto/cuentas", methods=['GET'])
def obtener_Cuentas():
    
    cuentas = Cuenta.obtener()
    datos = [cuenta.__dict__ for cuenta in cuentas]
    
    return jsonify(datos)

#rura de acceso para consultar usuarios

@app.route("/api-proyecto/usuarios", methods=['GET'])
def obtener_Usuarios():
    
    usuarios = Usuario.obtener()
    datos = [usuario.__dict__ for usuario in usuarios]
    
    return jsonify(datos)

