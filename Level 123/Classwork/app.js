const express = require("express");
const app = express()

let products = [
    {id: 43725252, title: "product1", price: 30},
    {id: 24763573, title: "product2", price: 40},
    {id: 32473473, title: "product3", price: 50},
    {id: 648548, title: "product4", price: 60},
]

app.param('productId', (req, res, next, productId) => {
    const foundProduct = products.find((product) => product.id === parseInt(productId))
    if (!foundProduct) {
        return res.status(404).send({message: "Product with specified id doesn't exist"})
    }
    req.foundProduct = foundProduct
    next()
})

app.get('/', (req, res) => {
    res.send('Home')
})

app.get('/products/:productId', (req, res) => {
    res.json(req.foundProduct)
})

app.delete('/products/:productId', (req, res) => {
    const filteredProducts = products.filter((product) => product.id !== parseInt(req.params.productId))
    products = filteredProducts
    return res.json(products)
})

app.listen(3000)