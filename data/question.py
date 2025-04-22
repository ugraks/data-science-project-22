import psycopg2

def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="testdb",
    user="postgres",
    password="postgres")
    return conn


def question_1_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students WHERE age > 22;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM courses WHERE category = \'Veritabanı\';')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students WHERE first_name LIKE \'A%\';')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM courses WHERE course_name LIKE \'%SQL%\'')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students WHERE age BETWEEN 22 AND 24;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.first_name, s.last_name FROM students s INNER JOIN enrollments e ON s.student_id = e.student_id;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, COUNT(e.enrollment_id) AS student_count FROM courses c LEFT JOIN enrollments e ON c.course_id = e.course_id WHERE c.category = \'Veritabanı\' GROUP BY c.course_name;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, i.name AS instructor_name FROM courses c JOIN course_instructors ci ON c.course_id = ci.course_id JOIN instructors i ON ci.instructor_id = i.instructor_id;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students WHERE student_id NOT IN (SELECT student_id FROM enrollments);')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, AVG(s.age) AS avg_age FROM courses c JOIN enrollments e ON c.course_id = e.course_id JOIN students s ON s.student_id = e.student_id GROUP BY c.course_name;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_11_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.first_name, s.last_name, COUNT(e.course_id) AS total_courses FROM students s LEFT JOIN enrollments e ON s.student_id = e.student_id GROUP BY s.student_id;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_12_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT i.name, COUNT(ci.course_id) AS total_courses FROM instructors i JOIN course_instructors ci ON i.instructor_id = ci.instructor_id GROUP BY i.instructor_id HAVING COUNT(ci.course_id) > 1;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_13_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, COUNT(DISTINCT e.student_id) AS unique_students FROM courses c JOIN enrollments e ON c.course_id = e.course_id GROUP BY c.course_name;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_14_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.first_name, s.last_name FROM students s WHERE student_id IN (SELECT e1.student_id FROM enrollments e1 JOIN enrollments e2 ON e1.student_id = e2.student_id WHERE e1.course_id = 1 AND e2.course_id = 2);')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_15_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.first_name, s.last_name, c.course_name, i.name AS instructor_name, e.enrollment_date FROM students s JOIN enrollments e ON s.student_id = e.student_id JOIN courses c ON c.course_id = e.course_id JOIN course_instructors ci ON c.course_id = ci.course_id JOIN instructors i ON i.instructor_id = ci.instructor_id;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data