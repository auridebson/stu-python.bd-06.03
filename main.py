import sqlite3

conn = sqlite3.connect('escola')

cursor = conn.cursor()

cursor.execute("""
    SELECT * FROM escola
""")

def addUsuario(nome, curso, email, senha):
    pass

def criar_tabela_alunos():
    # Conectar ao banco de dados (o arquivo será criado se não existir)
    conexao = sqlite3.connect('exemplo.db')

    # Criar um cursor para interagir com o banco de dados
    cursor = conexao.cursor()

    # Executar comando SQL para criar a tabela
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            curso TEXT,
            email TEXT
        )
    ''')





conn.commit()
cursor.close()
conn.close()

