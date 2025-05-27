import sqlite3

def get_connection():
    connection = sqlite3.connect('quiz.db')
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    correct_option INTEGER NOT NULL) ''')
    connection.commit()
    connection.close()

def add_question(q, o1, o2, o3, o4, correct):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(''' 
    INSERT INTO questions (question, option1, option2, option3 , option4, correct_option)
    VALUES (?, ?, ?, ?, ?, ?)''', (q, o1, o2, o3, o4, correct))
    connection.commit()
    connection.close()

def get_questions():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM questions')
    questions = cursor.fetchall()
    connection.close()
    return questions
