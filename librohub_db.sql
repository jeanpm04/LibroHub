-- Crear la base de datos
CREATE DATABASE librohub_db;

-- Usar la base de datos
USE librohub_db;

-- Crear la tabla 'libros'
CREATE TABLE libros (
  id INT(11) NOT NULL AUTO_INCREMENT,
  titulo VARCHAR(255) NOT NULL,
  autor VARCHAR(255) NOT NULL,
  anio_publicacion INT(11) DEFAULT NULL,
  genero VARCHAR(100) DEFAULT NULL,
  PRIMARY KEY (id)
);

-- Insertar registros en la tabla 'libros'
INSERT INTO libros (titulo, autor, anio_publicacion, genero) VALUES
('Cien años de soledad', 'Gabriel García Márquez', 1967, 'Novela'),
('Don Quijote de la Mancha', 'Miguel de Cervantes', 1605, 'Novela'),
('Crimen y castigo', 'Fyodor Dostoevsky', 1866, 'Novela'),
('Orgullo y prejuicio', 'Jane Austen', 1813, 'Romance'),
('1984', 'George Orwell', 1949, 'Distopía'),
('El gran Gatsby', 'F. Scott Fitzgerald', 1925, 'Novela'),
('Matar a un ruiseñor', 'Harper Lee', 1960, 'Novela'),
('La Odisea', 'Homero', NULL, 'Épica'),
('En busca del tiempo perdido', 'Marcel Proust', 1913, 'Novela'),
('Ulises', 'James Joyce', 1922, 'Novela'),
('El retrato de Dorian Gray', 'Oscar Wilde', 1890, 'Novela Gótica'),
('La metamorfosis', 'Franz Kafka', 1915, 'Ficción'),
('Los miserables', 'Victor Hugo', 1862, 'Drama'),
('Fahrenheit 451', 'Ray Bradbury', 1953, 'Distopía'),
('Divina Comedia', 'Dante Alighieri', NULL, 'Poesía Épica'),
('El nombre de la rosa', 'Umberto Eco', 1980, 'Misterio'),
('Cumbres borrascosas', 'Emily Brontë', 1847, 'Romance'),
('El señor de los anillos', 'J.R.R. Tolkien', 1954, 'Fantasía'),
('Jane Eyre', 'Charlotte Brontë', 1847, 'Novela'),
('El extranjero', 'Albert Camus', 1942, 'Filosofía');

SELECT * FROM libros;