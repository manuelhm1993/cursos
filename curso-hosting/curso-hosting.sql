CREATE TABLE Clientes (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre     VARCHAR(50),
    apellido   VARCHAR(50),
    email      VARCHAR(100),
    telefono   VARCHAR(20)
);

CREATE TABLE Empleados (
    empleado_id  INT PRIMARY KEY AUTO_INCREMENT,
    nombre       VARCHAR(50),
    apellido     VARCHAR(50),
    especialidad VARCHAR(50)
);

CREATE TABLE Servicios (
    servicio_id INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(100),
    duracion    INT,
    precio      DECIMAL(10,2)
);

CREATE TABLE Turnos (
    turno_id          INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id        INT,
    empleado_id       INT,
    servicio_id       INT,
    fecha_hora_inicio DATETIME,
    estado            VARCHAR(20),
    FOREIGN KEY (cliente_id)  REFERENCES Clientes(cliente_id),
    FOREIGN KEY (empleado_id) REFERENCES Empleados(empleado_id),
    FOREIGN KEY (servicio_id) REFERENCES Servicios(servicio_id)
);