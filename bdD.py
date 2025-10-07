-- ======================
-- EMPLEADOS
-- ======================
CREATE TABLE Empleado (
    ci TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    telefono TEXT,
    salario REAL,
    cargo TEXT,
    sexo CHAR(1),
    estado TEXT,
    turno TEXT,
    fechaIngreso DATE,
    fechaSalida DATE,
    id_farmacia INTEGER,
    FOREIGN KEY (id_farmacia) REFERENCES Farmacia(id_farmacia) ON DELETE SET NULL
);

CREATE TABLE Farmaceutico (
    ci TEXT PRIMARY KEY,
    matricula TEXT,
    especialidad TEXT,
    FOREIGN KEY (ci) REFERENCES Empleado(ci) ON DELETE CASCADE
);

CREATE TABLE Administrador (
    ci TEXT PRIMARY KEY,
    FOREIGN KEY (ci) REFERENCES Empleado(ci) ON DELETE CASCADE
);

CREATE TABLE EncargadoInventario (
    ci TEXT PRIMARY KEY,
    FOREIGN KEY (ci) REFERENCES Empleado(ci) ON DELETE CASCADE
);

-- ======================
-- USUARIOS Y REPORTES
-- ======================
CREATE TABLE Usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    fecha_creacion DATE,
    ci_empleado TEXT,
    FOREIGN KEY (ci_empleado) REFERENCES Empleado(ci) ON DELETE SET NULL
);

CREATE TABLE Reporte (
    id_reporte INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_reporte DATE,
    tipo TEXT,
    ci_empleado TEXT,
    FOREIGN KEY (ci_empleado) REFERENCES Empleado(ci) ON DELETE CASCADE
);

-- ======================
-- CLIENTES
-- ======================
CREATE TABLE Cliente (
    ci_cliente TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    telefono TEXT,
    direccion TEXT,
    ci_empleado TEXT,
    FOREIGN KEY (ci_empleado) REFERENCES Empleado(ci) ON DELETE SET NULL
);

-- ======================
-- SUCURSAL Y FARMACIA
-- ======================
CREATE TABLE Sucursal (
    id_sucursal INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    departamento TEXT,
    nit TEXT,
    email TEXT,
    direccion TEXT,
    horario TEXT,
    fecha_registro DATE
);

CREATE TABLE Farmacia (
    id_farmacia INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_farmacia TEXT,
    razonLegal TEXT,
    id_sucursal INTEGER,
    FOREIGN KEY (id_sucursal) REFERENCES Sucursal(id_sucursal) ON DELETE CASCADE
);

-- ======================
-- INVENTARIO, PRODUCTO Y ALERTA
-- ======================
-- ======================
-- ALMACEN
-- ======================
CREATE TABLE Almacen (
    id_almacen INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria TEXT,
    ubicacion TEXT,
    fecha_ingreso DATE,
    fecha_salida DATE
);

-- Relación de composición con Inventario
-- Cada Inventario pertenece a un Almacen, si se elimina el Almacen se elimina también su Inventario
CREATE TABLE Inventario (
    id_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
    cantidad INT,
    estado TEXT,
    fecha_actualizacion DATE,
    stock_minimo INT,
    ci_encargado TEXT NOT NULL,
    id_almacen INTEGER NOT NULL,
    FOREIGN KEY (ci_encargado) REFERENCES EncargadoInventario(ci) ON DELETE CASCADE,
    FOREIGN KEY (id_almacen) REFERENCES Almacen(id_almacen) ON DELETE CASCADE
);

CREATE TABLE Producto (
    codigoBarra TEXT PRIMARY KEY,
    nombre TEXT,
    descripcion TEXT,
    estado TEXT,
    precioUnitario REAL,
    stock INT,
    fechaVencimiento DATE,
    iva TEXT,
    id_inventario INTEGER NOT NULL,
    ci_cliente TEXT,
    FOREIGN KEY (id_inventario) REFERENCES Inventario(id_inventario) ON DELETE CASCADE,
    FOREIGN KEY (ci_cliente) REFERENCES Cliente(ci_cliente) ON DELETE SET NULL
);

CREATE TABLE Alerta (
    id_alerta INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT,
    descripcion TEXT,
    fecha_alerta DATE,
    estado TEXT,
    id_inventario INTEGER,
    FOREIGN KEY (id_inventario) REFERENCES Inventario(id_inventario) ON DELETE CASCADE
);

CREATE TABLE Proveedor (
    id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    telefono TEXT,
    email TEXT,
    direccion TEXT,
    estado TEXT,
    fecha_registro DATE,
    id_inventario INTEGER,
    FOREIGN KEY (id_inventario) REFERENCES Inventario(id_inventario) ON DELETE SET NULL
);

-- ======================
-- VENTAS Y DETALLES
-- ======================
CREATE TABLE Venta (
    id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
    factura BOOLEAN,
    fecha DATE,
    total REAL,
    estado TEXT,
    ci_cliente TEXT,
    FOREIGN KEY (ci_cliente) REFERENCES Cliente(ci_cliente) ON DELETE CASCADE
);

CREATE TABLE DetalleVenta (
    id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
    cantidad INT,
    precioUnitario REAL,
    subtotal REAL,
    metodoPago TEXT,
    descuento BOOLEAN,
    id_venta INTEGER NOT NULL,
    FOREIGN KEY (id_venta) REFERENCES Venta(id_venta) ON DELETE CASCADE
);

-- ======================
-- RECETAS Y DETALLES
-- ======================
CREATE TABLE Receta (
    id_receta TEXT PRIMARY KEY,
    fecha_emision DATE,
    matricula_medico TEXT,
    medicamento TEXT,
    cantidad INT,
    ci_cliente TEXT,
    FOREIGN KEY (ci_cliente) REFERENCES Cliente(ci_cliente) ON DELETE CASCADE
);

CREATE TABLE DetalleReceta (
    id_detalle_receta INTEGER PRIMARY KEY AUTOINCREMENT,
    dosis TEXT,
    frecuencia TEXT,
    duracion TEXT,
    instrucciones TEXT,
    id_receta TEXT NOT NULL,
    FOREIGN KEY (id_receta) REFERENCES Receta(id_receta) ON DELETE CASCADE
);
