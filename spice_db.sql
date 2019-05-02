

#drop all tables if they exist; clean slate
DROP TABLE IF EXISTS `Recipe`;
DROP TABLE IF EXISTS `Spice`;

#create the tables

CREATE TABLE Spice
            (
             	Name text NOT NULL DEFAULT '', 
             	GramsPerTsp real,
             	Available BIT DEFAULT 0, 
             	PRIMARY KEY (Name)
         	
         	)

ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

CREATE TABLE Recipe
             	(
	             	name text NOT NULL DEFAULT '', 
	             	Ingredient1 text,
	             	Ingredient2 text,
	             	Ingredient3 text,
	             	Ingredient4 text,
	             	Ingredient5 text,
	             	Ingredient6 text,
	             	Ingredient7 text DEFAULT NULL, 
	             	amount1 real,
	             	amount2 real,
	             	amount3 real,
	             	amount4 real,
	             	amount5 real,
	             	amount6 real,
	             	amount7 real DEFAULT NULL, 
	             	PRIMARY KEY (Name),
					
					CONSTRAINT realspice_1 
					FOREIGN KEY (Ingredient1) 
					REFERENCES Spice (Name),

					CONSTRAINT realspice_2 
					FOREIGN KEY (Ingredient2) 
					REFERENCES Spice (Name),

					CONSTRAINT realspice_3 
					FOREIGN KEY (Ingredient3) 
					REFERENCES Spice (Name),

					CONSTRAINT realspice_4 
					FOREIGN KEY (Ingredient4) 
					REFERENCES Spice (Name),

					CONSTRAINT realspice_5 
					FOREIGN KEY (Ingredient5) 
					REFERENCES Spice (Name),

					CONSTRAINT realspice_6 
					FOREIGN KEY (Ingredient6) 
					REFERENCES Spice (Name)

				) 

ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;


#example insertion

LOCK TABLES Spice WRITE;

INSERT INTO Spice VALUES 
('Pepper', 6.4, 1),
('Salt', 5.69, 1);

UNLOCK TABLES;
