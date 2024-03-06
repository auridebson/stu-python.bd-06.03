import sqlite3

conn = sqlite3.connect('escola')

cursor = conn.cursor()



cursor.execute("""
    SELECT * FROM alunos

""")

