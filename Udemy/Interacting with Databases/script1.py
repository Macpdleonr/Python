import psycopg2


def create_table():
  conn = psycopg2.connect("dbname='database1' user='postgres' password='1234' host='localhost' port='5417'")

  cur = conn.cursor()

  cur.execute("CREATE TABLE IF NOT EXISTS STORE (item TEXT, quantity INTEGER, price REAL)")

  conn.commit()
  conn.close()

def insert(item, quantity, price):
  conn = psycopg2.connect("dbname='database1' user='postgres' password='1234' host='localhost' port='5417'")

  cur = conn.cursor()

  cur.execute("INSERT INTO STORE VALUES('%s','%s','%s')" % (item, quantity, price))

  conn.commit()
  conn.close()

# insert("Water Glass", 10, 5)

def view():
  conn = psycopg2.connect("dbname='database1' user='postgres' password='1234' host='localhost' port='5417'")

  cur = conn.cursor()

  cur.execute("SELECT * FROM STORE")
  rows = cur.fetchall()

  conn.close()
  return rows

def delete(item):
  conn = psycopg2.connect("dbname='database1' user='postgres' password='1234' host='localhost' port='5417'")

  cur = conn.cursor()

  cur.execute("DELETE FROM STORE WHERE item=?",(item,))
  conn.commit()
  conn.close()

# delete("Water Glass")

def update(quantity,price,item):
  conn = psycopg2.connect("dbname='database1' user='postgres' password='1234' host='localhost' port='5417'")

  cur = conn.cursor()

  cur.execute("UPDATE STORE SET quantity=?, price=? WHERE item=?",(quantity,price,item))
  conn.commit()
  conn.close()

update(11,6,"Water Glass")
insert("Apple", 10, 15)
print(view())