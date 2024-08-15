import sqlite3

# Função para criar o banco de dados e a tabela
def setup_database():
    conn = sqlite3.connect('meu_banco_de_dados.db')
    cursor = conn.cursor()
    
    # Criar a tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    
    # Inserir dados do usuário admin se não existir
    cursor.execute("SELECT * FROM usuarios WHERE login='admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO usuarios (login, senha) VALUES ('admin', 'admin123')")
    
    # Salvar as alterações e fechar a conexão
    conn.commit()
    conn.close()

# Executa a função para criar o banco de dados
setup_database()
print("Banco de dados configurado com sucesso.")
