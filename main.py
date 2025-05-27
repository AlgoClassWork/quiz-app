from flask import Flask, render_template

app = Flask(__name__)

#http://127.0.0.1:5000/
@app.route('/')
def home():
    return render_template('home_page.html')

app.run()