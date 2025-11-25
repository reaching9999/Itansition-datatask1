import sqlite3
import json

def ingest_data(json_path, db_path):

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: JSON file not found at '{json_path}'.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file at '{json_path}' is not a valid JSON file.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    
    cursor.execute('DROP TABLE IF EXISTS books;')

    
    cursor.execute('''
    CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        publication_year INTEGER,
        price_text TEXT
    )
    ''')

    
    for record in data:
        cursor.execute(
            'INSERT INTO books (title, author, publication_year, price_text) VALUES (?, ?, ?, ?)',
            (record.get('title'), record.get('author'), record.get('year'), record.get('price'))
        )

    conn.commit()
    conn.close()

    print(f"Successfully ingested {len(data)} records into '{db_path}'.")

if __name__ == "__main__":
    ingest_data('task1_d_fixed.json', 'book_data.db')