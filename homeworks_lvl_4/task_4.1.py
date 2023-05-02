# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

# Создаем базу данных и подключаемся к ней
conn = sqlite3.connect('/home/tafflin/Desktop/studies/envs/project/app/homeworks_lvl_4/teacher.db')
cursor = conn.cursor()

# Создаем таблицу Students, предварительно удаляем талицу, если она уже существует
cursor.execute("DROP TABLE IF EXISTS Students")
cursor.execute('''CREATE TABLE Students
                  (Student_Id INTEGER, Student_Name TEXT, School_Id INTEGER PRIMARY KEY)''')

# Заполняем таблицу данными
students_data = [(201, 'Иван', 1),
                 (202, 'Петр', 2),
                 (203, 'Анастасия', 3),
                 (204, 'Игорь', 4)]
cursor.executemany('INSERT INTO Students VALUES (?, ?, ?)', students_data)
# Создаем таблицу Schools
cursor.execute('''CREATE TABLE Schools
                  (School_Id INTEGER PRIMARY KEY, School_Name TEXT)''')

# Заполняем таблицу данными
schools_data = [(1, 'Школа №1'),
                (2, 'Школа №2'),
                (3, 'Школа №3'),
                (4, 'Школа №4')]
cursor.executemany('INSERT INTO Schools VALUES (?, ?)', schools_data)


# Функция для получения информации о студенте и его школе
def get_student_info(student_id):
    # Получаем данные о студенте и его школе
    cursor.execute('''SELECT s.Student_Id, s.Student_Name, s.School_Id, sc.School_Name
                      FROM Students s
                      JOIN Schools sc ON s.School_Id = sc.School_Id
                      WHERE s.Student_Id = ?''', (student_id,))
    result = cursor.fetchone()
    if result:
        # Выводим информацию о студенте и его школе
        print('ID Студента:', result[0])
        print('Имя студента:', result[1])
        print('ID школы:', result[2])
        print('Название школы:', result[3])
    else:
        print('Студент с таким ID не найден')

# Пример использования 
print('---Данные студента 202---')
get_student_info(202)
print('---Данные студента 204---')
get_student_info(204)
#Или можно попросить ввести ID студента
while True:
    student_id = input('Введите ID студента (для выхода введите "q"): ')
    if student_id == 'q':
        break
    try:
        student_id = int(student_id)
        print('---Данные введенного студента ',student_id,'---')
        get_student_info(student_id)
    except ValueError:
        print('Введите корректный ID студента')
