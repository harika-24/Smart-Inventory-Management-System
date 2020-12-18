import psycopg2
conn = 0
def start():
    global conn
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "jelly", host = "localhost", port = "5432")
    print("Opened database successfully")
def insert_and_update_stmt(st):
    cur = conn.cursor()
    cur.execute(st)
    conn.commit()
    cur.close()
def select_stmt(st):
    cur = conn.cursor()
    cur.execute(st)
    r=cur.fetchall()
    conn.commit()
    cur.close()
    return r
def truncate_tab():
    cur = conn.cursor()
    cur.execute("Truncate products;")
    conn.commit()
    cur.close()
def close_conn():
    conn.close()
    
##connect()
##execute_stmt("Insert into products(name,count) values('Dove',20)")
##close_conn()
