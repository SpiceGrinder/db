
'''	see 
	https://docs.python.org/2/library/sqlite3.html
	for some documentations on sqlite
'''

import sqlite3


#get functions from database_func.py in same directory
from database_func import *

#make a connection
conn = sqlite3.connect('BurrGrinder.db')

#make cursor object to execute sql commands
c = conn.cursor()

#house cleaning
#delete table if it already exist
c.execute("DROP TABLE IF EXISTS `Recipe`;")
c.execute("DROP TABLE IF EXISTS `Spice`;")

#create tables
c.execute('''CREATE TABLE Spice
            (
             	Name text NOT NULL DEFAULT '', 
             	GramsPerTsp real,
             	Available BIT DEFAULT 0, 
             	PRIMARY KEY (Name)
         	
         	)'''
         )

#amount is in tsp
#to get grams, mult. time GramsPerTsp in Table Spice
c.execute('''	CREATE TABLE Recipe
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

				)'''
		)

# Insert rows of data 1 by 1

'''
c.execute("INSERT INTO Spice VALUES ('Pepper', 6.4, 1)")
c.execute("INSERT INTO Spice VALUES ('Salt', 5.69, 1)")
c.execute("INSERT INTO Spice VALUES ('Paprika', 1.6, 0)")
c.execute("INSERT INTO Spice VALUES ('Parsley', 2.1, 0)")
c.execute("INSERT INTO Spice VALUES ('Cinnamon', 2.3, 0)")
c.execute("INSERT INTO Spice VALUES ('Cloves', 6.6, 0)")
'''

# Insert rows of data all at once using a list
spices = [
			('Pepper', 6.4, 1),
			('Salt', 5.69, 1),
			('Paprika', 1.6, 0),
			('Parsley', 2.1, 0),
			('Cinnamon', 2.3, 0),
			('Cloves', 6.6, 0) 
		 ]

#the ? are how many fields in each value not how many elements in the list
#example: the table `Spice` has 3 attributes so 3 ?
c.executemany('INSERT INTO Spice VALUES (?, ?, ?)', spices)

#add 1st recipe using SQLite syntax 
#this method takes 1 arg 
c.execute('''	INSERT INTO Recipe 
				VALUES 	(	'The Monstrosity', 
							'Pepper',
							'Salt',
							'Paprika',
							'Parley',
							'Cinnamon',
							'Cloves',
							Null,
							2.5,
							8.2,
							1.73,
							2.127,
							12.31,
							0.53,
							NULL
						)

		''')

#add 2nd recipe using function from database_func
#takes multiple arguments
#this method is easier for variables (specifically user input)
insertNewRecipe(c, 	'Too much Cloves', 
					'Cloves',  
					'Cloves', 
					'Cloves', 
					'Cloves', 
					'Cloves', 
					'NULL', 
					'NULL', 
					'2', 
					'2', 
					'2', 
					'2', 
					'2', 
					'NULL', 
					'NULL')

#add a new individual spice using a function from database_func
insertNewSpice(c, 'curry powder',  '6.3', '0')

#in the connection c, delete from the table Recipe where Name is Too much Cloves
deleteTuple(c, 'Recipe', 'Name', 'Too much Cloves')

# Save (commit) the changes
conn.commit()

#all print functions are from database_func.py
printSortedTable(c, 'Spice', 'Available')
printTable(c, 'Spice')
printTuple(c, 'Recipe', 'Name', 'The Monstrosity')
printTable(c, 'Recipe')
print(retrieveTuple(c, 'Recipe', 'Name', 'The Monstrosity'))

print('')
print('5 tsp of Pepper is '),
print(TspToGram(c, 5 ,'Pepper')),
print(" grams")

print('81 grams of salt is '),
print(GramToTsp(c, 81 ,'Salt')),
print(" tsp")

#program termination indicator
print("")
print("program ran sucessfully")

# Close the connection when done
# Be sure any changes have been committed or they will be lost
conn.close()
