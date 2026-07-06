const express = require("express");
const app = express();
const morgan = require("morgan");

// morgan is request logging open source library with utils
app.use(morgan('tiny'))

// /info/eryeyue

app.get("/", (req, res, next) => {
    next('Credentials invlaid')
})

app.get("/info/:id", (req, res, next) => {
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

// specific (excluded) middleware to handle errors
// only middleware that can take 4 arguments

app.use((err, req, res, next) => {
    console.log(err)
})


app.listen(3000);