import sqlite3, time, datetime, os, psutil

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")


conn = sqlite3.connect('database.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS main(datestamp TEXT, keyword TEXT)')

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    if "League of Legends" in (p.name() for p in psutil.process_iter()):
        keywordOne = "League Opened"
    else:
        keywordOne = "League Not Open"
    c.execute("INSERT INTO main(datestamp, keyword) VALUES (?, ?)", (date, keywordOne))
    conn.commit()

def league_opened():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keywordOne = "League Opened"
    c.execute("INSERT INTO main(datestamp, keyword) VALUES(?, ?)", (date, keywordOne))
    conn.commit()

create_table()
dynamic_data_entry()
print ("Computer Uptime Logged!")

while 1:
    if "League of Legends" in (p.name() for p in psutil.process_iter()):
        league_opened()
        print("League Detected, Logged!")
    else:
        pass