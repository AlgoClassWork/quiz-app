import database
from flask import Flask, render_template

app = Flask(__name__)

#http://127.0.0.1:5000/
@app.route('/')
def home():
    return render_template('home_page.html')

#http://127.0.0.1:5000/start_quiz


database.create_table()
app.run()