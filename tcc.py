import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('escolatcc.db')
cursor = conn.cursor()

# Função para adicionar um novo usuário
def add_user(login, senha):
    cursor.execute('INSERT INTO usuarios (login, senha) VALUES (?, ?)', (login, senha))
    conn.commit()

# Exemplo de como adicionar um usuário
add_user('admin', 'admin123')

# Fechar a conexão
conn.close()
print("Usuário adicionado.")
