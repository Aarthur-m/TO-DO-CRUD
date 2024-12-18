from database import init_db

from flask import Flask, render_template, request, redirect, url_for

import sqlite3

app = Flask(__name__)

init_db()

# Rota para exibir tarefas

@app.route("/")
def index():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

# Rota para a criação de tarefas

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form['title']
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title) VALUES (?)', (title,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


app.run()