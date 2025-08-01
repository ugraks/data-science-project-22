import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = 'postgres'


def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password=password)
    return conn


def question_1_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students WHERE age > 22')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM courses WHERE category = 'Veritabanı'")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE first_name LIKE 'A%'")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM courses WHERE course_name LIKE '%SQL%'")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students WHERE age BETWEEN 22 AND 24')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT first_name, last_name FROM students')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT c.course_name, COUNT(DISTINCT e.student_id) AS student_count FROM courses AS c JOIN enrollments AS e ON c.course_id = e.course_id WHERE c.category = 'Veritabanı' GROUP BY c.course_name")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, i.name as instructor_name FROM courses AS c JOIN course_instructors as ci ON c.course_id = ci.course_id JOIN instructors as i ON ci.instructor_id = i.instructor_id')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.* FROM students AS s LEFT JOIN enrollments AS e ON s.student_id = e.student_id WHERE e.enrollment_id IS NULL;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, AVG(s.age) as avg_age FROM students as s JOIN enrollments as e  ON s.student_id = e.student_id  JOIN courses as c  ON c.course_id = e.course_id  GROUP BY c.course_name')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_11_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.first_name, s.last_name, COUNT(e.student_id) as total_courses FROM students as s JOIN enrollments as e ON s.student_id = e.student_id JOIN courses as c ON c.course_id = e.course_id GROUP BY s.first_name, s.last_name')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_12_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT i.name AS instructor_name, COUNT(ci.instructor_id) AS total_courses FROM instructors AS i JOIN course_instructors AS ci ON i.instructor_id = ci.instructor_id JOIN courses AS c ON c.course_id = ci.course_id GROUP BY i.name HAVING COUNT(ci.instructor_id) > 1;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_13_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, COUNT(e.student_id) as unique_students FROM enrollments as e LEFT JOIN courses as c ON c.course_id = e.course_id GROUP BY c.course_name')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_14_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT s.first_name, s.last_name FROM students AS s JOIN enrollments AS e ON s.student_id = e.student_id JOIN courses AS c ON c.course_id = e.course_id WHERE c.course_name IN ('SQL Temelleri', 'İleri SQL') GROUP BY s.student_id, s.first_name, s.last_name HAVING COUNT(DISTINCT c.course_name) = 2;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_15_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.first_name, s.last_name, c.course_name, i.name as instructor_name, e.enrollment_date FROM enrollments as e LEFT JOIN students as s ON e.student_id = s.student_id LEFT JOIN courses as c ON c.course_id= e.course_id LEFT JOIN course_instructors as ci ON c.course_id = ci.course_id LEFT JOIN instructors as i ON ci.instructor_id = i.instructor_id')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data