from base_db.conexion_db import conexion
from base_db.tabla_db import Tabla
from auxiliares.cifrado import encriptar

class Sucursal(Tabla):
    
    tabla = 'sucursal'
    conexion = conexion
    campos = ('id', 'nombre', 'direccion', 'horario')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)        

class Usuario(Tabla):
    
    tabla = 'usuario'
    conexion = conexion
    campos = ('id', 'id_cuenta', 'nombre', 'apellido','dni','fecha_de_nacimiento')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)

class Cuenta(Tabla):
    
    tabla = 'cuenta'
    conexion = conexion
    campos = ('id', 'mail', 'clave')
    
    def __init__(self, *args, de_bbdd=False):
        
        if not de_bbdd:
            cuenta = []
            cuenta.append(args[0])
            cuenta.append(encriptar(args[1]))
            super().crear(tuple(cuenta), de_bbdd)
        else:
            super().crear(args, de_bbdd)