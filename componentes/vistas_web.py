from flask import render_template
from app import app
from componentes.modelos import Sucursal
from componentes.modelos import Usuario
from componentes.modelos import Cuenta

@app.route('/')
def inicio():
    return render_template('./inicio.html')

@app.route('/sucursales')
def mostrar_sucursales():
    sucursales = Sucursal.obtener()
    return render_template('./sucursales.html',sucursales=sucursales)


@app.route('/cuentas')
def mostrar_cuentas():
    cuentas = Cuenta.obtener()
    return render_template('cuentas.html',cuentas=cuentas)

@app.route('/usuarios')
def mostrar_usuarios():
    usuarios = Usuario.obtener()
    return render_template('./usuarios.html',usuarios=usuarios)