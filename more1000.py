import sqlite3

#open database
conn = sqlite3.connect('accounts.db')
cur = conn.cursor()

count = 0
cur.execute("SELECT Account, Balance FROM EOS WHERE Balance > 1000.0 ")
for row in cur:
#    print (row)
    count = count + 1

print('There are ', count , 'accounts with more than 1000 EOS of balance')

conn.close()
