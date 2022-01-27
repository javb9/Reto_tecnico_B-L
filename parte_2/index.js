const express = require('express');
const crypto = require('crypto');
const jwt = require('jsonwebtoken');
const app = express();

const cookieParser = require('cookie-parser');
const { response } = require('express');
app.use(cookieParser());

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

app.set('port', process.env.PORT || 8002);

app.get('/', (req, res) => {
    res.clearCookie('token')
    res.clearCookie('username')
    res.send(`
    <body>
    <form action="/login" method="GET">
        <input id="name" name="name" placeholder="Nombre">
        <input id="pass" name="pass" type="password" placeholder="Contraseña">
        <button type="submit" id="btnSubmit">Iniciar</button>
    </form>
    </body>
    `)
})

app.get('/login', (req, res) => {

    let { pass, name } = req.query;

    const hash = crypto.createHmac('sha256', pass)
        .update('B&L_Secret')
        .digest('hex');

    const llave_hash = crypto.createHmac('sha256', 'clave')
        .update('B&L_Secret')
        .digest('hex');

    if (hash === llave_hash) {
        const payload = {
            check: true,
            usuario: name
        };
        const token = jwt.sign(payload, llave_hash, {
            expiresIn: 1440
        });
        res.cookie('token', token).cookie('username', name)
        res.send('<a href="/interno">Interno</a>')
    } else {
        res.clearCookie('token')
        res.clearCookie('username')
        res.send('<a href="/">Inicio</a>')
    }
    res.json()
});

app.get("/interno", (req, res) => {
    const cookie = req.headers.cookie
    if (cookie) {
        const cookiesData = cookie.split(';')
        const username = cookiesData[1].split('=')[1]
        const username_sin_espacios = username.replace('%20', ' ');
        res.send(`<h1>Bienvenido ${username_sin_espacios}</h1>`)
    } else {
        location.href = '/'
    }
});

app.listen(app.get('port'), () => {
    console.log(`Server run on port ${app.get('port')}`);
});