# import sqlite3
#
# connection = sqlite3.connect("less10.sl3", 5)
# cur = connection.cursor()
# cur.execute("CREATE TABLE ya_karta (Nazva TEXT);") #1
# connection.commit()
# cur.execute("INSERT INTO ya_tablitsa (Nazva) VALUES ('Ya znachenie')") #2
# connection.commit()
# cur.execute("UPDATE ya_tablitsa SET Nazva='BURGER' WHERE rowid=1")
# cur.execute("SELECT rowid, Nazva FROM ya_tablitsa;") #3
# connection.commit()
# res = cur.fetchall()
# print(res)
# connection.close()

import sqlite3
from bs4 import BeautifulSoup
import requests

connection = sqlite3.connect("less10.sl3", 5)
cur = connection.cursor()


response = requests.get("https://privatbank.ua/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td", {"id" : "USD_sell"})
for elem in soup_list:
    text_1 = elem.text

# cur.execute("CREATE TABLE ya_karta (Data);")
cur.execute(f"INSERT INTO ya_karta (Data) VALUES ('{text_1}')")
connection.commit()
cur.execute("SELECT rowid, Data FROM ya_karta;")
res = cur.fetchall()
print(res)
connection.close()
