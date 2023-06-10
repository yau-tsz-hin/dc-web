from flask import Flask, render_template, request, redirect, url_for    

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    # 執行你想要做的事情
    return redirect('https://youtu.be/UIp6_0kct_U')

# You must keep the routes at the end.
from app import routes, errors