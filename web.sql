-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-05-2023 a las 06:20:13
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `web`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito`
--

CREATE TABLE `carrito` (
  `ID` int(8) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `Color` varchar(255) NOT NULL,
  `Precio` int(8) NOT NULL,
  `imagen` varchar(255) NOT NULL,
  `cantidad` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carrito`
--

INSERT INTO `carrito` (`ID`, `nombre`, `descripcion`, `Color`, `Precio`, `imagen`, `cantidad`) VALUES
(10, 'asd', 'asd', 'asd', 12, '2023203850_4.jpg', 123),
(11, 'qwe', 'qwe', 'qwe', 23, '2023205219_3.jpg', 3),
(12, 'Sudadera', 'Hecho de algodón', 'Blanco', 20, '2023215649_6.jpg', 5),
(13, 'Sudadera', 'hecho de algodón', 'morado', 50, '2023215724_7.jpg', 2),
(14, 'Sudadera', 'Hecha de algodón', 'multi-color', 78, '2023215805_8.jpg', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `ID` int(8) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `Color` varchar(255) NOT NULL,
  `Precio` int(8) NOT NULL,
  `imagen` varchar(255) NOT NULL,
  `cantidad` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`ID`, `nombre`, `descripcion`, `Color`, `Precio`, `imagen`, `cantidad`) VALUES
(4, 'asd', 'asd', 'asd', 12, '2023203850_4.jpg', 123),
(5, 'qwe', 'qwe', 'qwe', 23, '2023205219_3.jpg', 3),
(6, 'Sudadera', 'Hecho de algodón', 'Blanco', 20, '2023215649_6.jpg', 5),
(7, 'Sudadera', 'hecho de algodón', 'morado', 50, '2023215724_7.jpg', 2),
(8, 'Sudadera', 'Hecha de algodón', 'multi-color', 78, '2023215805_8.jpg', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user/pass`
--

CREATE TABLE `user/pass` (
  `Id` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user/pass`
--

INSERT INTO `user/pass` (`Id`, `Nombre`, `Email`, `Password`) VALUES
(1, 'admin', 'admin@gmail.com', 'admin'),
(9, 'prueba', 'prueba@gmail.com', 'prueba'),
(10, 'qwer', 'qwer@gmail.com', 'qwer'),
(11, 'f', 'f@gmail.com', 'f');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `user/pass`
--
ALTER TABLE `user/pass`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `carrito`
--
ALTER TABLE `carrito`
  MODIFY `ID` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `ID` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `user/pass`
--
ALTER TABLE `user/pass`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
