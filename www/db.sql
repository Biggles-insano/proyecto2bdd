--Nivel de aislamiento
SET default_transaction_isolation TO 'READ COMMITTED';

--Crear tablas
DROP TABLE IF EXISTS bitacora, asientos, salas, peliculas CASCADE;

CREATE TABLE peliculas (
    id_nombre SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE salas (
    id_sala SERIAL PRIMARY KEY,
    id_pelicula INTEGER NOT NULL,
    hora_inicio TIMESTAMP NOT NULL,
    hora_fin TIMESTAMP NOT NULL,
    CONSTRAINT fk_pelicula FOREIGN KEY (id_pelicula) REFERENCES peliculas (id_nombre)
);

CREATE TABLE asientos (
    id_asiento SERIAL PRIMARY KEY,
    id_sala INTEGER NOT NULL,
    estado VARCHAR(20) DEFAULT 'disponible' CHECK (estado IN ('disponible', 'reservado', 'ocupado')),
    CONSTRAINT fk_sala FOREIGN KEY (id_sala) REFERENCES salas (id_sala)
);

CREATE TABLE bitacora (
    id_bitacora SERIAL PRIMARY KEY,
    id_asiento INTEGER,
    accion VARCHAR(50) NOT NULL,
    descripcion TEXT,
    fecha TIMESTAMP DEFAULT NOW(),
    usuario VARCHAR(100),
    CONSTRAINT fk_bitacora_asiento FOREIGN KEY (id_asiento) REFERENCES asientos (id_asiento) ON DELETE SET NULL
);

--Datos iniciales
INSERT INTO peliculas (nombre) VALUES ('Ford vs Ferrari');
INSERT INTO salas (id_pelicula, hora_inicio, hora_fin) VALUES (1, '2025-05-01 14:00:00', '2025-05-01 16:30:00');

--Eliminar asientos
DELETE FROM asientos WHERE id_sala = 1;

--Insertar asientos disponibles
INSERT INTO asientos (id_sala, estado)
SELECT 1, 'disponible' FROM generate_series(1, 25); --Variar parametros segun cuantos asientos se necesiten

ALTER SEQUENCE asientos_id_asiento_seq RESTART WITH 1;
