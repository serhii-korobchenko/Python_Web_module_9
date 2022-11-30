import sys

from sqlalchemy import func, desc, and_, distinct, select

from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session

# for 12 select: https://docs.sqlalchemy.org/en/14/core/tutorial.html#scalar-selects

help_message = """
Виберіть який запит ви хочете виконати?
0 -- Вихід
1 -- Знайти 5 студентів з найбільшим середнім балом по всім предметам
2 -- Знайти студента з найбільшим середнім балом з дисципліни. (Перша дисципліна)
3 -- Знайти середній балл в групі по дисципліні. (Друга дисципліна)
4 -- Знайти середній бал на потоці (по всій таблиці grades)
5 -- Які курси веде викладач. (Перший id=1)
6 -- Список студентів в групі. (Перша група)
7 -- Оцінки студентів в окремій групі за конкретною дисципліною.
8 -- Знайти середній балл, який ставить викладач по своїм дисциплінам. (Перший викладач)
9 -- Знайти список курсів, які відвідує студент.
10 -- Знайти список курсів, які конкретному студенту веде конкретний викладач.
11 -- Середній балл, який конкретний викладач ставит конкретному студенту.
12 -- Оцінки студентів в групі по дисципліні на останньому занятті.
"""


def select_1():
    """
    Знайти 5 студентів з найбільшим середнім балом по всім предметам
    :return:
    """
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result


def select_2(student_id: int = 1):
    """
    Знайти студента з найбільшим середнім балом з дисципліни.
    :return:
    """
    result = session.query(Discipline.name, Student.fullname, func.round(func.avg(Grade.grade), 2).label(
        'student_grade')) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline).filter(Student.id == student_id).group_by(Student.id, Discipline.id).order_by(
        desc('student_grade')).limit(1).first()
    return result


def select_3(discipline_id: int = 1):
    """
    Cредний балл в группе по одному предмету.
    :return:
    """
    result = session.query(Discipline.name, Group.name, func.round(func.avg(Grade.grade), 2).label(
        'group_grade')) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(Discipline.id == discipline_id).group_by(Group.id, Discipline.name).order_by(
        desc('group_grade')).all()
    return result


def select_4():
    """
    Знайти середній бал на потоці (по всій таблиці grades)
    :return:
    """
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).select_from(Grade).one()
    return result


def select_5(teacher_id: int = 2):
    """
    -- Какие курсы читает преподаватель.
    :return:
    """
    result = session.query(Teacher.fullname, Discipline.name) \
        .select_from(Teacher) \
        .join(Discipline).filter(Teacher.id == teacher_id).all()
    return result


def select_6(group_id: int = 2):
    """
    -- Список студентов в группе.
    :return:
    """
    result = session.query(Student.id, Student.fullname, Group.name) \
        .select_from(Student) \
        .join(Group).filter(Group.id == group_id).all()
    return result


def select_7(discipline_id: int = 2, group_id: int = 2):
    """
    Cредний балл в группе по одному предмету.
    :return:
    """
    result = session.query(Discipline.name, Group.name, Student.fullname, Grade.date_of, Grade.grade) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(and_(Discipline.id == discipline_id, Group.id == group_id)) \
        .group_by(Discipline.name, Group.name, Student.fullname, Grade.date_of, Grade.grade) \
        .all()
    return result


def select_8(teacher_id: int = 2):
    """
    -- Средний балл, который ставит преподаватель.
    :return:
    """
    result = session.query(distinct(Teacher.fullname), func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(Teacher.id == teacher_id).group_by(Teacher.fullname) \
        .all()
    return result


def select_9(student_id: int = 2):
    """
    -- Список курсов, которые посещает студент.
    :return:
    """
    result = session.query(distinct(Student.fullname), Discipline.name) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Student) \
        .filter(Student.id == student_id).group_by(Student.fullname, Discipline.name) \
        .all()
    return result


def select_10(student_id: int = 2, teacher_id: int = 2):
    """
    -- Список курсов, которые студенту читает преподаватель.
    :return:
    """
    result = session.query(distinct(Student.fullname), Teacher.fullname, Discipline.name) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(and_(Grade.student_id == student_id, Teacher.id == teacher_id)) \
        .group_by(Student.fullname, Teacher.fullname, Discipline.name) \
        .all()
    return result


def select_11(student_id: int = 2, teacher_id: int = 2):
    """
    -- Средний балл, который преподаватель ставит студенту.
    :return:
    """
    result = session.query(distinct(Student.fullname), Teacher.fullname, Discipline.name,
                           func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(and_(Grade.student_id == student_id, Teacher.id == teacher_id)) \
        .group_by(Student.fullname, Teacher.fullname, Discipline.name) \
        .all()
    return result


def select_12(student_id: int = 2, teacher_id: int = 2, discipline_id: int = 2, group_id: int = 2):
    """
    -- Оценки студентов в группе по предмету на последнем занятии.
    :return:
    """
    subq = (select(Grade.date_of).join(Student).join(Group).where(
        and_(Grade.discipline_id == discipline_id, Group.id == group_id)).order_by(desc(Grade.date_of)).limit(
        1).scalar_subquery())

    result = session.query(Student.fullname, Discipline.name, Group.name, Grade.date_of, Grade.grade) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(and_(Group.id == group_id, Discipline.id == discipline_id, Grade.date_of == subq)) \
        .order_by(desc(Grade.date_of)) \
        .all()
    return result


execute_function = [select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10,
                    select_11, select_12]

if __name__ == '__main__':
    print(help_message)
    while True:
        task = int(input("Виберіть номер запиту: "))
        if task == 0:
            sys.exit()
        print(execute_function[task - 1]())