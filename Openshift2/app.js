
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send({
        message: 'Hola mundito'
    })
    console.log('hola mundito');
})


app.listen(8080,'0.0.0.0', () => {
    console.log(`Proyecto Aide escuchando en el puerto secreto`);
})