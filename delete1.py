import sqlite3

conn = sqlite3.connect('accounts.db')

cur = conn.cursor()

argument = input('id of row to delete: ')
# Delete an entire row based on an argument
cur.execute("DELETE FROM EOS WHERE id = '{}'".format(argument))
conn.commit()

conn.close()
