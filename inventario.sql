CREATE DATABASE inventario;

USE inventario;

CREATE TABLE itens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    modelo VARCHAR(100),
    marca VARCHAR(100),
    quantidade INT
);

CREATE TABLE historico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT,
    quem VARCHAR(100) NOT NULL,
    data_retirada DATETIME,
    quantidade_retirada INT,
    FOREIGN KEY (item_id) REFERENCES itens(id)
);
