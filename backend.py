import sqlite3

def connect():
    conn=sqlite3.connect('Books.db')
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text,author text,year integer,isbn integer)')
    conn.commit()
    conn.close()
    
def insert(title,author,year,isbn):
    conn=sqlite3.connect('Books.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO book VALUES (NULL,?,?,?,?)',(title,author,year,isbn))
    conn.commit()
    conn.close()         
    
def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect('Books.db')
    cur=conn.cursor()
    cur.execute('SELECT *FROM book WHERE title=? OR author=? OR year=? OR isbn=?',(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows 

def delete(id):
    conn=sqlite3.connect('Books.db')
    cur=conn.cursor()
    cur.execute('DELETE FROM book WHERE id=?',(id,))
    conn.commit()
    conn.close()
    
def update(id, title, author, year, isbn):
    conn = sqlite3.connect('Books.db')
    cur = conn.cursor()
    cur.execute('UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?', 
                (title, author, year, isbn, id))
    conn.commit()
    conn.close()
    
    


    
    
def view(): 
    conn=sqlite3.connect('Books.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM book')
    rows=cur.fetchall()
    conn.close()
    return rows
  
connect()

# insert('Peera Kamil',"Umera Ahmed",2000,89897987)
# insert('Abe hayat',"Umeraa Ahmed",2000,8987)
# insert('halim',"Umeraaa Ahmed",2000,8989787)
# update(2,"u","la",2002,4598)
# print(view())
# print(search(author="Umeraa Ahmed"))
# delete(3)