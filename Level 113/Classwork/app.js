const express = require("express");

const app = express();
app.use(express.json())

// params

let products = [
    {id: 2352, name: "Web Camera", price: 125},
    {id: 14532, name: "Microphone", price: 3463},
    {id: 2521, name: "Headphones", price: 341}
]


app.get("/products", (req, res) => {
    res.json(products)
})

app.get("/products/:id", (req, res) => {
    const {id} = req.params;

    const product = products.find((p) => p.id === parseInt(id))
    if (product) {
        res.status(200)
        return res.json(product)
    }

    res.status(404).json({message: "Product with specificed id couldn't be found"})
})

app.post('/products', (req, res) => {
    const {name, price} = req.body;

    if(!name || !price) {
        return res.status(400).send("Provided information isn't enough")
    }
    
    const product = {
        id: Date.now(),
        name,
        price
    }

    products.push(product)
    res.status(201).send("Product added successfuly")
})

app.delete('/products/:id', (req, res) => {
    const {id} = req.params;

    const productIndex = products.findIndex((prod) => prod.id === parseInt(id))
    
    if(productIndex === -1) {
        return res.status(404).send(`Product with ${id} couldn't be found`)
    }

    products.splice(productIndex, 1)

    res.status(204).send('Product successfuly removed')
})

app.put("/products/:id", (req, res) => {
    const {id} = req.params;
    const {price} = req.body;

    if (!price) {
        return res.status(400).send("incomplete data")
    }

    const foundIndex = products.findIndex(p => p.id === parseInt(id))

    if(foundIndex === -1) {
        return res.status(404).send("invalid id")
    }

    products[foundIndex] = {
        ...(products[foundIndex]),
        price: price
    }

    res.status(200).send("successfully")
})

app.listen(3000)