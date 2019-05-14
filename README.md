# app_purbeurre_project_5

install connect mysql : pip install mysql-connector-python

## 1 création du Repositories : 

https://github.com/BCouble/app_purbeurre_project_5/blob/master/README.md

## 2 création du trello : 

![Trello off](https://github.com/BCouble/app_purbeurre_project_5/blob/master/image/trello_off.PNG) 

## 3 Création de la base de donnee et du script SQL pour MySQL

### Creation of the database :
- in the console connect to mysql and type the command :
	
	mysql -h localhost -u root -p
	CREATE DATABASE purbeurre CHARACTER SET 'utf8';
	CREATE USER 'purb'@'localhost' IDENTIFIED BY 'purb456!';
	GRANT ALL PRIVILEGES ON purbeurre.* TO 'purb'@'localhost';
	EXIT;

- connect to the database with the user "purb":
	
	mysql -h localhost -u purb -p
	"taper le mot de passe"

### Creating Food, Category, and Substitute Tables :

	USE purbeurre
	SOURCE "c:\chemin_absolut\tables_creation.sql";

Problematic:

ERROR 1215 (HY000): Cannot add foreign key constraint

The columns did not have any UNSIGNED which caused an error in the creation of foreign keys (Resolved)

## 4 Création d'une classe en python pour rechercher dans la base Open Food Fact (OFF)

### Etude du fonctionnement de l'API

- Avec l'url : https://fr.openfoodfacts.org/api/v0/cgi/search.pl exemple fichier off.py
- ou avec : import openfoodfacts exemple fichier pb.py
- Critère de recherche définit dans le fichier constant.py


pip install -r requirements.txt 
python -m pip install flask

