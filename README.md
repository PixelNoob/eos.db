# eos.db
__EOS Accounts Database and Query examples__

The eos.db repository is composed by a list of python scripts that query a database of all EOS Accounts and their balances to perform different actions and study the token distribution on EOS Mainnet.

To use it you first need to download the .csv file provided by [EOS Newyork](https://www.eosnewyork.io). For reference I have included the snapshot "20200318_account_snapshot.csv" in the repository, but you should get a more recent snapshot from https://www.eossnapshots.io and download it in your eos.db directory. 

    wget https://www.eossnapshots.io/data/2020-03/20200318_account_snapshot.csv 

You would also need to change the [add2database.py line](https://github.com/PixelNoob/eos.db/blob/999682b13a08c02f2b459ebdd6ae749a9ea3b347/add2database.py#L5) that specifies the .csv directory to put in the database. 

    readfile=open('<YOUR_DOWNLOADED_CSV_FILE>','r', newline='')

The name of each query script tells you pretty much what they do:

* add2database.py = Creates Database, inserts Accounts and Balances, deletes first row that contains unnecesary strings. 
* zero.py = Accounts with 0 EOS. 
* nonzero.py = Accounts with more than 0 EOS.
* top100.py = top 100 EOS holders. (includes eosio accounts)
* more10.py = Accounts with more than 10 EOS.
* more100.py = Accounts with more than 100 EOS.
* more1000.py = Accounts with more than 1.000 EOS.
* 1million.py = Accounts with over 1 million EOS.
* delete1.py = Delete row with specified row id. 
* query_account.py = Query an specific account.
* read_all.py = Read and count all rows from database.
* read_csv.py = Read and count all rows from .csv


### SUMMARY

1 Download your desired snapshot from https://www.eossnapshots.io. <br/>
2 Run the *add2database.py* script to populate the database. <br/>
3 Run your desired script to query the database or create your own and contribute to the repo :). 
