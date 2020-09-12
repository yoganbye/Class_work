# https://sqliteonline.com/

# Галопом по SQL. Краткие основы БД
# https://sqliteonline.com/
# postqreSQL
# Создать таблицу
# CREATE TABLE months (ID INT PRIMARY KEY, NAME VARCHAR(10), DAYS INT, QUARTER INT);
#                     <NAME> <TYPE DATA>
# PRIMARY KEY - Уникальное поле

# Запрос создает данные (со значениями)
# INSERT INTO months VALUES(1, 'January', 31, 1);
# INSERT INTO months VALUES(2, 'February', 29, 1), (3, 'March', 31, 1);

# Вывод типа данных
# SELECT * FROM months; * - <Тип данных>

# Вывод типа данных с условием
# SELECT * FROM months WHERE days>=30;

# Указание на отсортировку по атрибуту
# SELECT * from months ORDER BY days;
# SELECT * from months ORDER BY days DESC;
# desc - сортировка от большего к меньшему
# ASC - от меньшего к большему

#Проверяет входит ли тип данных в указанные значение
# SELECT * from months WHERE days IN (29, 30);
# BETWEEN - В ПРОМЕЖУТКЕ
# LITE - ищет по шаблону

# Обновление строчек
# UPDATE months SET days = 31 where name = 'May';

# Удаление записи
# Обязательно нужно указывать услвие иначе удаляться все поля
# DELETE from months WHERE NAME = 'May';

# TRUNCATE - очищает таблицу