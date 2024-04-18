-- Inserciones para la tabla Estados_huevos
INSERT INTO estados_huevos (nombre) VALUES
    ('Estado de huevo 1'),
    ('Estado de huevo 2'),
    ('Estado de huevo 3'),
    ('Estado de huevo 4'),
    ('Estado de huevo 5');

-- Inserciones para la tabla Tipo_lectura
INSERT INTO tipo_lectura (nombre) VALUES
    ('Tipo de lectura 1'),
    ('Tipo de lectura 2'),
    ('Tipo de lectura 3'),
    ('Tipo de lectura 4'),
    ('Tipo de lectura 5');

-- Inserciones para la tabla Tipo_alerta
INSERT INTO tipo_alerta (nombre) VALUES
    ('Tipo de alerta 1'),
    ('Tipo de alerta 2'),
    ('Tipo de alerta 3'),
    ('Tipo de alerta 4'),
    ('Tipo de alerta 5');

-- Inserciones para la tabla Estado_alerta
INSERT INTO estado_alerta (id_estado_alerta, nombre) VALUES
    (1, 'Estado de alerta 1'),
    (2, 'Estado de alerta 2'),
    (3, 'Estado de alerta 3'),
    (4, 'Estado de alerta 4'),
    (5, 'Estado de alerta 5');

-- Inserciones para la tabla Tipo_estado_alerta
INSERT INTO tipo_estado_alerta (estado_alerta_id, tipo_alerta_id) VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5);

-- Inserciones para la tabla Caracteristicas_incubacion
INSERT INTO caracteristicas_incubacion (temperatura_minima, temperatura_maxima, humedad_minima, humedad_maxima, angulo_rotacion, tiempo_rotacion) VALUES
    (20, 30, 40, 60, 90, 120),
    (21, 31, 41, 61, 91, 121),
    (22, 32, 42, 62, 92, 122),
    (23, 33, 43, 63, 93, 123),
    (24, 34, 44, 64, 94, 124);

-- Inserciones para la tabla Tipo_ave
INSERT INTO tipo_ave (imagen, nombre, descripcion, caracteristicas_incubacion_id) VALUES
    ('Imagen 1', 'Nombre de ave 1', 'Descripción de ave 1', 1),
    ('Imagen 2', 'Nombre de ave 2', 'Descripción de ave 2', 2),
    ('Imagen 3', 'Nombre de ave 3', 'Descripción de ave 3', 3),
    ('Imagen 4', 'Nombre de ave 4', 'Descripción de ave 4', 4),
    ('Imagen 5', 'Nombre de ave 5', 'Descripción de ave 5', 5);

-- Inserciones para la tabla Dispositivos
INSERT INTO dispositivos (w, n, caracteristica_incubacion_id) VALUES
    ('W 1', 'N 1', 1),
    ('W 2', 'N 2', 2),
    ('W 3', 'N 3', 3),
    ('W 4', 'N 4', 4),
    ('W 5', 'N 5', 5);

-- Inserciones para la tabla Huevos
INSERT INTO huevos (columna, fila, fecha_hora_puesta, fecha_hora_ingreso, fecha_hora_salida, dispositivo_id, tipo_ave_id) VALUES
    (1, 1, '2024-04-17 08:00:00', '2024-04-17 08:00:00', '2024-04-17 08:00:00', 1, 1),
    (2, 1, '2024-04-17 08:15:00', '2024-04-17 08:15:00', '2024-04-17 08:15:00', 2, 2),
    (3, 1, '2024-04-17 08:30:00', '2024-04-17 08:30:00', '2024-04-17 08:30:00', 3, 3),
    (4, 1, '2024-04-17 08:45:00', '2024-04-17 08:45:00', '2024-04-17 08:45:00', 4, 4),
    (5, 1, '2024-04-17 09:00:00', '2024-04-17 09:00:00', '2024-04-17 09:00:00', 5, 5);

-- Inserciones para la tabla Sensores
INSERT INTO sensores (referencia, descripcion, dispositivo_id) VALUES
    ('sensor 1', 'Descripción 1', 1),
    ('sensor 2', 'Descripción 2', 2),
    ('sensor 3', 'Descripción 3', 3),
    ('sensor 4', 'Descripción 4', 4),
    ('sensor 5', 'Descripción 5', 5);

-- Inserciones para la tabla Lecturas
INSERT INTO lecturas (fecha_hora, valor, sensor_id, tipo_lectura_id) VALUES
    ('2024-04-17 08:00:00', 'Valor de lectura 1', 1, 1),
    ('2024-04-17 08:15:00', 'Valor de lectura 2', 2, 2),
    ('2024-04-17 08:30:00', 'Valor de lectura 3', 3, 3),
    ('2024-04-17 08:45:00', 'Valor de lectura 4', 4, 4),
    ('2024-04-17 09:00:00', 'Valor de lectura 5', 5, 5);

-- Inserciones para la tabla Alertas
INSERT INTO alertas (fecha_alertas, lectura_id, tipo_estado_alerta_id) VALUES
    ('2024-04-17 08:00:00', 1, 1),
    ('2024-04-17 08:15:00', 2, 1),
    ('2024-04-17 08:30:00', 3, 2),
    ('2024-04-17 08:45:00', 4, 2),
    ('2024-04-17 09:00:00', 5, 3);

-- Inserciones para la tabla Revision_huevos
INSERT INTO revision_huevos (fecha_revision, observacion, estado_huevo_id, id_huevo) VALUES
    ('2024-04-17 08:00:00', 'Observación 1', 1, 1),
    ('2024-04-17 08:15:00', 'Observación 2', 2, 2),
    ('2024-04-17 08:30:00', 'Observación 3', 3, 3),
    ('2024-04-17 08:45:00', 'Observación 4', 4, 4),
    ('2024-04-17 09:00:00', 'Observación 5', 5, 5);
