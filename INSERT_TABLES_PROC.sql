-- Insercion para la tabla caracteristicas_incubacion
INSERT INTO caracteristicas_incubacion (temperatura_minima, temperatura_maxima, humedad_minima, humedad_maxima, angulo_rotacion, tiempo_rotacion) VALUES
    (37, 38, 45, 60, 45, 120),
    (37, 38, 60, 70, 45, 120)

-- Inserciones para la tabla Tipo_ave
INSERT INTO tipo_ave (imagen, nombre, descripcion, caracteristicas_incubacion_id) VALUES
    ('Imagen 1', 'Gallina', 'La gallina doméstica (Gallus gallus domesticus), descendiente del gallo salvaje del sudeste asiático, es una ave social y omnívora conocida por su alta producción de huevos y carne. Estas aves, que pesan entre 1.5 y 3 kg y presentan un plumaje variado, comienzan a poner huevos a los 5-7 meses de edad, produciendo entre 200 y 300 huevos anuales. Viven en bandadas con una jerarquía social definida y requieren una dieta balanceada, incluyendo suplementos de calcio para cáscaras fuertes. Las razas populares como la Leghorn y Rhode Island Red son apreciadas por su productividad y temperamento.', 1),

-- Inserciones para la tabla Dispositivos
INSERT INTO dispositivos (w, n, caracteristica_incubacion_id) VALUES
    ('Incubadora W', 'Incubadora N', 1),

-- Inserciones para la tabla Sensores
INSERT INTO sensores (referencia, descripcion, dispositivo_id) VALUES
    ('DTH11', 'Temperatura y Humedad', 1),

-- Inserciones para la tabla Tipo_lectura
INSERT INTO tipo_lectura (nombre) VALUES
    ('Temperatura'),
    ('Humedad')
