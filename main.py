import sqlite3

conn = sqlite3.connect('escola')

cursor = conn.cursor()

cursor.execute("""
    SELECT * FROM escola
""")

def addUsuario(nome, curso, email, senha):
    pass

conn.commit()
cursor.close()
conn.close()



print("Aplicativo de acesso ao BD")