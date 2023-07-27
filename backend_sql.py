import sqlite3 as sql3


class Info_Contact():
    def __init__(self, LName, FName, Number, Email):
        self.LName = LName
        self.FName = FName
        self.Number = Number
        self.Email = Email

    #функция SQL создания БД
    def sql_query(self):
        # если база уже есть, то она просто откроется, иначе создастся
        connection = sql3.connect('Contacts.db')
        cursor = connection.cursor()  # для выполнения sql запросов

        cursor.execute('''CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                              LName VARCHAR(250), 
                                                              FName VARCHAR(250), 
                                                              Number VARCHAR(20),  
                                                              Email VARCHAR(250))''')

        cursor.execute('''INSERT INTO contact (LName, FName, Number, Email) VALUES (?,?,?,?)''',
                       (self.LName, self.FName, self.Number, self.Email))
        connection.commit()

        cursor.execute('''SELECT * FROM contact''')
        rows = cursor.fetchall()
        connection.close()

        return self.process_rows(list(rows))


    #фунция распаковки списка, и отправки данных
    def process_rows(self, rows_list):
        for row in rows_list:
            id = row[0]
            print(id)
            a = row[1]
            print(a)
            b = row[2]
            print(b)
            c = row[3]
            print(c)
            d = row[4]
            print(d)






























