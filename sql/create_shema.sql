-- MySQL Workbench Synchronization
-- Generated: 2019-06-04 09:30
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: admin

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `purbeurre` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `purbeurre`.`categorie` (
  `id` SMALLINT(6) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 0
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `purbeurre`.`food` (
  `id` SMALLINT(6) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NOT NULL,
  `description` VARCHAR(400) NULL DEFAULT NULL,
  `id_categorie` SMALLINT(6) UNSIGNED NOT NULL,
  `shops` VARCHAR(200) NULL DEFAULT NULL,
  `date_save` DATETIME NOT NULL,
  `url_page_off` VARCHAR(500) NULL DEFAULT NULL,
  `nutriscore` CHAR(5) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_categorie_id` (`id_categorie` ASC) VISIBLE,
  CONSTRAINT `fk_categorie_id`
    FOREIGN KEY (`id_categorie`)
    REFERENCES `purbeurre`.`categorie` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 0
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `purbeurre`.`substitutes` (
  `id` SMALLINT(6) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_produit` SMALLINT(10) NULL DEFAULT NULL,
  `id_substitute` SMALLINT(10) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 0
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
