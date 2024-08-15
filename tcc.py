from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
import urllib.parse

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('''<html>
                <body>
                    <h1>Página Inicial</h1>
                    <form action="/login" method="post">
                        <input type="text" name="login" placeholder="Usuário" required>
                        <input type="password" name="senha" placeholder="Senha" required>
                        <button type="submit">Entrar</button>
                    </form>
                </body>
                </html>'''.encode('utf-8'))
        elif self.path == '/login':
            self.send_response(404)
            self.end_headers()  # Não deve ter GET para essa rota

    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            # Decodificar os dados do formulário
            data = urllib.parse.parse_qs(post_data.decode('utf-8'))
            login = data.get('login', [None])[0]
            senha = data.get('senha', [None])[0]

            if verifica_usuario(login, senha):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body><h1>Login bem-sucedido!</h1></body></html>')
            else:
                self.send_response(403)  # Proibido
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body><h1>Login ou senha incorretos!</h1></body></html>')

def verifica_usuario(login, senha):
    conn = sqlite3.connect('meu_banco_de_dados.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM usuarios WHERE login=? AND senha=?", (login, senha))
    usuario = cursor.fetchone()
    
    conn.close()
    
    return usuario is not None

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servindo na porta {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
