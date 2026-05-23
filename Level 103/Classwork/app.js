// node.js

// for (i = 0; i < 10; i++) {
//     console.log(i)
// }

// let isRegistered = true;

// if (isRegistered) {
//     console.log("User is authorized")
// }

// function welcomeMsg() {
//     return "Welcome back to platform"
// }

// console.log(welcomeMsg())

// const { formatDate } = require("./dateFormat.js");

// console.log(formatDate(2026, 5, 23))
// console.log(formatDate(2013, 7, 12))

// if (process.argv[2] === "development") {
//     console.log("Development server up and running")
// } else if (process.argv[2] === "production") {
//     console.log("Production real-time server model")
// }

// console.log(process.memoryUsage())

const os = require('os');

const server = {
    type: os.type(),
    architecture: os.arch(),
    uptime: os.uptime()
}

console.log(server)