import csv

readfile=open('20200318_account_snapshot.csv','r', newline='')
readfile=csv.reader(readfile, delimiter=',')

#for row in readfile:
#    print (row)
count = 0
# read second row
for row in readfile:
    print(row[1], row[2])
    count = count + 1

print(count, 'entries')
