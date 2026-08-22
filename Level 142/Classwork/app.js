// Modules
const express = require('express');
const http = require('http');
const cors = require('cors');
const { Server } = require("socket.io")


// server initialization
const app = express();
app.use(cors());

const server = http.createServer(app);

const io = new Server(server, {
    cors: ["http://localhost:5173"],
})

// socket.emit(); // ინდივიდუალურ კლიენთან გაგზვნა
// io.emit() // ყველა კლიენტთან გაგზავნა მოვლენის
// socket.broadcast() // ამ კლიენტის გარდა ყველსთან გამოწვევა მოვლენის

io.on('connection', (socket) => {
    console.log(`Client connected: ${socket.id}`)

    socket.emit("connectSuccess", socket.id)

    socket.on('msgSent', (msg, room) => {
        if (room === "") {
            socket.broadcast.emit('receiveMsg', msg)
        } else {
            socket.to(room).emit('receiveMsg', msg)
        }
    });

    socket.on('joinRoom', room => {
        socket.join(room)
        socket.emit("join-result", `Successfully joined room: ${room}`, room)
    })

    socket.on('privateMsg', (msg, privateId) => {
        io.to(privateId).emit('receiveMsg', msg)
    })
})

app.get('/health',  (req, res ) => {
    res.send("running")
})

server.listen(process.env.PORT || 3000, () => {
    console.log("Server is running on port 3000")
})