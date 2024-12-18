import sqlite3

def init_db():
    # Conecta ao banco SQLite (ou cria o arquivo "todo.db")
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()
    
    # Cria a tabela `tasks` se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT DEFAULT 'In progress'
        )
    ''')
    connection.commit()
    connection.close()