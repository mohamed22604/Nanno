import sqlite3

connection = sqlite3.connect("knowledge.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT UNIQUE,
    content TEXT
)
""")

connection.commit()
connection.close()

def get_db():
    connection = sqlite3.connect("knowledge.db")
    return connection

def get_file(file_path: str) -> str:
    file_path = str(file_path)  # Ensure file_path is a string
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT content FROM documents WHERE file_path = ?
    """, (file_path,))

    result = cursor.fetchone()
    connection.close()

    if result:
        return result[0]
    else:
        return None


def save_file_content(file_path: str, content: str):
    file_path = str(file_path)  # Ensure file_path is a string
    content = str(content)  # Ensure content is a string
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO documents (file_path, content)
    VALUES (?, ?)
    """, (file_path, content))

    connection.commit()
    connection.close()

