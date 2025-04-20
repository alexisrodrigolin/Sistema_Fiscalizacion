-- Crear base de datos
CREATE DATABASE IF NOT EXISTS test CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE test;

-- Crear tabla art
CREATE TABLE `art` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `PLU` int DEFAULT NULL,
  `PLU2` int DEFAULT NULL,
  `Precio` double DEFAULT NULL,
  `Marca` text,
  `Descripcion` text,
  `Tipo_Sabor` text,
  `Cantidad` double DEFAULT NULL,
  `Unidad` text,
  `Departamento` text,
  `Pasillo` int DEFAULT NULL,
  `Costo` double DEFAULT NULL,
  `IVA` int DEFAULT NULL,
  `Ganancia` int DEFAULT NULL,
  `Cant1` int DEFAULT NULL,
  `Precio1` double DEFAULT NULL,
  `Cant2` int DEFAULT NULL,
  `Precio2` double DEFAULT NULL,
  `Cant3` int DEFAULT NULL,
  `Precio3` double DEFAULT NULL,
  `Fecha_de_modificacion` text,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla Caja1
CREATE TABLE `Caja1` (
  `Date` datetime NOT NULL,
  `Facturated` int DEFAULT NULL,
  `Non_Facturated` int DEFAULT NULL,
  `Card` int DEFAULT NULL,
  `Cash` int DEFAULT NULL,
  `virtualp` int DEFAULT NULL,
  `Tcard` int DEFAULT NULL,
  `Tcash` int DEFAULT NULL,
  `Tvirtual` int DEFAULT NULL,
  `TCancelled` int DEFAULT NULL,
  `Cancelled` int DEFAULT NULL,
  PRIMARY KEY (`Date`),
  UNIQUE KEY `Date_UNIQUE` (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla etiq
CREATE TABLE `etiq` (
  `ID` int DEFAULT NULL,
  `PLU` bigint DEFAULT NULL,
  `PLU2` int DEFAULT NULL,
  `Precio` double DEFAULT NULL,
  `Marca` text,
  `Descripcion` text,
  `Tipo_Sabor` text,
  `Cantidad` double DEFAULT NULL,
  `Unidad` text,
  `Pasillo` int DEFAULT NULL,
  `Costo` double DEFAULT NULL,
  `IVA` int DEFAULT NULL,
  `Ganancia` int DEFAULT NULL,
  `Cant1` int DEFAULT NULL,
  `Precio1` double DEFAULT NULL,
  `Cant2` int DEFAULT NULL,
  `Precio2` double DEFAULT NULL,
  `Cant3` int DEFAULT NULL,
  `Precio3` double DEFAULT NULL,
  `Fecha_de_modificacion` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla setiq
CREATE TABLE `setiq` (
  `ID` text,
  `PLU` text,
  `PLU2` text,
  `Precio` text,
  `Marca` text,
  `Descripcion` text,
  `Tipo_Sabor` text,
  `Cantidad` text,
  `Unidad` text,
  `Pasillo` text,
  `Costo` text,
  `IVA` text,
  `Ganancia` text,
  `Cant1` text,
  `Precio1` text,
  `Cant2` text,
  `Precio2` text,
  `Cant3` text,
  `Precio3` text,
  `Fecha_de_modificacion` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;