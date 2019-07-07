-- MySQL Workbench Synchronization
-- Generated: 2019-07-07 21:50
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: admin

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `Pur_Beurre` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `Pur_Beurre`.`food` (
  `idfood` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NULL DEFAULT NULL,
  `dsc` VARCHAR(500) NULL DEFAULT NULL,
  `cat_s2` INT(11) NULL DEFAULT NULL,
  `shop` VARCHAR(200) NULL DEFAULT NULL,
  `url_page` VARCHAR(500) NULL DEFAULT NULL,
  `nutriscore` CHAR(5) NULL DEFAULT NULL,
  PRIMARY KEY (`idfood`),
  INDEX `cat_s2_idx` (`cat_s2` ASC) VISIBLE,
  CONSTRAINT `cat_s2`
    FOREIGN KEY (`cat_s2`)
    REFERENCES `Pur_Beurre`.`s2_category` (`ids2_categorie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Pur_Beurre`.`s0_category` (
  `idcategorie` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idcategorie`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Pur_Beurre`.`s1_category` (
  `idsous_categorie` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `s0_category_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idsous_categorie`),
  INDEX `cat_s0_idx` (`s0_category_id` ASC) VISIBLE,
  CONSTRAINT `cat_s0`
    FOREIGN KEY (`s0_category_id`)
    REFERENCES `Pur_Beurre`.`s0_category` (`idcategorie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Pur_Beurre`.`favorites` (
  `idfavorites` INT(11) NOT NULL AUTO_INCREMENT,
  `id_food` INT(11) NULL DEFAULT NULL,
  `id_substitute` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idfavorites`),
  INDEX `food_idx` (`id_food` ASC) VISIBLE,
  INDEX `sub_idx` (`id_substitute` ASC) VISIBLE,
  CONSTRAINT `food`
    FOREIGN KEY (`id_food`)
    REFERENCES `Pur_Beurre`.`food` (`idfood`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `sub`
    FOREIGN KEY (`id_substitute`)
    REFERENCES `Pur_Beurre`.`food` (`idfood`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `Pur_Beurre`.`s2_category` (
  `ids2_categorie` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `s1_category_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`ids2_categorie`),
  INDEX `cat_s1_idx` (`s1_category_id` ASC) VISIBLE,
  CONSTRAINT `cat_s1`
    FOREIGN KEY (`s1_category_id`)
    REFERENCES `Pur_Beurre`.`s1_category` (`idsous_categorie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
