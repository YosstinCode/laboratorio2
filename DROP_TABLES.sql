-- Eliminar la tabla Alertas y todas las relaciones asociadas
DROP TABLE IF EXISTS alertas CASCADE;

-- Eliminar la tabla Revision_huevos y todas las relaciones asociadas
DROP TABLE IF EXISTS revision_huevos CASCADE;

-- Eliminar la tabla Huevos y todas las relaciones asociadas
DROP TABLE IF EXISTS huevos CASCADE;

-- Eliminar la tabla Dispositivos y todas las relaciones asociadas
DROP TABLE IF EXISTS dispositivos CASCADE;

-- Eliminar la tabla Sensores y todas las relaciones asociadas
DROP TABLE IF EXISTS sensores CASCADE;

-- Eliminar la tabla Lecturas y todas las relaciones asociadas
DROP TABLE IF EXISTS lecturas CASCADE;

-- Eliminar la tabla Tipo_estado_alerta y todas las relaciones asociadas
DROP TABLE IF EXISTS tipo_estado_alerta CASCADE;

-- Eliminar la tabla Tipo_lectura y todas las relaciones asociadas
DROP TABLE IF EXISTS tipo_lectura CASCADE;

-- Eliminar la tabla Tipo_alerta y todas las relaciones asociadas
DROP TABLE IF EXISTS tipo_alerta CASCADE;

-- Eliminar la tabla Estado_alerta y todas las relaciones asociadas
DROP TABLE IF EXISTS estado_alerta CASCADE;

-- Eliminar la tabla Tipo_ave y todas las relaciones asociadas
DROP TABLE IF EXISTS tipo_ave CASCADE;

-- Eliminar la tabla Caracteristicas_incubacion y todas las relaciones asociadas
DROP TABLE IF EXISTS caracteristicas_incubacion CASCADE;

-- Eliminar la tabla Estados_huevos y todas las relaciones asociadas
DROP TABLE IF EXISTS estados_huevos CASCADE;
