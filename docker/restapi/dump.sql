CREATE DATABASE IF NOT EXISTS `rest_api_db`;
USE `rest_api_db`;

CREATE TABLE IF NOT EXISTS `rest_api_data` (
  `vorname` varchar(50) DEFAULT NULL,
  `nachname` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
