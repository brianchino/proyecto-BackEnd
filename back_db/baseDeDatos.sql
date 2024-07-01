CREATE DATABASE python_backend;

USE python_backend;
CREATE TABLE sucursal (
id INT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(30),
direccion VARCHAR(60),
horario VARCHAR(60),
PRIMARY KEY(id)
);
CREATE TABLE cuenta (
id INT NOT NULL AUTO_INCREMENT,
mail VARCHAR(60),
clave VARCHAR(60),
PRIMARY KEY(id)
);

CREATE TABLE usuario (
id INT NOT NULL AUTO_INCREMENT,
id_cuenta INT,
nombre VARCHAR(30),
apellido VARCHAR(30),
dni INT,
fecha_de_nacimiento DATE,
PRIMARY KEY(id)
);

ALTER TABLE usuario
	ADD FOREIGN KEY (id_cuenta) REFERENCES cuenta(id)
		ON UPDATE NO ACTION
		ON DELETE NO ACTION;

INSERT INTO sucursal (nombre,direccion,horario) VALUES
	('Samco Palermo','Avenida Santa Fe','Lunes a Sabado de 10 a 18 hs.'),
    ('Samco Caballito','Avenida Rividavia 4736','Lunes a Sabado de 10 a 18 hs.'),
    ('Samco Flores','Avenida Rividavia 7392','Lunes a Viernes de 9 a 18 hs.'),
    ('Samco Liniers','Avenida Rividavia 10701','Lunes a Viernes de 9 a 16 hs.');
    
SELECT * FROM sucursal;
SELECT * FROM usuario;
SELECT * FROM cuenta;




