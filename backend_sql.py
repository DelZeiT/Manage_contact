import sqlite3 as sql3

# если база уже есть, то она просто откроется, иначе создастся
connection = sql3.connect('Contacts.db')
cursor = connection.cursor() # для выполнения sql запросов

cursor.execute('''CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                      LName VARCHAR(250), 
                                                      FName VARCHAR(250), 
                                                      Number INTEGER,  
                                                      Email VARCHAR(250))''')

cursor.execute('''INSERT INTO contact (LName, FName, Number, Email) VALUES (?,?,?,?)''', ('Пупкин', 'Вася', 8999000, 'vasya@gmail.com'))

connection.commit()



cursor.execute('''SELECT * FROM contact''')
rows = cursor.fetchall()
for row in rows:
    print(*row)


connection.close()

















