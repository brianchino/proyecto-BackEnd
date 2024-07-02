import mysql.connector

config_dev = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'python_backend',
}

config_prod = {
  'user': 'chinobrian',
  'password': 'francisco50',
  'host': 'chinobrian.mysql.pythonanywhere-services.com',
  'database': 'chinobrian$default',
}

conexion = mysql.connector.connect(**config_prod)     