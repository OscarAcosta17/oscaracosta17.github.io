CREATE TABLE tipos(id INTEGER PRIMARY KEY NOT NULL,
nombre VARCHAR(255) NOT NULL);

INSERT INTO tipos(nombre)
VALUES ("Basura"),
       ("Plástico"),
       ("Aluminio"),
       ("Papel"),
       ("Vidrio");

CREATE TABLE puntos_SJ(id INTEGER PRIMARY KEY NOT NULL,
coorX FLOAT NOT NULL,
coorY FLOAT NOT NULL,
tipo INTEGER,
FOREIGN KEY(tipo) REFERENCES tipos(id));

CREATE TABLE puntos_CC(id INTEGER PRIMARY KEY NOT NULL,
coorX FLOAT NOT NULL,
coorY FLOAT NOT NULL,
tipo INTEGER,
FOREIGN KEY(tipo) REFERENCES tipos(id)); 

INSERT INTO puntos_CC(coorX, coorY, tipo)
VALUES (34.2, 54.3, 4),
       (3.2 , 84.3 , 2),
       (54 , 52.1 , 1),
       (3.5 , 22 , 5),
       (2.37, 62.3, 4);

INSERT INTO puntos_SJ(coorX, coorY, tipo)
VALUES  (1, 2, 1),
        (3, 2, 4),
        (6, 4, 3);

SELECT * FROM puntos_SJ
JOIN tipos ON puntos_SJ.tipo = tipos.id;
SELECT * FROM puntos_CC
JOIN tipos ON puntos_CC.tipo = tipos.id;





