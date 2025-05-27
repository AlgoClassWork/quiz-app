import database
from flask import Flask, render_template

app = Flask(__name__)

#http://127.0.0.1:5000/
@app.route('/')
def home():
    return render_template('home_page.html')

#http://127.0.0.1:5000/start_quiz
@app.route('/start_quiz')
def start():
    questions = database.get_questions()
    return render_template('start_quiz.html', questions=questions)

database.create_table()
app.run()