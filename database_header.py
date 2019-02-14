
from database_func import *
from conversion_func import *

#SQL commands 
#----------------------------------------------------------------------------------------

#delete tables
#have to be separate for each table since since execute only does 1 cmd at a time
deleteRecipeTable = 	'DROP TABLE IF EXISTS `Recipe`;' 
deleteSpiceTable	 = 	'DROP TABLE IF EXISTS `Spice`;'

createSpiceTable = '''CREATE TABLE Spice
			            (
			             	Name text NOT NULL DEFAULT '', 
			             	GramsPerTsp real,
			             	Available BIT DEFAULT 0, 
			             	PRIMARY KEY (Name)
			         	
			         	)
			       '''

createRecipeTable = '''	CREATE TABLE Recipe
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
					'''

#----------------------------------------------------------------------------------------
