// const buffer = require("buffer")

// const myBuffer = Buffer.alloc(10, "A")
// myBuffer[1] = 5
// console.log(myBuffer)

// console.log(myBuffer.toString())

// const newBuffer =Buffer.from("treter")
// console.log(Buffer.concat([newBuffer, myBuffer]))

// setImmediate(() => {
//     console.log('Hello! My name is Codey.');
// });

// console.log('Will this line print before or after?');

// console.log("1")
// console.log("2")
// console.log("3")

// setTimeout(() => {
//     console.log("timeouted")
// }, 0);

// console.log('normal')

const http = require("http");
const fs = require("fs");
const PORT = 3000;

// 1. path - ფაილის მისმართი ბილიკი
// 2. encryption/interperation - ინფორმაციის ენკოდირების გზა
// 3. callback ფუნქცია

const server = http.createServer((req, res) => {

    fs.readFile('index.html', 'utf-8', (err, data) => {
        if (err) {
            console.log(err)
            res.writeHead(404)
            res.write("error reading html")
        } else {
            res.writeHead(200, { "Content-Type": "text/html"})
            res.write(data)
        }
        res.end()
    })
})

server.listen(PORT, function(error) {
    if(error) {
        console.log(error)
    } else {
        console.log(`Listening port ${PORT}`)
    }
})