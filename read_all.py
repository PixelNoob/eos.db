import sqlite3

#open database
conn = sqlite3.connect('accounts.db')
cur = conn.cursor()

count = 0
cur.execute("SELECT * FROM EOS")
for row in cur:
    print (row)
    count = count + 1

print('There are ', count , 'total entries')

conn.close()
