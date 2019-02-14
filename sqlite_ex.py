
'''	example code from 
	https://docs.python.org/2/library/sqlite3.html
'''

import sqlite3

#make a connection
conn = sqlite3.connect('example.db')

#make cursor object
c = conn.cursor()

#delete table if it already exist
c.execute("DROP TABLE IF EXISTS `stocks`;")

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print c.fetchone()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

print("program ran sucessfully")
