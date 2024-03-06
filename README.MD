============================ MATERIAL DA AULA ======================================

https://diegosmp.notion.site/SQL-Infinity-3e5da26a3521495a9059e2e63a47b9e4?pvs=74    ---- NOTION

=============================================================================================

CREATE DATABASE IF NOT EXISTS escola;

use escola;

CREATE TABLE alunos (
	id_aluno INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    curso VARCHAR(50),
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(20)
);


INSERT INTO alunos(nome, curso, email, senha)
VALUES ('Diego', 'Python', 'diego@email.com', '12345asb');



SELECT nome,email FROM alunos;

