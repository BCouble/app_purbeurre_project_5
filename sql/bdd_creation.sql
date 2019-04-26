CREATE DATABASE purbeurre CHARACTER SET 'utf8';
CREATE USER 'purb'@'localhost' IDENTIFIED BY 'purb456!';
GRANT ALL PRIVILEGES ON purbeurre.* TO 'purb'@'localhost';