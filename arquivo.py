import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('escolatcc.db')
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL,
        senha INTEGER NOT NULL
    )
''')

# Inserir dados do usuário admin
cursor.execute("INSERT INTO usuarios (login, senha) VALUES ('admin', 'admin123')")

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()
