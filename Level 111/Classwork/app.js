const express = require("express")
const cors = require("cors")

const app = express()

const data = []

// middleware

app.use(cors({
    origin: ["http://localhost:5173"]
}))
app.use(express.json())
// server.method

// rounting - პროცესი სერვერზე ბევრი როუტების გაწერსია რომ სხვადსხვა სახის მოთხოვნები
// დავამუშაოთ მიღებული კლიენტისგან

// route 
app.get("/home", (req, res) => {

    res.json(data)
})

app.get("/about")



app.delete('/home/main', (req, res) => {
    
})



app.post("/home", (req, res) => {
    const { title, desc} = req.body;

    data.push(
        {
            title,
            desc,
            id: Date.now()
        }
    )


    res.status(201).json({post: "Successful"})
})

app.listen(3000, () => console.log("Server running on port 3000"))