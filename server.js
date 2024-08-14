const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Configuração do banco de dados
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'senai',
    password: '1234',
    database: 'escolatcc'
});

// Conectando ao banco de dados
connection.connect((err) => {
    if (err) {
        console.error('Erro ao conectar ao banco de dados:', err);
        return;
    }
    console.log('Conectado ao banco de dados!');
});

// Exemplo de uma rota para buscar usuários
app.get('/usuarios', (req, res) => {
    connection.query('SELECT * FROM usuarios', (err, results) => {
        if (err) {
            console.error('Erro ao executar a consulta:', err);
            res.status(500).send('Erro ao buscar dados');
            return;
        }
        res.json(results);
    });
});

// Rota para login
app.post('/login', (req, res) => {
    const { login, senha } = req.body;

    // Verificando o usuário no banco de dados
    connection.query('SELECT * FROM usuarios WHERE login = ? AND senha = ?', [login, senha], (err, results) => {
        if (err) {
            console.error('Erro ao executar a consulta:', err);
            return res.status(500).send('Erro ao realizar login');
        }

        // Se o usuário for encontrado
        if (results.length > 0) {
            res.sendFile(path.join(__dirname, 'public', 'admin.html'));
        } else {
            res.status(401).send('Login ou senha inválidos!'); // Retorna erro de login
        }
    });
});

// Servindo arquivos estáticos (HTML, CSS, etc.)
app.use(express.static('public'));

// Iniciar o servidor
app.listen(3000, () => {
    console.log('Servidor rodando na porta 3000');
});
