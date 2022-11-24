from datetime import datetime
from datetime import date
import faker
from faker_education import SchoolProvider
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 5
NUMBER_TEACHERS = 3
NUMBER_GRADES = 20

def generate_fake_data(number_students, number_teachers) -> tuple():
    fake_students = []
    fake_teachers = []

    '''Возьмём три компании из faker и поместим их в нужную переменную'''
    fake_data = faker.Faker('ru-RU')
    fake_data_school = SchoolProvider

    # Сгенерируем набор students
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Сгенерируем set teachers
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    fake_groups = ['EK141', 'EK121', 'EK115']

    fake_subjects = ['Math', 'Chemistry', 'IT', 'Philosophy', 'Geography']

    fake_grades = []

    return fake_students, fake_groups, fake_subjects, fake_teachers, fake_grades

def prepare_data(students, groups, subjects, teachers, grades) -> tuple():

    # подготавливаем список кортежей students
    for_students = []

    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    # подготавливаем список кортежей groups
    for_groups = []
    for group in groups:
        for_groups.append((group, ))

    # подготавливаем список кортежей subjects
    for_subjects = []

    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    # подготавливаем список кортежей teachers
    for_teachers = []

    for teacher in teachers:
        for_teachers.append((teacher, ))

    # подготавливаем список кортежей grades
    for_grades = []
    for sb in range(1, NUMBER_SUBJECTS+1):
        for st in range(1, NUMBER_STUDENTS+1):
            for _ in range(1, NUMBER_GRADES+1):
                for_grades.append((st, sb, date(2022, randint(1, 11), randint(1, 28)), randint(2, 5)))

    return for_students, for_groups, for_subjects, for_teachers, for_grades

def insert_data_to_db(students, groups, subjects, teachers, grades) -> None:
    # Создадим соединение с нашей БД и получим объект курсора для манипуляций с данными

    with sqlite3.connect('hw_sql_3.db') as con:

        cur = con.cursor()

        '''Заполняем таблицу students. И создаем скрипт для вставки, где переменные, которые будем вставлять отметим
        знаком заполнителя (?) '''

        sql_to_students = """INSERT INTO students(name_student, group_id)
                               VALUES (?, ?)"""

        '''Для вставки сразу всех данных воспользуемся методом executemany курсора. Первым параметром будет текст
        скрипта, а вторым данные (список кортежей).'''

        cur.executemany(sql_to_students, students)

        # Далее вставляем данные о groups. Напишем для него скрипт и укажем переменные

        sql_to_groups = """INSERT INTO groups(name_group)
                               VALUES (?)"""

        # Данные были подготовлены заранее, потому просто передаем их в функцию

        cur.executemany(sql_to_groups, groups)

        # Далее вставляем данные о subjects. Напишем для него скрипт и укажем переменные

        sql_to_subjects = """INSERT INTO subjects(name_subject, teacher_id)
                              VALUES (?, ?)"""

        # Вставляем данные о subjects

        cur.executemany(sql_to_subjects, subjects)

        # Далее вставляем данные о teachers. Напишем для него скрипт и укажем переменные

        sql_to_teachers = """INSERT INTO teachers(name_teacher)
                                     VALUES (?)"""

        cur.executemany(sql_to_teachers, teachers)

        # Далее вставляем данные о grades. Напишем для него скрипт и укажем переменные

        sql_to_grades = """INSERT INTO grades(student_id, subject_id, date_of, grade)
                                     VALUES (?, ?, ?, ?)"""

        cur.executemany(sql_to_grades, grades)

        # Фиксируем наши изменения в БД

        con.commit()


if __name__ == "__main__":
    students, groups, subjects, teachers, grades = generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS)
    print('FAKE DATA:')
    print(students)
    print(groups)
    print(subjects)
    print(teachers)
    print(grades)
    students, groups, subjects, teachers, grades = prepare_data(students, groups, subjects, teachers, grades)
    print('PREPEARED DATA:')
    print(students)
    print(groups)
    print(subjects)
    print(teachers)
    print(grades)
    insert_data_to_db(students, groups, subjects, teachers, grades)