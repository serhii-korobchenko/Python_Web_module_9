--PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_subject VARCHAR(255) UNIQUE NOT NULL,
    teacher_id REFERENCES teachers (id)
);

-- table: groups
DROP TABLE IF EXISTS [groups];
CREATE TABLE [groups] (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name_group VARCHAR(255) UNIQUE
);

-- table: grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id REFERENCES students (id),
    subject_id REFERENCES subjects (id),
    date_of DATA NOT NULL,
    grade INTEGER NOT NULL
);

-- table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_student VARCHAR(255) UNIQUE NOT NULL,
    group_id REFERENCES [groups] (id)
);

-- table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_teacher VARCHAR(255) UNIQUE NOT NULL
);

COMMIT TRANSACTION
--PRAGMA foreign_keys = on;