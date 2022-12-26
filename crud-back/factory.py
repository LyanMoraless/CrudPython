import psycopg2 

class Factory:
  conn = psycopg2.connect("dbname=CrudHcosta user=postgres password=123456")
  cur = conn.cursor()

  def create(self):
    self.cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    self.conn.commit()
    self.close_connections()

  def insert(self):
    self.cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
    self.conn.commit()
    self.close_connections()

  def select(self, query):
    self.cur.execute(query)
    data = self.cur.fetchone()
    self.conn.commit() 
    print(data)
    self.close_connections()

  def close_connections(self):
    self.cur.close()
    self.conn.close()

Factory().select()