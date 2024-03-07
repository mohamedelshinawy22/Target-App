import sqlite3

def create_db():
    #======Customer data base======
    con=sqlite3.connect(database=r'data base\\mis.db')
    cur=con.execute("CREATE TABLE IF NOT EXISTS product(Id INTEGER PRIMARY KEY AUTOINCREMENT,Date text,Category text,Supplier text,Price text,Quantity text,Total text,Note text,Madfo3 text)")
    con.commit()
    
    cur=con.execute("CREATE TABLE IF NOT EXISTS product2(Id INTEGER PRIMARY KEY AUTOINCREMENT,Date text,Category text,Supplier text,Price text,Quantity text,Total text,Note text,Madfo3 text)")
    con.commit()
    cur=con.execute("CREATE TABLE IF NOT EXISTS category(Category_Id INTEGER PRIMARY KEY AUTOINCREMENT,Name text)")
    con.commit()
    
    cur=con.execute("CREATE TABLE IF NOT EXISTS supplier(Invoice INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Contact text,Note text)")
    con.commit()
    
    cur=con.execute("CREATE TABLE IF NOT EXISTS supplier2(Invoice INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Contact text,Note text)")
    con.commit()
    
   
    
create_db()