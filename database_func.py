
import sqlite3


#print functions
#----------------------------------------------------------------------------------------

#print all inputs from a table
#cursor is the database cursor class where the connection is established
#tableName is the name of the table
#sortBy is the table attribute you want to sort by (alphabetically)
def printSortedTable(cursor, tableName, sortBy):
	print(tableName+' sorted by '+ sortBy+":")
	for row in cursor.execute('SELECT * FROM ' + tableName + ' ORDER BY '+ sortBy):
		print row
	print("")

#print all inputs from a table
#cursor is the database cursor class where the connection is established
#tableName is the name of the table
def printTable(cursor, tableName):
	print(tableName + ":")
	for row in cursor.execute('SELECT * FROM ' + tableName):
		print row
	print("")

#print 1 row from a tables
#cursor is the database cursor class where the connection is established
#tableName is the name of the table
#attribute is the table column name
#field is the the specific attribute you want to retrieve 
def printTuple(cursor, tableName, attribute, field):
	#print title
	print('From table '+tableName+' where '+attribute+' = '+field+':')
	# ',' is needed to limit binding to 1
	field = (field,)
	#execute query
	cursor.execute('SELECT * FROM Recipe WHERE '+attribute+'=?', field)
	
	#the for loop is to print the tuple w/o type signifier 
	#the | is to separate attributes 
	print('|'),
	for element in cursor.fetchone():
		print(element),
		print('|'), 
	print("\n")
#----------------------------------------------------------------------------------------


#SQL functions
#----------------------------------------------------------------------------------------

#retrieve 1 row from a tables
#cursor is the database cursor class where the connection is established
#tableName is the name of the table
#attribute is the table column name
#field is the the specific attribute you want to retrieve 
def retrieveTuple(cursor, tableName, attribute, field):
	# ',' is needed to limit binding to 1
	field = (field,)
	#execute query
	cursor.execute('SELECT * FROM '+tableName+' WHERE '+attribute+'=?', field)
	return cursor.fetchone()
	
#adds a new row to the table Recipe
#cursor is the database cursor class where the connection is established
#name is the name of the Recipe
#ingredient 1-7 are ingredients used in recipe
#amount 1-7 are the amount (in teaspoon) 
def insertNewRecipe(cursor, name, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, amount1, amount2, amount3, amount4, amount5, amount6, amount7):
	#add ' ' to all strings that aren't NULL
	if ingredient1 != 'NULL':
		ingredient1 = '\''+ingredient1+'\'' 
	if ingredient2 != 'NULL':
		ingredient2 = '\''+ingredient2+'\'' 
	if ingredient3 != 'NULL':
		ingredient3 = '\''+ingredient3+'\'' 
	if ingredient4 != 'NULL':
		ingredient4 = '\''+ingredient4+'\'' 
	if ingredient5 != 'NULL':
		ingredient5 = '\''+ingredient5+'\'' 
	if ingredient6 != 'NULL':
		ingredient6 = '\''+ingredient6+'\'' 
	if ingredient7 != 'NULL':
		ingredient7 = '\''+ingredient7+'\'' 
	if amount1 != 'NULL':
		amount1 = '\''+amount1+'\'' 
	if amount2 != 'NULL':
		amount2 = '\''+amount2+'\''
	if amount3 != 'NULL':
		amount3 = '\''+amount3+'\'' 
	if amount4 != 'NULL':
		amount4 = '\''+amount4+'\''
	if amount5 != 'NULL':
		amount5 = '\''+amount5+'\'' 
	if amount6 != 'NULL':
		amount6 = '\''+amount6+'\''
	if amount7 != 'NULL':
		amount7 = '\''+amount7+'\'' 
	#name cannot be NULL
	name = '\''+name+'\''

	cursor.execute(	'INSERT INTO Recipe VALUES ('
						+name+', ' 
						+ingredient1+', '
						+ingredient2+', '
						+ingredient3+', '
						+ingredient4+', '
						+ingredient5+', '
						+ingredient6+', '
						+ingredient7+', '
						+amount1+', '
						+amount2+', '
						+amount3+', '
						+amount4+', '
						+amount5+', '
						+amount6+', '
						+amount7+' )'
				  )

#add a new row to the table Spice
#name is the name of the spice
#gpt is grams per tsp
#available is if the spice is attached to the machine
def insertNewSpice(cursor, name, gpt, available):
	#sqlite doesn't have manual locking mechanism
	#see create transaction if explicit locking is neccessary
	#cursor.execute('LOCK TABLES Spice WRITE;')
	cursor.execute(	"INSERT INTO Spice VALUES ("
						+'\''+name+'\', '
						+gpt+', '
						+available+' )'
				  )
	#cursor.execute('UNLOCK TABLES;')

#retrieve 1 row from a tables
#cursor is the database cursor class where the connection is established
#tableName is the name of the table
#attribute is the table column name
#field is the the specific attribute you want to retrieve 
def deleteTuple(cursor, tableName, attribute, field):
	# ',' is needed to limit binding to 1
	field = (field,)
	#execute query
	cursor.execute('DELETE FROM '+tableName+' WHERE '+attribute+'=?', field)

#----------------------------------------------------------------------------------------


#Conversion functions
#----------------------------------------------------------------------------------------

#convert ounce to grams
def OunceToGram(ounce):
	return ounce*28.8495

#convert grams to ounce
def GramToOunce(gram):
	return gram/28.8495

#convert Kg to grams
def KgToGram(kilogram):
	return kilogram*1000

#convert grams to Kg
def GramToKg(gram):
	return gram/1000

#convert pounds to grams
def PoundToGram(Pound):
	return Pound*453.592

#convert grams to pounds
def PoundGramTo(gram):
	return gram/453.592

#convert tsp to cup
def TspToCup(tsp):
	return Tsp/48

def CupToTsp(Cup):
	return Cup*48

def GramToTsp(cursor, gram, name):
	row = retrieveTuple(cursor, 'Spice', 'Name', name)
	GramsPerTsp = row[1]
	return gram/GramsPerTsp

def TspToGram(cursor, tsp, name):
	row = retrieveTuple(cursor, 'Spice', 'Name', name)
	GramsPerTsp = row[1]
	return GramsPerTsp*tsp
#----------------------------------------------------------------------------------------	
