import  sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute('''
    creat table students
     st_id Int auto_increment primary key,
     st_name varchar(50),
     st_class varchar(10)  
     st_emil verchar(30)
    
    ''')

conn.close()