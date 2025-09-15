import sqlite3
def create_table():
  conn = sqlite3.connect('lite.db')

  cur = conn.cursor()

  conn.commit()
  conn.close()

def insert(item, quantity, price):
  conn = sqlite3.connect('lite.db')

  cur = conn.cursor()

  cur.execute("INSERT INTO STORE VALUES(?,?,?)",(item, quantity, price))

  conn.commit()
  conn.close()

insert("Coffee Cup", 10, 5)

def view():
  conn = sqlite3.connect('lite.db')

  cur = conn.cursor()

  cur.execute("SELECT * FROM STORE")
  rows = cur.fetchall()

  conn.close()
  return rows

print(view())