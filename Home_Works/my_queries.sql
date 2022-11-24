-- 5 студентов с наибольшим средним баллом по всем предметам.
SELECT s.name_student, round (avg(g.grade), 2) AS avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 5;

--1 студент с наивысшим средним баллом по одному предмету.
SELECT sb.name_subject, s.name_student, round (avg(g.grade), 2) AS avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN subjects sb ON sb.id = g.subject_id
WHERE sb.id = 1
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 1;

--средний балл в группе по одному предмету.
SELECT sb.name_subject, gr.name_group, round (avg(g.grade), 2) AS avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN subjects sb ON sb.id = g.subject_id
LEFT JOIN [groups] gr ON gr.id = s.group_id
WHERE sb.id = 4
GROUP BY gr.name_group
ORDER BY avg_grade DESC;

--Средний балл в потоке.
SELECT gr.name_group, round (avg(g.grade), 2) AS avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN [groups] gr ON gr.id = s.group_id
WHERE gr.id = 1;


-- Какие курсы читает преподаватель.
SELECT t.name_teacher, sb.name_subject
FROM teachers t
LEFT JOIN subjects sb ON t.id = sb.teacher_id
WHERE t.id = 3;


--Список студентов в группе.
SELECT gr.name_group, s.name_student
FROM [groups] gr
LEFT JOIN students s ON s.group_id  = gr.id
WHERE gr.id = 3;

--Оценки студентов в группе по предмету.
SELECT s.name_student, g.grade, sb.name_subject, gr.name_group, g.date_of
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN subjects sb ON sb.id = g.subject_id
LEFT JOIN [groups] gr ON gr.id = s.group_id
WHERE sb.id = 2 AND gr.id = 1;

--Оценки студентов в группе по предмету на последнем занятии.
SELECT  s.name_student, g.grade, sb.name_subject, gr.name_group, g.date_of
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN subjects sb ON sb.id = g.subject_id
LEFT JOIN [groups] gr ON gr.id = s.group_id
WHERE sb.id = 3 AND gr.id = 2 AND g.date_of = (SELECT g.date_of
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN subjects sb ON sb.id = g.subject_id
LEFT JOIN [groups] gr ON gr.id = s.group_id
WHERE sb.id = 3 AND gr.id = 2
ORDER BY g.date_of DESC
LIMIT 1);

-- Список курсов, которые посещает студент.
SELECT DISTINCT s.name_student, sb.name_subject
FROM students s
LEFT JOIN grades g  ON s.id = g.student_id
LEFT JOIN subjects sb ON sb.id = g.subject_id
WHERE s.id = 2
ORDER BY sb.name_subject  DESC;


--Список курсов, которые студенту читает преподаватель.
SELECT DISTINCT s.name_student, sb.name_subject, t.name_teacher
FROM students s
LEFT JOIN grades g  ON s.id = g.student_id
LEFT JOIN subjects sb ON sb.id = g.subject_id
LEFT JOIN teachers t  ON t.id = sb.teacher_id
WHERE s.id = 2 AND t.id = 3

--Средний балл, который преподаватель ставит студенту.
SELECT s.name_student, t.name_teacher, round (avg(g.grade), 2) AS avg_grade
FROM students s
LEFT JOIN grades g  ON s.id = g.student_id
LEFT JOIN subjects sb ON sb.id = g.subject_id
LEFT JOIN teachers t  ON t.id = sb.teacher_id
WHERE s.id = 2 AND t.id = 1

--Средний балл, который ставит преподаватель.
SELECT t.name_teacher, round (avg(g.grade), 2) AS avg_grade
FROM grades g

LEFT JOIN subjects sb ON sb.id = g.subject_id
LEFT JOIN teachers t  ON t.id = sb.teacher_id
GROUP BY t.name_teacher
ORDER BY avg_grade DESC;