const http = require("http");

const products = [
    {
        productName: "PC",
        price: 1500,
        id: 132
    },
    {
        productName: "Laptop",
        price: 755,
        id: 235
    },
    {
        productName: "headphones",
        price: 200,
        id: 232
    },
]

const server = http.createServer((req, res) => {
    console.log(req.domain)
    if (req.url === "/home") {
        res.writeHead(200, {"Content-Type": "text/plain"})
        return res.end("Home")
    } else if (req.url === "/about") {
        res.statusCode = 200
        return res.end("About")
    } else if (req.url === "/products") {
        res.statusCode = 200
        return res.end(JSON.stringify(products))
    } 

    res.statusCode = 404
    res.end("Resource not found")

})

server.listen(3000)
