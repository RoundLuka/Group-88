const http = require("http");
const { json } = require("stream/consumers");

const server = http.createServer((req, res) => {
    let body = ""
    req.on("data", (chunk) => {
        body += chunk.toString()
        console.log(chunk)
        console.log(body)
    })

    console.log(body)
    res.write(body)
    res.end()
});

server.listen(3000, () => console.log("Server running on port 3000"))


// protcol: https:
// domain: //www.codewars.com
// path: /kata/search/my-languages
// query: ?q=&r%5B%5D=-5&r%5B%5D=-6&r%5B%5D=-7&xids=played&beta=false&order_by=total_completed%20desc

// 