const mysql = require('mysql2');

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'senai',
    password: '1234',
    database: 'escola'
});

connection.connect((err) => {
    if (err) {
        console.error('Erro ao conectar ao banco de dados:', err);
        return;
    }
    console.log('Conectado ao banco de dados!');
});

connection.query('SELECT * FROM usuarios', (err, results) => {
    if (err) {
        console.error('Erro ao executar a consulta:', err);
        return;
    }
    console.log('Resultados da consulta:', results);
});

connection.end();
