const express = require("express");
const cors = require("cors");
const http = require('http');
const { Server } = require('socket.io');

const server = http.createServer();

const io = new Server(server, {
    cors: "*"
});

io.on('connection', (socket) => {
    console.log(`New socket connected ${socket.id}`)

    socket.on('msg', (msg) => {
        socket.broadcast.emit('receive', msg)
    })
})

server.listen(3000)