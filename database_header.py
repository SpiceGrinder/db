
from database_func import *
from conversion_func import *

#SQL commands 
#----------------------------------------------------------------------------------------

#delete tables
#have to be separate for each table since since execute only does 1 cmd at a time
deleteRecipeTable = 	'DROP TABLE IF EXISTS `Recipe`;' 
deleteSpiceTable	 = 	'DROP TABLE IF EXISTS `Spice`;'

#create tables
createSpiceTable = '''CREATE TABLE Spice
			            (
			            	id INTEGER PRIMARY KEY AUTOINCREMENT,
			             	name text NOT NULL DEFAULT '', 
			             	grams_per_tsp real,
			             	available BIT DEFAULT 0 	
			
			         	)
			       '''

createRecipeTable = '''	CREATE TABLE Recipe
		             	(
		             		id INTEGER PRIMARY KEY AUTOINCREMENT,
			             	name text NOT NULL DEFAULT '', 
			             	ingredient1 text,
			             	ingredient2 text,
			             	ingredient3 text,
			             	ingredient4 text,
			             	ingredient5 text,
			             	ingredient6 text,
			             	ingredient7 text DEFAULT NULL, 
			             	amount1 real,
			             	amount2 real,
			             	amount3 real,
			             	amount4 real,
			             	amount5 real,
			             	amount6 real,
			             	amount7 real DEFAULT NULL, 
							
							CONSTRAINT realspice_1 
							FOREIGN KEY (ingredient1) 
							REFERENCES Spice (name),

							CONSTRAINT realspice_2 
							FOREIGN KEY (ingredient2) 
							REFERENCES Spice (name),

							CONSTRAINT realspice_3 
							FOREIGN KEY (ingredient3) 
							REFERENCES Spice (name),

							CONSTRAINT realspice_4 
							FOREIGN KEY (ingredient4) 
							REFERENCES Spice (name),

							CONSTRAINT realspice_5 
							FOREIGN KEY (ingredient5) 
							REFERENCES Spice (name),

							CONSTRAINT realspice_6 
							FOREIGN KEY (ingredient6) 
							REFERENCES Spice (name)

						)
					'''

#----------------------------------------------------------------------------------------
