//Passa para a variável express o poder do express
const express = require('express')
//Batiza a variável app como um backend
const app = express()
//Define uma porta para executar o servidor
const PORT = 3000

let data = {
    name : 'james'
}

//Middleware
app.use(express.json())

app.get('/', (req, res) => {
    console.log('Eu consegui chegar no endpoint', req.method)
    res.send(`
        <body>
            <h1>Data:</h1>
            <p>${JSON.stringify(data)}</p>
        </body>
        `)
})

app.get('/api/data', (req, res) => {
    console.log('This one was for data')
    res.send(data)
})
app.post('/api/data', (req, res) => {
    console.log('O post foi feito')
    const newEntry = req.body
    console.log(newEntry)
    res.sendStatus(201)

    res.send(data)
})

//Conecta o servidor na porta definida
app.listen(PORT, () => console.log(`O Server está ligado na porta ${PORT}`))

