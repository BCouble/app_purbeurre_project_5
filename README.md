# app_purbeurre_project_5

pip install -r requirement.txt

## 1 creation of the Repositories:

https://github.com/BCouble/app_purbeurre_project_5/blob/master/README.md

## 2 creation of the trello:

![Trello off](https://github.com/BCouble/app_purbeurre_project_5/blob/master/image/trello_off_fin.PNG) 

## 3 creating the database and SQL script for MySQL:

### creation of the database:
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

	exemple : SOURCE c:/chemin_absolut/tables.sql;
	
	SOURCE C:/Users/admin/Desktop/cour_python/projet_5_PurBeurre/app_purbeurre_project_5/sql/create_shema.sql;


## 4 creation of a python class to search in the Open Food Fact (OFF) database:

### Study of the API operation:

- with the URL : https://fr.openfoodfacts.org/api/v0/cgi/search.pl exemple fichier off.py
- with : import openfoodfacts exemple file pb.py
- the search criteria defined in the constant.py file


To import the data: 
    
    insert_data.py 
    
To launch the application:

    pb.py

