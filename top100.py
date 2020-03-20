import sqlite3

#open database
conn = sqlite3.connect('accounts.db')
cur = conn.cursor()
count = 0
cur.execute("SELECT Account, Balance FROM EOS ORDER BY Balance DESC LIMIT 100")
for row in cur:
    count = count + 1
    print (count, row)

conn.close()
