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

# Rota para deletar uma tarefa

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__app__':
    app.run(debug=True)