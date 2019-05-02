
from database_func import *

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
	GramsPerTsp = row[2]
	return gram/GramsPerTsp

def TspToGram(cursor, tsp, name):
	row = retrieveTuple(cursor, 'Spice', 'Name', name)
	GramsPerTsp = row[2]
	return GramsPerTsp*tsp
#----------------------------------------------------------------------------------------	
