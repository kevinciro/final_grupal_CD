-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema final
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema final
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `final` DEFAULT CHARACTER SET utf8 ;
USE `final` ;

-- -----------------------------------------------------
-- Table `final`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `age` INT NULL,
  `password` VARCHAR(200) NULL,
  `dni` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `final`.`fligths`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final`.`fligths` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `departure_date` DATETIME NULL,
  `departure_hour` DATETIME NULL,
  `departure_place` VARCHAR(45) NULL,
  `destiny_place` VARCHAR(45) NULL,
  `total_seats` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `final`.`bills`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final`.`bills` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `total_price` DOUBLE NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_bills_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_bills_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `final`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `final`.`seats`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final`.`seats` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fligth_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `seat_number` INT NULL,
  `seat_price` DOUBLE NULL,
  `bill_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_compras_vuelos_idx` (`fligth_id` ASC) VISIBLE,
  INDEX `fk_compras_usuarios1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_seats_bills1_idx` (`bill_id` ASC) VISIBLE,
  CONSTRAINT `fk_compras_vuelos`
    FOREIGN KEY (`fligth_id`)
    REFERENCES `final`.`fligths` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_compras_usuarios1`
    FOREIGN KEY (`user_id`)
    REFERENCES `final`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_seats_bills1`
    FOREIGN KEY (`bill_id`)
    REFERENCES `final`.`bills` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
