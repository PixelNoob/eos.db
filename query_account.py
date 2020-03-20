import sqlite3

#open database
conn = sqlite3.connect('accounts.db')
cur = conn.cursor()

query = input("Name of Account: ")

# get row containing -
cur.execute("SELECT Account, Balance FROM EOS WHERE Account LIKE '%{}%'".format(query))
for row in cur:
    print (row)

conn.close()
