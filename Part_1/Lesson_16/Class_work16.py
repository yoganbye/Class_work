# Работа с базами данными в питон

# SQL Lite - дефолтная изичная тема

# import sqlite3#Модуль для работы с SQL lite


# conn = sqlite3.connect('Chinook_Sqlite.sqlite')#Подключаем БД и прописываем путь

# cursor = conn.cursor()#Запросы в БД

# cursor.execute("SELECT * FROM artists ORDER BY Name LIMIT 3")#Метод который выполняет запрос в БД; запрос осуществляется на нативном SQL
# # result = cursor.fetchall()#Забираем данные запроса
# # result2 = cursor.fetchall()#Второй раз fetchall данный не прочитает, т.к. в курсоре они удалились

# result = cursor.fetchmany(2)#Возвращает необходимое количество данных

# # result1 = cursor.fetchone()#Возвращает необходимое количество данных, на четвертом one баганет
# # result2 = cursor.fetchone()
# # result3 = cursor.fetchone()

# print(result)
# # print(result1)
# # print(result2)
# # print(result3)

# conn.close()#Закрывает БД


#______________________________________________________________________________________________________

# Запись в базу
# Получаем данные из базы и таблицу не изменяем, если мы изменяем базу, то обзяательно нужно делать commit
# т.к. наши данные без комита сохраняются в кэш

# conn = sqlite3.connect('Chinook_Sqlite.sqlite')

# cursor = conn.cursor()

# cursor.executescript("""
#     INSERT INTO artists VALUES (NULL, 'A Aagrh1');
#     INSERT INTO artists VALUES (NULL, 'A Aagrh2')
# """)#Если много буков)) можно в тройные кавычки; Можно делать только один запрос за раз!! Можно разделять запросы на execute либо excutescript

# conn.commit()#сохранение вновь добавленных данных в БД

# cursor.execute("SELECT * FROM artists ORDER BY Name LIMIT 3")
# result = cursor.fetchall()

# print(result)

# conn.close()


#______________________________________________________________________________________________________

# Вставка данных в строчку запроса
# Несколько значений на лекции не получилось сделать:(

# conn = sqlite3.connect('Chinook_Sqlite.sqlite')

# cursor = conn.cursor()

# # cursor.execute("SELECT * FROM artists ORDER BY Name LIMIT ?", ('2',))#в кортеже перечисляем данные
# cursor.execute("SELECT * FROM artists ORDER BY Name LIMIT :limit", {"limit":4})#в cловаре перечисляем данные

# result = cursor.fetchall()
# print(result)
# conn.close()

#______________________________________________________________________________________________________

#Итерация БД и обработка ошибок

# conn = sqlite3.connect('Chinook_Sqlite.sqlite')

# cursor = conn.cursor()

# try:
#     for row in cursor.execute("SELECT * FROM artists ORDER BY Name LIMIT :limit", {"limit":4}):
#         print(row)
# except sqlite3.DatabaseError as err:
#     print(err)

# conn.close()

#______________________________________________________________________________________________________

#with за место прописи close

# with sqlite3.connect('Chinook_Sqlite.sqlite') as conn:

#     cursor = conn.cursor()
#     for row in cursor.execute("SELECT * FROM artists ORDER BY Name LIMIT :limit", {"limit":4}):
#         print(row)

#______________________________________________________________________________________________________
#______________________________________________________________________________________________________
#______________________________________________________________________________________________________

# SQL Alchemy - позволяет работать с разными БД; Реализует ORM (ООП)
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey


engine = create_engine('sqlite:///:memory', echo=True)#Подключение с БД; sqlite:///:memory - <БД>:///:<Куда сохраняться, 
                                                                #в данном случае в кэщ>, echo - логгировани
# metadata = MetaData()#Метаданные нашей таблицы
# users_table = Table('Users', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('fullname', String),
#     Column('password', String)
    )#Таблица и её колонки
#Column('name', String(50))

# metadata.create_all(engine)


#______________________________________________________________________________________________________

from sqlalchemy.orm import mapper

class User:
    def __init_(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s', '%s', '%s')>" % (self.name, self.fullname, self.password)

mapper(User, users_table)

user = User('Vasya', 'Man', 'Manovich')
print(user)
print(user.id)