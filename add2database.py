import sqlite3
import csv

# Open csv file
readfile=open('20200318_account_snapshot.csv','r', newline='')
readfile=csv.reader(readfile, delimiter=',')

conn = sqlite3.connect('accounts.db')
cur = conn.cursor()

cur.execute('CREATE TABLE EOS (id INTEGER PRIMARY KEY AUTOINCREMENT, Account TEXT, Balance FLOAT)')
conn.commit()

count = 0
# read second row
for row in readfile:
    account = row[1]
    balance = row[2]
    count = count + 1
    # add to database
    cur.execute('INSERT INTO EOS (id, Account, Balance) VALUES (NULL, ?, ?)', ('{}'.format(account) , '{}'.format(balance)))

# Delete first row
cur.execute("DELETE FROM EOS WHERE id = 1")

conn.commit()

conn.close()

print(count, 'entries addes to the database')
