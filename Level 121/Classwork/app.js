const express = require("express");
const app = express();

// /info/eryeyue

app.use('/info', (req, res, next) => {
    console.log("Request recevied on path info")
    next()
})

app.get("/", (req, res) => {
    res.send("Main Data")
})

app.get("/info/:id", (req, res) => {
    res.send(`Information ${req.params.id}`)
})

// function checkAdmin(req, res, next) {
//     if (req.query.user === "luka") {
//         res.admin = true
//         next()
//     } else {
//         res.send("Not authorized")
//     }
// }


app.listen(3000);