// routing - პროცესი server-ზე სხვადასხვა მისამართის და ტიპის მოთხვონების საპასუხო გზების დამატება

// route

// const newUrl = new URL("https://www.localhost3000/profile?user=luka")

// console.log(newUrl)

// const reqUrl = new URL("https://www.localhost3000/" + req.url)
//     console.log(reqUrl)
    
//     if (reqUrl.pathname = "/products") {
//         res.end(JSON.stringify(products))
//     } else if (reqUrl.pathname === "/home") {
//         res.end("Home")
//     } else {
//         res.end("doesn't exist")
//     }


// const { url } = require('inspector/promises');


const http = require('http');
const fs = require("fs");


function readData() {
    return JSON.parse(fs.readFileSync("products.json", "utf-8"))
}

function writeData(data) {
    const products = readData()
    const toWrite = [...products, data]
    fs.writeFileSync('products.json', JSON.stringify(toWrite))
}

let products = readData()

const retriveBody = async (req) => {
    return new Promise((resolve) => {
        let body = ""

        req.on('data', (chunk) => {
            body += chunk.toString()
        })
        
        req.on('end', () => {
            resolve(body);
        })
    })
}
// route
async function postMethod(req, res) {
    const body = await retriveBody(req)
    const data = JSON.parse(body)
    
    const newProduct = {
        id: Date.now(),
        ...data
    }

    products.push(newProduct)
    writeData(newProduct)
    console.log("product added")

    res.writeHead(200)
    res.end(JSON.stringify(products))
}
// route
async function deleteMethod(req, res) {
    const body = await retriveBody(req)
    const { id } = JSON.parse(body)
    
    const filteredProducts = products.filter((product) => product.id !== id)
    writeData(filteredProducts)
}


const server = http.createServer((req, res) => {
    const { method } = req

    switch(method) {
        case "GET":
            res.end("")
            break
        case "POST":
            return postMethod(req, res)
        case "PUT":
            res.end()
            break
        case "DELETE":
            res.end()
            break
        default:  
            res.end("")        
    }
})

server.listen(3000)