from flask import jsonify
from flask import render_template
from flask import request

from main import app
from componentes.modelos import Usuario
from componentes.modelos import Sucursal

from componentes.modelos import Cuenta


@app.route("/api-proyecto/sucursales", methods=['GET'])
def api_cursos():
    sucursales = Sucursal.obtener()
    datos = [sucursal.__dict__ for sucursal in sucursales]
    
    return jsonify(datos)



