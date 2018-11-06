






DROP TABLE IF EXISTS `Recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Recipe` (
`Name` varchar(50) NOT NULL DEFAULT '',
`Ingredient1` varchar(50) DEFAULT NULL,
`Ingredient2` varchar(50) DEFAULT NULL,
`Ingredient3` varchar(50) DEFAULT NULL,
`Ingredient4` varchar(50) DEFAULT NULL,
`Ingredient5` varchar(50) DEFAULT NULL,
`Ingredient6` varchar(50) DEFAULT NULL,
`Ingredient7` varchar(50) DEFAULT NULL,
`Amount1` float(5) DEFAULT NULL,
`Amount2` float(5) DEFAULT NULL,
`Amount3` float(5) DEFAULT NULL,
`Amount4` float(5) DEFAULT NULL,
`Amount5` float(5) DEFAULT NULL,
`Amount6` float(5) DEFAULT NULL,
`Amount7` float(5) DEFAULT NULL,
PRIMARY KEY (`Name`),
CONSTRAINT `flightinstance_ibfk_1` FOREIGN KEY (`Ingredient1`) REFERENCES `Spices` (`Name`),
CONSTRAINT `flightinstance_ibfk_2` FOREIGN KEY (`Ingredient2`) REFERENCES `Spices` (`Name`),
CONSTRAINT `flightinstance_ibfk_3` FOREIGN KEY (`Ingredient3`) REFERENCES `Spices` (`Name`),
CONSTRAINT `flightinstance_ibfk_4` FOREIGN KEY (`Ingredient4`) REFERENCES `Spices` (`Name`),
CONSTRAINT `flightinstance_ibfk_5` FOREIGN KEY (`Ingredient5`) REFERENCES `Spices` (`Name`),
CONSTRAINT `flightinstance_ibfk_6` FOREIGN KEY (`Ingredient6`) REFERENCES `Spices` (`Name`),
CONSTRAINT `flightinstance_ibfk_7` FOREIGN KEY (`Ingredient7`) REFERENCES `Spices` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

/*
LOCK TABLES `Recipe` WRITE;
/*!40000 ALTER TABLE `Recipe` DISABLE KEYS ;
INSERT INTO `Recipe` VALUES 
('Curr','Baltimore','MD'),
('SFO','San Francisco','CA');
/*!40000 ALTER TABLE `Recipe` ENABLE KEYS ;
UNLOCK TABLES;
*/