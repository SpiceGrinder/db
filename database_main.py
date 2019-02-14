
'''	see 
	https://docs.python.org/2/library/sqlite3.html
	for some documentations on sqlite
'''

import sqlite3


#these python files in same directory
from database_header import *

#make a connection
conn = sqlite3.connect('BurrGrinder.db')

#make cursor object to execute sql commands
c = conn.cursor()

#house cleaning
#delete table if it already exist
c.execute(deleteRecipeTable)
c.execute(deleteSpiceTable)

#create tables
c.execute(createSpiceTable)
c.execute(createRecipeTable)

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
print(retrieveTuple(c, 'Recipe', 'Name', 'The Monstrosity'), '\n')
print('5 tsp of Pepper is', TspToGram(c, 5 ,'Pepper'), 'grams')
print('81 grams of salt is', GramToTsp(c, 81 ,'Salt'), 'tsp')

#program termination indicator
print("\nprogram ran sucessfully")

# Close the connection when done
# Be sure any changes have been committed or they will be lost
conn.close()
