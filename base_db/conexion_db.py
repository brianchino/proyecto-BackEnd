import mysql.connector

config_dev = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'python_backend',
}

config_prod = {
  'user': 'chinoBrian',
  'password': 'francisco50',
  'host': 'chinoBrian.mysql.pythonanywhere-services.com',
  'database': 'chinoBrian$default',
}

conexion = mysql.connector.connect(**config_dev)     